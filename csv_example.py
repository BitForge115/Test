"""Werken met de csv-module."""

import csv


def write_csv(bestand):
    """Schrijf voorbeeldgegevens naar een CSV-bestand."""
    with open(bestand, "w", newline="", encoding="utf-8") as f:
        schrijver = csv.writer(f)
        schrijver.writerow(["naam", "leeftijd"])
        schrijver.writerow(["Bram", 30])
        schrijver.writerow(["Eva", 25])


def read_csv(bestand):
    """Lees een CSV-bestand en print de rijen."""
    with open(bestand, "r", newline="", encoding="utf-8") as f:
        lezer = csv.reader(f)
        for rij in lezer:
            print(rij)


if __name__ == "__main__":
    bestand = "voorbeeld.csv"
    write_csv(bestand)
    read_csv(bestand)
