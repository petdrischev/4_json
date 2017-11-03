import json
from sys import argv


def load_data(filepath):
    try:
        with open(filepath) as f:
            return json.load(f) 
    except (FileNotFoundError, json.decoder.JSONDecodeError):  
        return None


def pretty_print_json(data):
    print (json.dumps(data, indent=4))


if __name__ == '__main__':
    script, from_file = argv
    data = load_data(from_file)
    pretty_print_json(data)
