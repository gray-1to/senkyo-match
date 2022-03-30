def extract_answer_value_list(user_answer: list[dict], extract_key: str) -> list[int]:
    """
    user_answer: list[dict], party_answer: list[dict] から answer_value のみを抽出する。
    """
    answer_value_list: list[int] = []
    for user_answer_data in user_answer:
        answer_value_list.append(user_answer_data[extract_key])
    return answer_value_list
