from libs.utils.calc.calc_score import calcurate_score
from utils.functions.convert import question_size_to_answer_type_converter
from utils.functions.extract import extract_answer_value_list
from utils.os.read_json import read_json


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
