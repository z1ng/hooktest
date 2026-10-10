# hooktest

A minimal Python project scaffold (src layout, zero runtime dependencies, pytest + ruff).

## Requirements

- Python >= 3.9

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
hooktest World        # => Hello, World!
python -m hooktest World
```

## Development

```bash
pytest          # run tests
ruff check .    # lint
```

## License

[MIT](LICENSE)
