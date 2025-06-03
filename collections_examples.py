"""Voorbeelden van verschillende collecties in Python."""


def list_example():
    """Laat zien hoe je met lijsten werkt."""
    boodschappen = ["melk", "brood", "eieren"]  # lijst met drie items
    boodschappen.append("kaas")  # voeg een item toe
    for item in boodschappen:
        print("Item:", item)


def tuple_example():
    """Toont gebruik van een tuple, een onveranderbare lijst."""
    kleuren = ("rood", "groen", "blauw")
    for kleur in kleuren:
        print("Kleur:", kleur)


def set_example():
    """Demonstreert een set die geen dubbele waarden bevat."""
    unieke_getallen = {1, 2, 3, 3}
    print("Set:", unieke_getallen)


def dict_example():
    """Werkt met een dictionary van sleutel/waarde-paren."""
    persoon = {"naam": "Lisa", "leeftijd": 22}
    for sleutel, waarde in persoon.items():
        print(f"{sleutel} -> {waarde}")


if __name__ == "__main__":
    list_example()
    tuple_example()
    set_example()
    dict_example()
