import json


def write_json(json_file_path: str, data: dict) -> None:
    with open(json_file_path, "w") as f:
        json.dump(data, f, indent=4)
