"""Uitleg over if-statements en loops."""


def if_example(getal):
    """Geeft aan of het getal positief, negatief of nul is."""
    if getal > 0:
        print("Positief")
    elif getal < 0:
        print("Negatief")
    else:
        print("Nul")


def for_example():
    """Loopt over een reeks getallen en toont elk getal."""
    for i in range(3):
        print("For-lus:", i)


def while_example():
    """Aftellen met een while-lus."""
    teller = 3
    while teller > 0:
        print("Teller:", teller)
        teller -= 1


if __name__ == "__main__":
    if_example(1)
    if_example(-2)
    if_example(0)
    for_example()
    while_example()
