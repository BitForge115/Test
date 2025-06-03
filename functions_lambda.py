"""Voorbeelden van functies en lambda-functies."""


def square(number):
    """Geeft het kwadraat van een getal terug."""
    return number * number


# Een lambda-functie doet hetzelfde maar in één regel
square_lambda = lambda x: x * x


def demo():
    """Toont het gebruik van de gewone functie en de lambda."""
    for i in range(3):
        print("square():", square(i))
        print("lambda:", square_lambda(i))


if __name__ == "__main__":
    demo()
