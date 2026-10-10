import pytest

from hooktest.cli import main
from hooktest.core import greet


def test_greet_returns_message():
    assert greet("World") == "Hello, World!"


def test_greet_rejects_blank_name():
    with pytest.raises(ValueError):
        greet("   ")


def test_cli_prints_greeting(capsys):
    assert main(["World"]) == 0
    assert capsys.readouterr().out == "Hello, World!\n"


def test_cli_reports_error(capsys):
    assert main(["  "]) == 1
    assert "error" in capsys.readouterr().err
