# Este projeto é um Sudoku Solver (Resolvedor de Sudoku)
# Inicio: 01/12/22
# Graziela Maria

# Imports
import math
import tkinter
from tkinter import filedialog
import pygame as pg

# Selecionando um arquivo que representa um sudoko de dentro sistema do usuário



def abrir_arquivo_do_sistema():
    tk_screen = tkinter.Tk()
    tk_screen.withdraw() # esconde a janela do tkinter
    arquivo = filedialog.askopenfilename()
    tk_screen.destroy()
    return arquivo


# Abrindo arquivo que possue o sudoku escrito
def abrindo_arquivo():
    arquivo_sudoku = open(abrir_arquivo_do_sistema()) #abre arquivo selecionado
    sudoku = []
    for a in arquivo_sudoku:
        lista = []
        for j in a:
            if j != '\n' and j != '[' and j != ']' and j != ',' and j != ' ':
                lista.append(int(j))

        sudoku.append(lista)
    print(sudoku)
    return sudoku


# retorna o sudoku resolvido
def criar_arquivo_resposta(sudoku):
    resposta = open('../../resposta.txt', 'w')
    for i in sudoku:
        resposta.write(str(i))
        resposta.write('\n')


# cores utilizados
cinza_escuro = (40, 49, 64, 25)
azul_selecionado = (119, 146, 191, 75)
azul_brilhante = (158, 195, 255, 100)

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

def tabuleiro_hover(window, mouse_position_x, mouse_position_y):
    quadrado = 50
    ajuste = 30
    x = math.ceil((mouse_position_x-ajuste)/quadrado)-1
    y = math.ceil((mouse_position_y-ajuste)/quadrado)-1
    pg.draw.rect(window, cinza_escuro, (0, 0, 800, 700))
    if 0 <= x <= 8 and 0 <= y <= 8:
        pg.draw.rect(window, azul_brilhante, (ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado))
        print(ajuste + x * quadrado)

def quadrado_selecionado(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    quadrado = 50
    ajuste = 30
    if click_last_status == True and click == True:
        x = math.ceil((mouse_position_x - ajuste) / quadrado) - 1
        y = math.ceil((mouse_position_y - ajuste) / quadrado) - 1
    if 0 <= x <= 8 and 0 <= y <= 8:
        pg.draw.rect(window, azul_selecionado, (ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado))
    return x, y


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                sudoku = abrindo_arquivo()
                for i in sudoku:
                    print(i)
        elif event.type == pg.KEYDOWN:
            numero = pg.key.name(event.key)


    #mouse
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # declarando variavel do mouse
    click = pg.mouse.get_pressed()
    print(click)

    #Game
    tabuleiro_hover(window, mouse_position_x, mouse_position_y)
    click_position_x, click_position_y = quadrado_selecionado(window, mouse_position_x, mouse_position_y, click_last_status, click[0], click_position_x, click_position_y)

    # click_last_status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.flip()

pg.quit()
