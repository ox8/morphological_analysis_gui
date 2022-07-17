from typing import List, Optional, Tuple

import PySimpleGUI as sg
from config import FONT_LARGE, FONT_MEDIUM, FONT_NAME, FONT_SMALL
from domains.models.input_text import InputText
from domains.models.morphological_token import MorphologicalToken
from services.morphological_analyse import MorphologicalAnalyseService
from services.py_simple_gui import PySimpleGUIService


def get_validation_message(text: str) -> Optional[Tuple[str, str]]:
    if len(text) == 0:
        return ("入力値エラー", "テキストを入力してください。")
    return None


if __name__ == "__main__":
    sg.theme("Dark Blue")
    morphological_analyse = MorphologicalAnalyseService()

    layout = [
        [sg.Text("Python 形態素解析", font=FONT_LARGE)],
        [
            sg.Frame(
                "オプション",
                font=FONT_MEDIUM,
                layout=[
                    [sg.Checkbox("数字を正規化", font=FONT_MEDIUM, key="is_normalize_number")],
                    [sg.Checkbox("半角化", font=FONT_MEDIUM, key="is_normalize_half_size")],
                    [sg.Checkbox("改行・スペース削除", font=FONT_MEDIUM, key="is_delete_space")],
                    [sg.Checkbox("ストップワード削除", font=FONT_MEDIUM, key="is_delete_stop_words")],
                ],
            )
        ],
        [
            sg.Text("解析したいテキストを入力してください。", font=FONT_MEDIUM),
            sg.Submit(button_text="結果を見る", auto_size_button=True, font=FONT_NAME, key="exec"),
        ],
        [sg.Multiline("", size=(1800, 200), font=FONT_LARGE, key="input_text")],
    ]

    window = sg.Window("", layout, resizable=True, size=(1200, 600))

    while True:
        event, values = window.read()

        if event is None:
            print("exit")
            break

        validation_message: Optional[Tuple[str, str]] = get_validation_message(text=values["input_text"])
        if validation_message:
            PySimpleGUIService.popup_message_dialog(title=validation_message[0], message=validation_message[1])
            continue

        input_text: InputText = InputText(
            text=values["input_text"],
            is_normalize_number=values["is_normalize_number"],
            is_normalize_half_size=values["is_normalize_half_size"],
            is_delete_space=values["is_delete_space"],
            is_delete_stop_words=values["is_delete_stop_words"],
        )

        if event == "exec":
            results: List[MorphologicalToken] = morphological_analyse.get_morphological_analysed_token(text=input_text)
            show_message: str = "\n".join(
                [f"{result.token.surface} {result.token.part_of_speech}" for result in results]
            )
            PySimpleGUIService.popup_message_dialog(message=show_message)

    window.close()
