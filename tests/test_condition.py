import socket

from condition import valid_domain, valid_mail


def test_valid_mail_returns_true_for_valid_email() -> None:
    assert valid_mail("user@example.com") is True


def test_valid_mail_returns_false_for_invalid_email() -> None:
    assert valid_mail("invalid-email") is False


def test_valid_mail_returns_false_for_non_string() -> None:
    assert valid_mail(None) is False


def test_valid_domain_returns_true_when_dns_resolves(monkeypatch) -> None:
    monkeypatch.setattr(socket, "gethostbyname", lambda domain: "127.0.0.1")
    assert valid_domain("user@example.com") is True


def test_valid_domain_returns_false_when_dns_fails(monkeypatch) -> None:
    def _raise_dns_error(domain: str) -> str:
        raise socket.gaierror("dns error")

    monkeypatch.setattr(socket, "gethostbyname", _raise_dns_error)
    assert valid_domain("user@example.com") is False


def test_valid_domain_returns_false_when_email_has_no_domain() -> None:
    assert valid_domain("invalid-email") is False
