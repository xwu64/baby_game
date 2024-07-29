import pygame
from exit import ExitType, ExitUnit


def up_down_select(win, items, width, height, normal_color, select_color) -> ExitUnit:
    menu_font = pygame.font.SysFont(None, 100)
    cur_pos = 0

    while True:
        win.fill((255, 255, 255))

        for i, item in enumerate(items):
            color = normal_color if i != cur_pos else select_color
            text = menu_font.render(str(item), True, color)
            dest_w = width // 2 - text.get_width() // 2
            dest_h = height // 2 - 100 + i * 150
            win.blit(text, (dest_w, dest_h))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return ExitUnit(ExitType.QUIT, None)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cur_pos = (cur_pos - 1) % len(items)
                elif event.key == pygame.K_DOWN:
                    cur_pos = (cur_pos + 1) % len(items)
                elif event.key == pygame.K_RETURN:
                    return ExitUnit(ExitType.NORMAL, items[cur_pos])