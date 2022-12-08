import sys
from ..components import button


def end_game(pg, window, const, font, menu, ranking, user_data):

    user_name = ''
    pg.display.set_caption('Ranking')
    titulos_font = pg.font.SysFont('arial', 50)

    # botão
    BUTTON_OK = button.ButtonMenu('Ok', 540, 460, const.CORES['roxo_claro'], font, window, 520, 450, 300,
                                  80, 3, const.CORES['roxo_claro'], const.CORES['roxo_escuro'])

    def input_name():
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 250, 660, 100), 2)

    def mostrar_digitos(letra):
        return str(letra)

    def digitando(user_name):
        nome = titulos_font.render(user_name, True, const.CORES['roxo_claro'])
        window.blit(nome, (140, 260))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if len(user_name) < 8:
                    letra = pg.key.name(event.key)
                    letra = mostrar_digitos(letra)
                    user_name = user_name + letra
            elif event.type == pg.MOUSEBUTTONDOWN:
                if BUTTON_OK.check_click(pg.mouse.get_pos()):
                    user_data['nome'] = user_name
                    ranking.ranking(pg, window, const, font, menu, user_data)

        window.fill(const.CORES['background_color'])
        input_name()

        # Titulo
        font_ranking = pg.font.SysFont('arial', 70)
        ranking_text = font_ranking.render('INSIRA SEU NOME:', True, const.CORES['roxo_claro'])
        text_rect = ranking_text.get_rect(center=(400, 100))
        window.blit(ranking_text, text_rect)

        # Botão Ok
        BUTTON_OK.update()
        BUTTON_OK.hover(pg.mouse.get_pos())

        # Digitar nome
        digitando(user_name)

        pg.display.update()
