import re
import socket

EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


def valid_mail(mail: str) -> bool:
    """Valida el formato de un correo usando una expresion regular.

    Args:
        mail: Correo a validar.

    Returns:
        True si el formato es valido, False en caso contrario.
    """
    if not isinstance(mail, str):
        return False
    return bool(re.match(EMAIL_PATTERN, mail))


def valid_domain(mail: str) -> bool:
    """Valida que el dominio del correo exista en DNS.

    Args:
        mail: Correo del cual se extrae el dominio.

    Returns:
        True si el dominio puede resolverse por DNS, False en caso contrario.
    """
    try:
        domain = mail.split("@")[1]
    except IndexError:
        return False

    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False