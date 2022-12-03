# Este projeto é um Sudoku Solver (Resolvedor de Sudoku)
# Inicio: 01/12/22
# Graziela Maria

# Imports
import math
import pygame as pg
from controller import controller_gerenciador_de_arquivos

# Cores utilizadas
background_color = (14, 17, 23, 17)
roxo_escuro = (73, 88, 173, 68)
roxo_claro = (105, 127, 250, 98)

# inicializando tela principal
pg.init()
window = pg.display.set_mode((800, 700))

# inicializando fontes
pg.font.init()
font = pg.font.SysFont('arial', 50, italic=True)

# variaveis utilizadas
click_last_status = False
click_position_x = -1
click_position_y = -1
numero = 0

# Desenho das linhas do tabuleiro
# A linha 1: Desenha o perimetro do quadrado maior
# linhas 2 e 3: desenham dois quadrados que representam as linhas verticais
# linhas 4 e 4: desenham dois quadrados que representam as linhas horizontais
def tabuleiro_sudoku(window):
    pg.draw.rect(window, roxo_claro, (30, 30, 450, 450), 6)
    pg.draw.rect(window, roxo_claro, (180, 30, 150, 450), 6)
    pg.draw.rect(window, roxo_claro, (30, 180, 450, 150), 6)
    pg.draw.rect(window, roxo_claro, (80, 30, 50, 450), 2)
    pg.draw.rect(window, roxo_claro, (230, 30, 50, 450), 2)
    pg.draw.rect(window, roxo_claro, (380, 30, 50, 450), 2)
    pg.draw.rect(window, roxo_claro, (30, 80, 450, 50), 2)
    pg.draw.rect(window, roxo_claro, (30, 230, 450, 50), 2)
    pg.draw.rect(window, roxo_claro, (30, 380, 450, 50), 2)


def tabuleiro_hover(window, mouse_position_x, mouse_position_y):
    quadrado = 50
    ajuste = 30
    x = math.ceil((mouse_position_x-ajuste)/quadrado)-1
    y = math.ceil((mouse_position_y-ajuste)/quadrado)-1
    pg.draw.rect(window, background_color, (0, 0, 800, 700))
    if 0 <= x <= 8 and 0 <= y <= 8:
        pg.draw.rect(window, roxo_claro, (ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado))


def quadrado_selecionado(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    quadrado = 50
    ajuste = 30
    if click_last_status == True and click == True:
        x = math.ceil((mouse_position_x - ajuste) / quadrado) - 1
        y = math.ceil((mouse_position_y - ajuste) / quadrado) - 1
    if 0 <= x <= 8 and 0 <= y <= 8:
        pg.draw.rect(window, roxo_escuro, (ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado))
    return x, y


def restart_button(window):
    pg.draw.rect(window, roxo_claro, (520, 40, 200, 80))
    word = font.render('Reniciar', True, background_color)
    window.blit(word, (525, 50))


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                sudoku = controller_gerenciador_de_arquivos.abrindo_arquivo()
                for i in sudoku:
                    print(i)
                controller_gerenciador_de_arquivos.criar_arquivo_resposta(sudoku)
        elif event.type == pg.KEYDOWN:
            numero = pg.key.name(event.key)


    #mouse
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # declarando variavel do mouse
    click = pg.mouse.get_pressed()

    # Game
    tabuleiro_hover(window, mouse_position_x, mouse_position_y)
    click_position_x, click_position_y = quadrado_selecionado(window, mouse_position_x, mouse_position_y, click_last_status, click[0], click_position_x, click_position_y)
    tabuleiro_sudoku(window)
    restart_button(window)

    # click_last_status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.draw.rect(window, roxo_claro, pg.Rect(30, 510, 100, 50), 2)
    pg.display.flip()

pg.quit()
