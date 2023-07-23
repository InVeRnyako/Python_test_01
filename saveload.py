import json

save_file = "data.json"


def load_data():
    try:
        with open(save_file, "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


def save_data(notes):
    with open(save_file, "w") as file:
        # json.dump(notes, file, indent=4, separators=(' ; ', ' : '))
        json.dump(notes, file, indent=4)
