import sys
from typing import List

sys.path.append("apps")

from domains.models.input_text import InputText
from domains.models.morphological_analyser import MorphologicalAnalyser
from domains.models.morphological_token import MorphologicalToken
from singleton import Singleton


class MorphologicalAnalyseService(Singleton):

    morphological_analyser = MorphologicalAnalyser()

    @classmethod
    def get_morphological_analysed_token(cls, text: InputText) -> List[MorphologicalToken]:
        """形態素解析を行う

        Args:
            text (InputText): 対象テキスト

        Returns:
            List[MorphologicalToken]: 形態素解析結果
        """
        resutls: List[MorphologicalToken] = cls.morphological_analyser.ja_morphological_analyse(text.target_text)
        return resutls
