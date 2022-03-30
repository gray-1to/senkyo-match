from libs.utils.calc.calc_score import calcurate_score
from libs.utils.functions.convert import question_size_to_answer_type_converter
from libs.utils.functions.extract import extract_answer_value_list
from libs.utils.os.read_json import read_json


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
        politician_match_score[politician_name] = calcurate_score(user_answer_value_list, politician_answer_value_list)

    return dict(sorted(politician_match_score.items(), key=lambda x: x[1], reverse=True))
