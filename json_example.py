"""Voorbeeld van JSON-verwerking."""

import json


def json_demo():
    """Schrijft en leest een dict als JSON."""
    data = {"naam": "Sara", "leeftijd": 28}
    # Schrijf JSON naar een string
    json_str = json.dumps(data)
    print("JSON-string:", json_str)

    # Lees JSON terug naar een dict
    opnieuw = json.loads(json_str)
    print("Terug naar dict:", opnieuw)


if __name__ == "__main__":
    json_demo()
