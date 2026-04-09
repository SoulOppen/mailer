import os
import smtplib
from email.mime.text import MIMEText
from pathlib import Path
from typing import Callable

import pandas as pd
from dotenv import load_dotenv

from condition import valid_domain, valid_mail
from constants import (
    ATTACHMENTS_SHEET,
    BODY_COLUMNS,
    DEFAULT_DOTENV_PATH,
    DEFAULT_EXCEL_PATH,
    INVALID_DOMAIN_PATH,
    INVALID_DOMAINS_HEADER,
    INVALID_MAIL_HEADER,
    INVALID_MAIL_PATH,
    MAIL_COLUMN,
    MAIL_SHEET,
    SMTP_PASSWORD_ENV,
    SMTP_PORT_ENV,
    SMTP_SERVER_ENV,
    SMTP_USER_ENV,
    SUBJECT_COLUMN,
    TEXT_SHEET,
)
from read_and_write import readTxt, writeTxt


def load_smtp_config(getenv: Callable[[str], str | None] = os.getenv) -> tuple[str, int, str, str]:
    """Carga configuracion SMTP desde variables de entorno.

    Args:
        getenv: Funcion para leer variables de entorno (inyectable para tests).

    Returns:
        Tupla con servidor, puerto, usuario y password.

    Raises:
        ValueError: Si falta alguna variable obligatoria o el puerto no es valido.
    """
    smtp_server = getenv(SMTP_SERVER_ENV)
    smtp_port_raw = getenv(SMTP_PORT_ENV)
    smtp_user = getenv(SMTP_USER_ENV)
    smtp_password = getenv(SMTP_PASSWORD_ENV)

    if not smtp_server or not smtp_port_raw or not smtp_user or not smtp_password:
        raise ValueError("Faltan variables SMTP requeridas en el entorno.")

    try:
        smtp_port = int(smtp_port_raw)
    except ValueError as exc:
        raise ValueError("SMTP_PORT debe ser un entero.") from exc

    return smtp_server, smtp_port, smtp_user, smtp_password


def build_email_body(text_sheet: pd.DataFrame, body_columns: tuple[str, ...] = BODY_COLUMNS) -> str:
    """Construye el cuerpo HTML del correo desde columnas del sheet de texto.

    Args:
        text_sheet: DataFrame de la hoja que contiene bloques de texto.
        body_columns: Columnas que se concatenaran como parrafos HTML.

    Returns:
        Cuerpo HTML completo.
    """
    body_parts: list[str] = []
    for column in body_columns:
        for text in text_sheet[column].dropna().tolist():
            body_parts.append(f"<p>{text}</p>")
    return "\n".join(body_parts)


def send_emails(
    server: smtplib.SMTP,
    recipients: list[str],
    body: str,
    subject: str,
    smtp_user: str,
    invalid_mail: set[str],
    invalid_domains: set[str],
) -> tuple[int, set[str], set[str]]:
    """Envia correos validos y acumula mails/dominios invalidos.

    Args:
        server: Cliente SMTP autenticado.
        recipients: Lista de destinatarios.
        body: Contenido HTML del correo.
        subject: Asunto del correo.
        smtp_user: Cuenta emisora.
        invalid_mail: Set de correos ya invalidados.
        invalid_domains: Set de dominios ya invalidados.

    Returns:
        Tupla con cantidad de envios exitosos y sets actualizados.
    """
    sent_count = 0
    for recipient in recipients:
        if (not valid_mail(recipient)) or recipient in invalid_mail:
            invalid_mail.add(recipient)
            continue

        domain = recipient.split("@")[1]
        if (not valid_domain(recipient)) or domain in invalid_domains:
            invalid_domains.add(domain)
            continue

        message = MIMEText(body, "html")
        message["From"] = smtp_user
        message["Subject"] = subject
        message["To"] = recipient
        server.sendmail(smtp_user, recipient, message.as_string())
        sent_count += 1

    return sent_count, invalid_mail, invalid_domains


def persist_invalid_entries(invalid_mail: set[str], invalid_domains: set[str]) -> None:
    """Persiste correos/dominios invalidos en archivos TXT si hay contenido."""
    if invalid_domains:
        writeTxt(str(INVALID_DOMAIN_PATH), invalid_domains, INVALID_DOMAINS_HEADER)
    if invalid_mail:
        writeTxt(str(INVALID_MAIL_PATH), invalid_mail, INVALID_MAIL_HEADER)


def main(excel_path: str | Path = DEFAULT_EXCEL_PATH, dotenv_path: str | Path = DEFAULT_DOTENV_PATH) -> int:
    """Orquesta la lectura de datos, envio SMTP y persistencia de invalidos.

    Args:
        excel_path: Ruta del archivo Excel origen.
        dotenv_path: Ruta del archivo .env a cargar.

    Returns:
        Cantidad de correos enviados exitosamente.
    """
    load_dotenv(dotenv_path=str(dotenv_path))
    invalid_mail = readTxt(str(INVALID_MAIL_PATH))
    invalid_domains = readTxt(str(INVALID_DOMAIN_PATH))
    smtp_server, smtp_port, smtp_user, smtp_password = load_smtp_config()

    workbook = pd.read_excel(str(excel_path), sheet_name=None)
    recipients = workbook[MAIL_SHEET][MAIL_COLUMN].dropna().tolist()
    subject = workbook[ATTACHMENTS_SHEET].at[0, SUBJECT_COLUMN]
    body = build_email_body(workbook[TEXT_SHEET])

    server = None
    sent_count = 0
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        sent_count, invalid_mail, invalid_domains = send_emails(
            server=server,
            recipients=recipients,
            body=body,
            subject=subject,
            smtp_user=smtp_user,
            invalid_mail=invalid_mail,
            invalid_domains=invalid_domains,
        )
    except Exception as exc:
        print(f"Error durante el envio: {exc}")
    finally:
        if server is not None:
            server.quit()

    persist_invalid_entries(invalid_mail, invalid_domains)
    return sent_count


if __name__ == "__main__":
    total_sent = main()
    print(f"Correos enviados: {total_sent}")