"""Demonstreert basis van exception handling."""


def divide(a, b):
    """Deelt a door b met foutafhandeling."""
    try:
        resultaat = a / b
    except ZeroDivisionError:
        print("Delen door nul kan niet")
    else:
        print("Resultaat:", resultaat)


if __name__ == "__main__":
    divide(10, 2)
    divide(5, 0)
