import sys

from ..components import button

def diffcult_level(pg, window, font, const, sudoku, menu, ranking, end_game):
    pg.display.set_caption('Dificuldade')

    while True:

        window.fill(const.CORES['background_color'])

        # Posicao do mouse
        mouse = pg.mouse.get_pos()
        font_menu_title = pg.font.SysFont('arial', 70)
        MENU_TEXT = font_menu_title.render('ESCOLHA A DIFICULDADE:', True, const.CORES['roxo_claro'])
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        copyright_title = pg.font.SysFont('arial', 20)
        COPYRIGHT_TEXT = copyright_title.render('Copyright © 2022 Graziela Felix', True, const.CORES['roxo_claro'])
        COPYRIGHT_RECT = MENU_TEXT.get_rect(center=(600, 600))

        EASY_BUTTON = button.ButtonMenu('Fácil', 260, 210, const.CORES['roxo_claro'], font, window, 200, 200, 700, 80, 3,
                                        const.CORES['roxo_claro'], const.CORES['roxo_escuro'])

        MEDIUM_BUTTON = button.ButtonMenu('Médio', 260, 310, const.CORES['roxo_claro'], font, window, 200, 300, 700,
                                           80, 3,
                                           const.CORES['roxo_claro'], const.CORES['roxo_escuro'])
        HARD_BUTTON = button.ButtonMenu('Difícil', 260, 410, const.CORES['roxo_claro'], font, window, 200, 400, 700, 80, 3,
                                        const.CORES['roxo_claro'], const.CORES['roxo_escuro'])

        window.blit(MENU_TEXT, MENU_RECT)
        window.blit(COPYRIGHT_TEXT, COPYRIGHT_RECT)

        for button_menu in [EASY_BUTTON, MEDIUM_BUTTON, HARD_BUTTON]:
            button_menu.update()
            button_menu.hover(mouse)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if EASY_BUTTON.check_click(mouse):
                    dificuldade = 69
                    sudoku.play(pg, window, const, font, menu, ranking, end_game, dificuldade)
                if MEDIUM_BUTTON.check_click(mouse):
                    dificuldade = 54
                    sudoku.play(pg, window, const, font, menu, ranking, end_game, dificuldade)
                if HARD_BUTTON.check_click(mouse):
                    dificuldade = 27
                    sudoku.play(pg, window, const, font, menu, ranking, end_game, dificuldade)

        pg.display.update()