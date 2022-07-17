import sys

import PySimpleGUI as sg

sys.path.append("apps")
from config import FONT_LARGE
from singleton import Singleton


class PySimpleGUIService(Singleton):
    @staticmethod
    def popup_message_dialog(title: str = "", message: str = "") -> None:
        sg.popup(message, title=title, font=FONT_LARGE)
