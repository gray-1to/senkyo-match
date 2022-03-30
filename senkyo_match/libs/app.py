import json


def read_json(json_file_path: str) -> list[dict]:
    with open(json_file_path, "r") as f:
        return json.load(f)


def write_json(json_file_path: str, data: dict) -> None:
    with open(json_file_path, "w") as f:
        json.dump(data, f, indent=4)


def question_size_to_answer_type_converter(question_size: int) -> str:
    if question_size == 8:
        return "flash"
    elif question_size == 18:
        return "advance"
    else:
        return "error"


def calcurate_politician_match_score(user_answer: list[dict], area_code: int) -> dict[str, int]:
    """
    マッチング結果が大きい順にした辞書型で返す
    """
    # area_code は、user の選挙区の政治家データを取得する際に用いる
    politician_name_list: list[str] = []  # 本来は、DBなどを叩いてきた返値
    user_answer_value_list: list[int] = extract_answer_value_list(user_answer, "user_answer_value")

    politician_match_score: dict[str, int] = {}
    for politician_name in politician_name_list:
        politician_answer_data: list[dict] = read_json(
            f"senkyo_match/data/{question_size_to_answer_type_converter(len(user_answer))}/politician/{politician_name}.json"
        )
        politician_answer_value_list: list[int] = extract_answer_value_list(
            politician_answer_data, "politician_answer_value"
        )
        politician_match_score[politician_name] = calcurate_score(
            user_answer_value_list, politician_answer_value_list
        )
    
    return dict(sorted(politician_match_score.items(), key=lambda x: x[1], reverse=True))


def calcurate_party_match_score(user_answer: list[dict]) -> dict[str, int]:
    """
    マッチング結果が大きい順にした辞書型で返す
    """
    user_answer_value_list: list[int] = extract_answer_value_list(user_answer, "user_answer_value")
    PARTY_LIST: list[str] = ["ldp", "komei"]

    party_match_score: dict[str, int] = {}
    for party in PARTY_LIST:

        party_answer_data: list[dict] = read_json(
            f"senkyo_match/data/{question_size_to_answer_type_converter(len(user_answer_value_list))}/party/{party}.json"
        )
        party_answer_value_list: list[int] = extract_answer_value_list(party_answer_data, "party_answer_value")

        party_match_score[party] = calcurate_score(user_answer_value_list, party_answer_value_list)

    return dict(sorted(party_match_score.items(), key=lambda x: x[1], reverse=True))


def calcurate_score(user_answer_value_list: list[int], party_answer_value_list: list[int]) -> int:
    pass

def calcurate_distance():
    pass

def extract_answer_value_list(user_answer: list[dict], extract_key: str) -> list[int]:
    """
    user_answer: list[dict], party_answer: list[dict] から answer_value のみを抽出する。
    """
    answer_value_list: list[int] = []
    for user_answer_data in user_answer:
        answer_value_list.append(user_answer_data[extract_key])
    return answer_value_list


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
