import re
import sys

from pydantic import BaseModel

sys.path.append("apps")
from domains.types.stop_words import STOP_WORDS
from utils.word import zen_to_han


class InputText(BaseModel):
    text: str
    is_normalize_number: bool
    is_normalize_half_size: bool
    is_delete_space: bool
    is_delete_stop_words: bool

    class Config:
        allow_mutation = False

    @property
    def target_text(self) -> str:
        result: str = self.text
        if self.is_normalize_number:
            result = re.sub(r"\d+", "0", result)
        if self.is_normalize_half_size:
            result = zen_to_han(text=result)
        if self.is_delete_space:
            result = result.strip()
        if self.is_delete_stop_words:
            for sw in STOP_WORDS:
                result = result.replace(sw, "")
        return result
