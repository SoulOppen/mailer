"""Constantes centralizadas del proyecto quickMail."""

from pathlib import Path

# Variables de entorno SMTP
SMTP_SERVER_ENV = "SMTP_SERVER"
SMTP_PORT_ENV = "SMTP_PORT"
SMTP_USER_ENV = "SMTP_USER"
SMTP_PASSWORD_ENV = "SMTP_PASSWORD"

# Rutas por defecto
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DOTENV_PATH = BASE_DIR / ".env"
INVALID_MAIL_PATH = BASE_DIR / "invalid_mail.txt"
INVALID_DOMAIN_PATH = BASE_DIR / "invalid_domain.txt"
DEFAULT_EXCEL_PATH = BASE_DIR / "data" / "Prototipo.xlsm"

# Encabezados de archivos de salida
INVALID_DOMAINS_HEADER = "Invalid Domains Found"
INVALID_MAIL_HEADER = "Invalid Mail Found"

# Estructura esperada del workbook
MAIL_SHEET = "mail"
MAIL_COLUMN = "mail"
ATTACHMENTS_SHEET = "adjuntos"
SUBJECT_COLUMN = "subject"
TEXT_SHEET = "Texto"
BODY_COLUMNS = ("Intro", "Noticia", "Bajada")
