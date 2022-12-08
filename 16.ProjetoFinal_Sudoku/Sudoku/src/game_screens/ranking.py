import sys
from ..components import button
from ..user_data import controller_user_data

# Lendo data
controller_user_data.read_user_data()


def ranking(pg, window, const, font, menu, user_data=None):
    # Atualizando arquivo json com os novos dados
    # produzidos pelo usuario ao finalizar o jogo
    if user_data != None:
        controller_user_data.update_user_data(user_data)
        controller_user_data.read_user_data()

    # titulo da tela
    pg.display.set_caption('Ranking')
    titulos_font = pg.font.SysFont('arial', 30)

    def tabela(window):
        # linhas horizontais
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 180, 660, 350), 3)
        pg.draw.rect(window, const.CORES['roxo_claro'], (400, 180, 200, 350), 3)
        # linhas verticais
        #titulo tabelas
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 180, 660, 50), 3)
        #linha dados
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 230, 660, 50), 2)
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 280, 660, 50), 2)
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 330, 660, 50), 2)
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 380, 660, 50), 2)
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 430, 660, 50), 2)
        pg.draw.rect(window, const.CORES['roxo_claro'], (70, 480, 660, 50), 2)

    def titulos_tabela():
        nome_titulo = titulos_font.render('Nome do Jogador', True, const.CORES['roxo_claro'])
        titulo_rect = nome_titulo.get_rect(center=(230, 200))
        window.blit(nome_titulo, titulo_rect)

        data_titulo = titulos_font.render('Data', True, const.CORES['roxo_claro'])
        data_rect = data_titulo.get_rect(center=(500, 200))
        window.blit(data_titulo, data_rect)

        tempo_titulo = titulos_font.render('Tempo', True, const.CORES['roxo_claro'])
        tempo_rect = tempo_titulo.get_rect(center=(655, 200))
        window.blit(tempo_titulo, tempo_rect)

    def mostrando_dados():
        ranking_data = controller_user_data.return_data()

        cont_nome_padding = 0
        cont_data_padding = 0
        cont_tempo_padding = 0
        for i in range(len(ranking_data)):
            nome = titulos_font.render(ranking_data[i].nome, True, const.CORES['roxo_claro'])
            window.blit(nome, (140, 235 + cont_nome_padding))

            data = titulos_font.render(ranking_data[i].data, True, const.CORES['roxo_claro'])
            window.blit(data, (440, 235 + cont_data_padding))

            tempo = titulos_font.render(ranking_data[i].tempo, True, const.CORES['roxo_claro'])
            window.blit(tempo, (640, 235 + cont_tempo_padding))

            cont_nome_padding += 50
            cont_data_padding += 50
            cont_tempo_padding += 50

    while True:

        window.fill(const.CORES['background_color'])

        # Nome Ranking
        font_ranking = pg.font.SysFont('arial', 70)
        ranking_text = font_ranking.render('RANKING', True, const.CORES['roxo_claro'])
        text_rect = ranking_text.get_rect(center=(200, 80))
        window.blit(ranking_text, text_rect)

        # Botão voltar
        VOLTAR_BUTTON = button.ButtonMenu('Voltar', 540, 50, const.CORES['roxo_claro'], font, window, 520, 40, 300,
                                          80, 3, const.CORES['roxo_claro'], const.CORES['roxo_escuro'])
        VOLTAR_BUTTON.update()
        VOLTAR_BUTTON.hover(pg.mouse.get_pos())

        # RANKING
        tabela(window)
        titulos_tabela()
        mostrando_dados()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if VOLTAR_BUTTON.check_click(pg.mouse.get_pos()):
                    menu(window)

        pg.display.update()
