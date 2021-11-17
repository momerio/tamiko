import sys
import time

mode = ""
color = ""
debug = False

name = ""


class Color:
    BLACK = '\033[30m'  # (文字)黒
    RED = '\033[31m'  # (文字)赤
    GREEN = '\033[32m'  # (文字)緑
    YELLOW = '\033[33m'  # (文字)黄
    BLUE = '\033[34m'  # (文字)青
    MAGENTA = '\033[35m'  # (文字)マゼンタ
    CYAN = '\033[36m'  # (文字)シアン
    WHITE = '\033[37m'  # (文字)白
    PINK = "\033[38;2;247;48;164m"
    COLOR_DEFAULT = '\033[39m'  # 文字色をデフォルトに戻す

    BOLD = '\033[1m'  # 太字
    UNDERLINE = '\033[4m'  # 下線
    INVISIBLE = '\033[08m'  # 不可視
    REVERCE = '\033[07m'  # 文字色と背景色を反転
    BG_BLACK = '\033[40m'  # (背景)黒
    BG_RED = '\033[41m'  # (背景)赤
    BG_GREEN = '\033[42m'  # (背景)緑
    BG_YELLOW = '\033[43m'  # (背景)黄
    BG_BLUE = '\033[44m'  # (背景)青
    BG_MAGENTA = '\033[45m'  # (背景)マゼンタ
    BG_CYAN = '\033[46m'  # (背景)シアン
    BG_WHITE = '\033[47m'  # (背景)白
    BG_DEFAULT = '\033[49m'  # 背景色をデフォルトに戻す
    RESET = '\033[0m'  # 全てリセット

    def get_font_color(self, color):
        if color == "black":
            return self.BLACK
        elif color == "red":
            return self.RED
        elif color == "green":
            return self.GREEN
        elif color == "yellow":
            return self.YELLOW
        elif color == "blue":
            return self.BLUE
        elif color == "magenta":
            return self.MAGENTA
        elif color == "cyan":
            return self.CYAN
        elif color == "white":
            return self.WHITE
        elif color == "default":
            return self.COLOR_DEFAULT
        else:
            return color


color_default = Color.COLOR_DEFAULT


def set_display_name(isSet=False):
    global name
    if isSet == True:
        name = "タミ子ちゃん: "


def set_font_color(color_name):
    global color
    color = color_name


def display(text, start, end):
    text = f"{color}{name}{start}{text}{end}{color_default}"
    print(text)


def start_program(start="", end=""):
    text = "プログラムがはじまりましたよぉ！"
    display(text, start, end)


def finish_program(start="", end=""):
    text = "おつかれさまでしたぁ～ プログラムがすべて完了しましたよぉっ！"
    display(text, start, end)


def start_process(process_name="", start="", end=""):
    if process_name == "":
        process_name = "処理"
    text = f"{process_name} がはじまりましたよぉ！"
    display(text, start, end)


def end_process(process_name="", start="", end=""):
    if process_name == "":
        process_name = "処理"
    text = f"{process_name} がおわったみたいですっ！"
    display(text, start, end)


def cheer():
    tamiko = "✧＼\ ٩( 'ω' )و /／✧"
    sys.stdout.write(f"\033[2K\033[G{tamiko}")
    sys.stdout.flush()
    print()
