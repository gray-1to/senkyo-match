import json


def read_json(json_file_path: str) -> dict:
    with open(json_file_path, "r") as f:
        return json.load(f)
