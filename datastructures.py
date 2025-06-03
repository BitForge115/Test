def list_and_dict_demo():
    """Toont eenvoudige bewerkingen met lijsten en dictionaries."""
    cijfers = [7, 8, 9]
    cijfers.append(10)
    print("Lijst:", cijfers)
    for idx, waarde in enumerate(cijfers, start=1):
        print(f"{idx}: {waarde}")

    leerling = {"naam": "Alex", "leeftijd": 20, "opleiding": "ICT"}
    print("Gegevens van leerling:")
    for sleutel, waarde in leerling.items():
        print(f"{sleutel}: {waarde}")


if __name__ == "__main__":
    list_and_dict_demo()
