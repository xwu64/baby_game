import pygame
from constants import MenuButton

# Function to display the main menu
def main_menu(win, width, height):
    menu_font = pygame.font.SysFont(None, 100)
    menu_items = ["Start Game", "Quit"]
    selected_item = 0

    while True:
        win.fill((255, 255, 255))

        for i, item in enumerate(menu_items):
            color = (0, 0, 0) if i != selected_item else (0, 0, 255)
            text = menu_font.render(item, True, color)
            win.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 100 + i * 150))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return MenuButton.QUIT
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:
                        return MenuButton.START
                    elif selected_item == 1:
                        pygame.quit()
                        return MenuButton.QUIT