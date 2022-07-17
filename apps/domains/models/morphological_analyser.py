import sys
from typing import List

from janome.analyzer import Analyzer
from janome.charfilter import UnicodeNormalizeCharFilter
from janome.tokenfilter import LowerCaseFilter
from janome.tokenizer import Token, Tokenizer

sys.path.append("apps")

from domains.models.morphological_token import MorphologicalToken
from singleton import Singleton


class MorphologicalAnalyser(Singleton):

    _ja_tokenizer = Tokenizer("apps/tmp/userdic")
    _ja_char_filters = [UnicodeNormalizeCharFilter()]
    _ja_token_filters = [LowerCaseFilter()]
    ja_analyzer = Analyzer(char_filters=_ja_char_filters, tokenizer=_ja_tokenizer, token_filters=_ja_token_filters)

    @classmethod
    def ja_morphological_analyse(cls, text: str) -> List[MorphologicalToken]:
        """日本語の形態素解析を行う

        Args:
            text (str): _description_

        Returns:
            List[MorphologicalToken]: _description_
        """
        token_list: List[Token] = list(cls.ja_analyzer.analyze(text))
        return [MorphologicalToken(token=token) for token in token_list]
