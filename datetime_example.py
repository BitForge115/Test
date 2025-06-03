"""Demonstreert gebruik van het datetime-module."""

from datetime import datetime, timedelta


def tijd_demo():
    """Print de huidige datum en tijd plus een dag."""
    nu = datetime.now()
    morgen = nu + timedelta(days=1)
    print("Nu:", nu)
    print("Morgen:", morgen)


if __name__ == "__main__":
    tijd_demo()
