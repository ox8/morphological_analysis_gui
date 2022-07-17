import mojimoji


def zen_to_han(text: str, is_digit: bool = False) -> str:
    """全角を半角に変換する

    Args:
        text (str): 対象となるテキスト
        is_digit (bool): 数字も半角に変換するか

    Returns:
        str: 変換後のテキスト
    """
    return mojimoji.zen_to_han(text, digit=is_digit, ascii=False)
