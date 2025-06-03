"""Voorbeelden van klassen, objecten en overerving."""


class Persoon:
    """Een eenvoudige klasse met een naam."""

    def __init__(self, naam):
        self.naam = naam  # sla de naam op in het object

    def groet(self):
        """Print een groet met de naam."""
        print(f"Hallo, ik ben {self.naam}")


class Student(Persoon):
    """Student erft van Persoon."""

    def __init__(self, naam, opleiding):
        super().__init__(naam)  # roep de constructor van Persoon aan
        self.opleiding = opleiding

    def groet(self):
        """Overschrijf de groet-methode voor extra informatie."""
        super().groet()
        print(f"Ik volg de opleiding {self.opleiding}")


if __name__ == "__main__":
    piet = Persoon("Piet")
    piet.groet()

    anna = Student("Anna", "ICT")
    anna.groet()
