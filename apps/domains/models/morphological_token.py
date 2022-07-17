from janome.tokenizer import Token
from pydantic import BaseModel


class MorphologicalToken(BaseModel):
    """janomeによって形態素解析された結果"""

    token: Token

    class Config:
        allow_mutation = False
        arbitrary_types_allowed = True

    @property
    def part_of_speech(self) -> str:
        return self.token.part_of_speech.split(",")[0]

    def __eq__(self, o: "MorphologicalToken") -> bool:
        if self.token.node == o.token.node:
            return True
        if self.token.extra == o.token.extra:
            return True
        return False
