import sys
from ..components import button
from ..user_data import controller_user_data

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
                letra = pg.key.name(event.key)
                if len(user_name) < 8:
                    if event.key == pg.K_SPACE:
                        letra = ' '
                        letra = mostrar_digitos(letra)
                        user_name = user_name + letra
                    elif event.key == pg.K_BACKSPACE:
                        user_name = user_name[0:len(user_name)-1]
                    elif event.key == pg.K_RETURN:
                        pass
                    else:
                        letra = mostrar_digitos(letra)
                        user_name = user_name + letra
                else:
                    if event.key == pg.K_BACKSPACE:
                        user_name = user_name[0:len(user_name)-1]
            elif event.type == pg.MOUSEBUTTONDOWN:
                if BUTTON_OK.check_click(pg.mouse.get_pos()):
                    # Atualizando arquivo json com os novos dados
                    # produzidos pelo usuario ao finalizar o jogo
                    user_data['nome'] = user_name
                    controller_user_data.update_user_data(user_data)
                    controller_user_data.append_new_data_in_list(user_data)
                    ranking.ranking(pg, window, const, font, menu)

        window.fill(const.CORES['background_color'])
        input_name()

        # Titulo
        font_ranking = pg.font.SysFont('arial', 50)
        congratulations_text = font_ranking.render('PARABÉNS! VOCÊ CONSEGUIU!', True, const.CORES['roxo_claro'])
        congratulations_rect = congratulations_text.get_rect(center=(400, 100))
        window.blit(congratulations_text, congratulations_rect)

        ranking_text = font_ranking.render('Insira seu nome abaixo:', True, const.CORES['roxo_claro'])
        text_rect = ranking_text.get_rect(center=(400, 200))
        window.blit(ranking_text, text_rect)

        # Botão Ok
        BUTTON_OK.update()
        BUTTON_OK.hover(pg.mouse.get_pos())

        # Digitar nome
        digitando(user_name)

        pg.display.update()
