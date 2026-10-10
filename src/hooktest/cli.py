"""Command line entry point."""

from __future__ import annotations

import argparse
import sys

from hooktest.core import greet


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="hooktest", description="A minimal Python project.")
    parser.add_argument("name", help="Name to greet.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        print(greet(args.name))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
