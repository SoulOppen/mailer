from pathlib import Path

from read_and_write import readTxt, writeTxt


def test_readTxt_returns_empty_set_when_file_does_not_exist(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.txt"
    assert readTxt(str(missing_file)) == set()


def test_readTxt_skips_header_and_empty_lines(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid_mail.txt"
    file_path.write_text("HEADER\na@example.com\n\nb@example.com\n", encoding="utf-8")

    result = readTxt(str(file_path))

    assert result == {"a@example.com", "b@example.com"}


def test_writeTxt_writes_header_and_lines(tmp_path: Path) -> None:
    file_path = tmp_path / "output.txt"
    writeTxt(str(file_path), {"line1", "line2"}, "HEADER")

    content = file_path.read_text(encoding="utf-8").splitlines()
    assert content[0] == "HEADER"
    assert set(content[1:]) == {"line1", "line2"}
