from pathlib import Path

import pandas as pd
import pytest

import main
from constants import ATTACHMENTS_SHEET, MAIL_SHEET, TEXT_SHEET


class DummySMTP:
    def __init__(self, server: str, port: int) -> None:
        self.server = server
        self.port = port
        self.started_tls = False
        self.logged_in = False
        self.sent_messages: list[tuple[str, str, str]] = []
        self.closed = False

    def starttls(self) -> None:
        self.started_tls = True

    def login(self, user: str, password: str) -> None:
        self.logged_in = True

    def sendmail(self, sender: str, recipient: str, message: str) -> None:
        self.sent_messages.append((sender, recipient, message))

    def quit(self) -> None:
        self.closed = True


def build_mock_workbook() -> dict[str, pd.DataFrame]:
    return {
        MAIL_SHEET: pd.DataFrame({"mail": ["ok@example.com", "bad-email", "no-dns@bad.tld"]}),
        ATTACHMENTS_SHEET: pd.DataFrame({"subject": ["Asunto de prueba"]}),
        TEXT_SHEET: pd.DataFrame(
            {
                "Intro": ["Hola"],
                "Noticia": ["Novedades"],
                "Bajada": ["Gracias"],
            }
        ),
    }


def test_load_smtp_config_returns_values() -> None:
    env = {
        "SMTP_SERVER": "smtp.test.local",
        "SMTP_PORT": "587",
        "SMTP_USER": "sender@test.local",
        "SMTP_PASSWORD": "secret",
    }
    config = main.load_smtp_config(getenv=env.get)
    assert config == ("smtp.test.local", 587, "sender@test.local", "secret")


def test_load_smtp_config_raises_when_missing_values() -> None:
    env = {"SMTP_SERVER": "smtp.test.local"}
    with pytest.raises(ValueError):
        main.load_smtp_config(getenv=env.get)


def test_build_email_body_concatenates_columns() -> None:
    sheet = pd.DataFrame({"Intro": ["Hola"], "Noticia": ["Novedad"], "Bajada": ["Chao"]})
    result = main.build_email_body(sheet)
    assert "<p>Hola</p>" in result
    assert "<p>Novedad</p>" in result
    assert "<p>Chao</p>" in result


def test_send_emails_sends_only_valid_recipients(monkeypatch) -> None:
    smtp = DummySMTP("smtp.test.local", 587)
    monkeypatch.setattr(main, "valid_mail", lambda email: email == "ok@example.com")
    monkeypatch.setattr(main, "valid_domain", lambda email: email == "ok@example.com")

    sent_count, invalid_mail, invalid_domains = main.send_emails(
        server=smtp,
        recipients=["ok@example.com", "bad-email", "no-dns@bad.tld"],
        body="<p>Body</p>",
        subject="Subject",
        smtp_user="sender@test.local",
        invalid_mail=set(),
        invalid_domains=set(),
    )

    assert sent_count == 1
    assert len(smtp.sent_messages) == 1
    assert "bad-email" in invalid_mail
    assert "bad.tld" in invalid_domains


def test_persist_invalid_entries_writes_files(monkeypatch) -> None:
    calls: list[tuple[str, set[str], str]] = []

    def fake_write(path: str, lines: set[str], head: str) -> None:
        calls.append((path, lines, head))

    monkeypatch.setattr(main, "writeTxt", fake_write)
    main.persist_invalid_entries({"a@a.com"}, {"domain.com"})

    assert len(calls) == 2


def test_main_runs_flow_and_returns_sent_count(monkeypatch, tmp_path: Path) -> None:
    dotenv_path = tmp_path / ".env"
    excel_path = tmp_path / "fake.xlsm"
    dotenv_path.write_text("", encoding="utf-8")
    excel_path.write_text("placeholder", encoding="utf-8")

    smtp_instance = DummySMTP("smtp.test.local", 587)

    monkeypatch.setattr(main, "load_dotenv", lambda dotenv_path: None)
    monkeypatch.setattr(main, "readTxt", lambda path: set())
    monkeypatch.setattr(main, "persist_invalid_entries", lambda invalid_mail, invalid_domains: None)
    monkeypatch.setattr(main, "load_smtp_config", lambda: ("smtp.test.local", 587, "sender@test.local", "secret"))
    monkeypatch.setattr(main.pd, "read_excel", lambda path, sheet_name=None: build_mock_workbook())
    monkeypatch.setattr(main.smtplib, "SMTP", lambda server, port: smtp_instance)
    monkeypatch.setattr(main, "valid_mail", lambda email: email == "ok@example.com")
    monkeypatch.setattr(main, "valid_domain", lambda email: email == "ok@example.com")

    sent_count = main.main(excel_path=excel_path, dotenv_path=dotenv_path)

    assert sent_count == 1
    assert smtp_instance.started_tls is True
    assert smtp_instance.logged_in is True
    assert smtp_instance.closed is True
