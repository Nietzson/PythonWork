from sys import exit

people = {
    "MALLIA": "06 00 00 00 00",
    "YOANN": "06 19 45 19 44",
    "PEPE": "02 98 82 90 94",
}

if "MALLIA" in people:
    print(f"Found {people['MALLIA']}")
    exit(0)