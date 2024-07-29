import pygame
from constants import MenuButton
from exit import ExitType, ExitUnit
from up_down_select import up_down_select
from menu_item import MenuItem

# Function to display the main menu
def main_menu(win, width, height):
    menu_items = [MenuItem(MenuButton.START, "Start Game"), MenuItem(MenuButton.QUIT, "Quit")]
    normal_color = (0, 0, 0)
    selected_color = (0, 0, 255)
    ret_msg = up_down_select(win, menu_items, width, height, normal_color, selected_color)

    return ret_msg