import PySimpleGUI as sg
from config import FONT_LARGE, FONT_MEDIUM, FONT_NAME, FONT_SMALL

if __name__ == "__main__":
    sg.theme("Dark Blue")

    layout = [
        [
            sg.Text("Python 形態素解析", font=FONT_LARGE),
            sg.Submit(button_text="結果を見る", auto_size_button=True, font=FONT_NAME, key="exec"),
        ],
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
        [sg.Text("解析したいテキストを入力してください。", font=FONT_MEDIUM)],
        [sg.Multiline("", size=(1800, 200), font=FONT_LARGE, key="input_text")],
    ]

    window = sg.Window("", layout, resizable=True, size=(1200, 600))

    while True:
        event, values = window.read()

        if event is None:
            print("exit")
            break

        if event == "exec":
            show_message = "テキスト:" + values["input_text"] + "が入力されました。"
            print(show_message)
            sg.popup(show_message)

    window.close()
