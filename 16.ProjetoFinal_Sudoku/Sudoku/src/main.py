# Este projeto é um Sudoku Solver (Resolvedor de Sudoku)
# Inicio: 01/12/22
# Graziela Maria

# Imports
import math
import pygame as pg
from controller import controller_gerenciador_de_arquivos

# inicializando tela principal
pg.init()
window = pg.display.set_mode((800, 600))
pg.display.set_caption('Sudoku', 'Sudoku')

# inicializando fontes
pg.font.init()
font = pg.font.SysFont('arial', 45)

# Cores utilizadas
background_color = (14, 17, 23, 17)
roxo_escuro = (73, 88, 173, 68)
roxo_claro = (105, 127, 250, 98)

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


class Button:
    def __init__(self, text_input, font_position_x, font_position_y, font_color, left, top, width, height,  fill):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.font_color = font_color
        self.text_input = text_input
        self.font_position_x = font_position_x
        self.font_position_y = font_position_y
        self.fill = fill
        self.text = font.render(self.text_input, True, self.font_color)
        self.pressed = False

    def update(self):
        pg.draw.rect(window, roxo_escuro, (self.left + 5, self.top + 5, self.width, self.height), self.fill)
        pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
        window.blit(self.text, (self.font_position_x, self.font_position_y))

    def hover(self, position):
        if position[0] in range(self.left, (self.left+self.width)) and position[1] in range(self.top, (self.top+self.height)):
            pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height))
            self.text = font.render(self.text_input, True, background_color)
            window.blit(self.text, (self.font_position_x, self.font_position_y))

        else:
            pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
            self.text = font.render(self.text_input, True, self.font_color)

    def check_click(self, position, function):
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top,(self.top + self.height)):
            if pg.mouse.get_pressed()[0]:
                pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                self.pressed = True
            else:
                if self.pressed:
                    pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                    function()
                    self.pressed = False

# Botões
button_restart = Button('Reniciar', 540, 50, roxo_claro, 520, 40, 300, 80, 3)
button_add_file = Button('Adicionar', 535, 150, roxo_claro, 520, 140, 300, 80, 3)
button_solve = Button('Resolver', 535, 250, roxo_claro, 520, 240, 300, 80, 3)

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
    button_restart.update()
    button_restart.hover(mouse)
    button_add_file.update()
    button_add_file.hover(mouse)
    button_add_file.check_click(mouse, controller_gerenciador_de_arquivos.abrindo_arquivo)
    button_solve.update()
    button_solve.hover(mouse)

    # click_last_status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.flip()

pg.quit()
