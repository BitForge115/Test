"""Voorbeelden van verschillende manieren om met bestanden te werken."""


def write_example(bestand, tekst):
    """Schrijf een tekst naar een nieuw bestand."""
    with open(bestand, "w", encoding="utf-8") as f:
        f.write(tekst)


def append_example(bestand, tekst):
    """Voeg tekst toe aan een bestaand bestand."""
    with open(bestand, "a", encoding="utf-8") as f:
        f.write(tekst)


def read_example(bestand):
    """Lees de volledige inhoud van een bestand en geef dit terug."""
    with open(bestand, "r", encoding="utf-8") as f:
        return f.read()


def read_lines_example(bestand):
    """Lees een bestand regel voor regel en print de regels."""
    with open(bestand, "r", encoding="utf-8") as f:
        for regel in f:
            print(regel.strip())


def file_demo():
    """Demonstratie van schrijven, aanvullen en lezen."""
    naam = "voorbeeld.txt"
    write_example(naam, "Eerste regel\n")
    append_example(naam, "Tweede regel\n")

    print("Volledige inhoud:")
    print(read_example(naam))

    print("Regel voor regel lezen:")
    read_lines_example(naam)


if __name__ == "__main__":
    file_demo()
