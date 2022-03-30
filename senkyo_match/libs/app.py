from libs.utils.os.read_json import read_json
from libs.utils.os.write_json import write_json


def main():
    user_answer_data: list[dict] = read_json("senkyo_match/io/input/user_answer_advance.json")
    print(type(user_answer_data))
    _answer_data_size: int = len(user_answer_data)
    if _answer_data_size == 8:
        pass
    elif _answer_data_size == 18:
        pass
    else:
        print("Error: user_answer_data size is not 8 or 18.")
        exit(1)


if __name__ == "__main__":
    main()
