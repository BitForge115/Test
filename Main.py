from file_handling import file_demo
from loops import multiplication_table
from datastructures import list_and_dict_demo


def main_menu():
    """Eenvoudig menu om voorbeelden te tonen."""
    while True:
        print("\nKies een optie:")
        print("1. File handling voorbeeld")
        print("2. Loops en functies voorbeeld")
        print("3. Datastructuren voorbeeld")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ").strip()
        if keuze == "1":
            file_demo()
        elif keuze == "2":
            multiplication_table()
        elif keuze == "3":
            list_and_dict_demo()
        elif keuze == "4":
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")


if __name__ == "__main__":
    main_menu()
