# Este projeto é um Sudoku Solver (Resolvedor de Sudoku)
# Inicio: 01/12/22
# Graziela Maria

# IMPORTS
# > Bibliotecas
import sys
import pygame as pg

# > modulos internos
import constants as const
from src.components import button
from src.game_screens import end_game
from src.game_screens import ranking
from src.game_screens import sudoku


# inicializando tela principal
pg.init()
window = pg.display.set_mode(const.DISPLAY_SIZE)

# inicializando fontes
pg.font.init()
font = pg.font.SysFont(const.FONT['name'], const.FONT['size'])


def menu(window):
    pg.display.set_caption('Menu')
    while True:

        window.fill(const.CORES['background_color'])

        # Posicao do mouse
        mouse = pg.mouse.get_pos()
        font_menu_title = pg.font.SysFont('arial', 70)
        MENU_TEXT = font_menu_title.render('SUDOKU', True, const.CORES['roxo_claro'])
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        copyright_title = pg.font.SysFont('arial', 20)
        COPYRIGHT_TEXT = copyright_title.render('Copyright © 2022 Graziela Felix', True, const.CORES['roxo_claro'])
        COPYRIGHT_RECT = MENU_TEXT.get_rect(center=(400, 600))

        PLAY_BUTTON = button.ButtonMenu('PLAY', 260, 210, const.CORES['roxo_claro'], font, window, 200, 200, 700, 80, 3,
                                        const.CORES['roxo_claro'], const.CORES['roxo_escuro'])

        RANKING_BUTTON = button.ButtonMenu('RANKING', 260, 310, const.CORES['roxo_claro'], font, window, 200, 300, 700, 80, 3,
                                        const.CORES['roxo_claro'], const.CORES['roxo_escuro'])
        EXIT_BUTTON = button.ButtonMenu('SAIR', 260, 410, const.CORES['roxo_claro'], font, window, 200, 400, 700, 80, 3, const.CORES['roxo_claro'], const.CORES['roxo_escuro'])

        window.blit(MENU_TEXT, MENU_RECT)
        window.blit(COPYRIGHT_TEXT, COPYRIGHT_RECT)

        for button_menu in [PLAY_BUTTON, RANKING_BUTTON, EXIT_BUTTON]:
            button_menu.update()
            button_menu.hover(mouse)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_click(mouse):
                    sudoku.play(pg, window, const, font, menu, ranking, end_game)
                if RANKING_BUTTON.check_click(mouse):
                    ranking.ranking(pg, window, const, font, menu)
                if EXIT_BUTTON.check_click(mouse):
                    pg.quit()
                    sys.exit()

        pg.display.update()


menu(window)
