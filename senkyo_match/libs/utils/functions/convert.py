def question_size_to_answer_type_converter(question_size: int) -> str:
    if question_size == 8:
        return "flash"
    elif question_size == 18:
        return "advance"
    else:
        return "error"
