import json
from sys import argv


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    script, filepath = argv
    json_loaded_data = load_data(filepath)
    pretty_print_json(json_loaded_data)
