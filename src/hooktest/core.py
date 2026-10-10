"""Core logic, kept independent of the CLI layer."""


def greet(name: str) -> str:
    """Return a greeting for ``name``.

    Args:
        name: Non-empty recipient name.

    Raises:
        ValueError: If ``name`` is empty or whitespace only.
    """
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
