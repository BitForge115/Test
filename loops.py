"""Voorbeelden van verschillende soorten loops in Python."""


def for_range_example():
    """Itereert over een range van nummers."""
    for i in range(5):
        print(f"Range voorbeeld: {i}")


def for_list_example():
    """Loopt door een lijst en toont index en waarde."""
    kleuren = ["rood", "groen", "blauw"]
    for index, kleur in enumerate(kleuren):
        print(f"{index}: {kleur}")


def while_example():
    """Eenvoudige while-lus die aftelt."""
    count = 3
    while count > 0:
        print(f"Countdown: {count}")
        count -= 1


def nested_loop_example():
    """Geneste loops om coordinaten te genereren."""
    for x in range(2):
        for y in range(2):
            print(f"({x}, {y})")


def multiplication_table():
    """Print een kleine vermenigvuldigings-tabel."""
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i * j}")
        print("-")


if __name__ == "__main__":
    # Voorbeelden worden uitgevoerd als dit bestand direct wordt gestart
    for_range_example()
    for_list_example()
    while_example()
    nested_loop_example()
    multiplication_table()
