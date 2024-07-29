import pygame
import string
from constants import Levels
from up_down_select import up_down_select
from exit import ExitType, ExitUnit
from menu_item import MenuItem


class LevelSetting():
    def __init__(self, dictionary) -> None:
        self.dictionary = dictionary


def select_level(win, width, height) -> ExitUnit:
    all_level = [Levels.LEVEL0, Levels.LEVEL1, Levels.LEVEL2]
    level_items = [MenuItem(level, f"Level {i}") for i, level in enumerate(all_level)]
    normal_color = (0,0,0)
    selected_color = (0, 0, 255)
    ret_msg = up_down_select(win, level_items, width, height, normal_color, selected_color)

    if ret_msg.exit_type == ExitType.QUIT:
        return ret_msg
    elif ret_msg.exit_type == ExitType.NORMAL:
        if ret_msg.rtn_msg.type == Levels.LEVEL0:
            return ExitUnit(ExitType.NORMAL, LevelSetting(list(string.digits)))
        if ret_msg.rtn_msg.type == Levels.LEVEL1:
            return ExitUnit(ExitType.NORMAL, LevelSetting(list(string.ascii_uppercase)))
        if ret_msg.rtn_msg.type == Levels.LEVEL2:
            return ExitUnit(ExitType.NORMAL, LevelSetting(list(string.digits)+list(string.ascii_uppercase)))