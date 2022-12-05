# Este projeto é um Sudoku Solver (Resolvedor de Sudoku)
# Inicio: 01/12/22
# Graziela Maria

# Imports
import math
import random
import pygame as pg
from controller import controller_gerenciador_de_arquivos
from abc import ABC, abstractmethod

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
escondendo_numeros = True
tabuleiro_preenchido = True
click_last_status = False
click_position_x = -1
click_position_y = -1
numero = 0

# o tabuleiro que será usado para comparar as respostas com o jogo_data
tabuleiro_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                  ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

# o tabuleiro que aparecerá na interface do jogo, pois possuirá espaços em branco
jogo_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
             ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]

# retorna um tabuleiro vazio
def restart_tabuleiro_data():
    tabuleiro_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    return tabuleiro_data

# Desenha das linhas do tabuleiro
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

# Quando o usuário passa o mouse por cima do quadrado ele fica mais escuro
def tabuleiro_hover(window, mouse_position_x, mouse_position_y):
    quadrado = 50
    ajuste = 30
    x = math.ceil((mouse_position_x-ajuste)/quadrado)-1
    y = math.ceil((mouse_position_y-ajuste)/quadrado)-1
    pg.draw.rect(window, background_color, (0, 0, 800, 700))
    if 0 <= x <= 8 and 0 <= y <= 8:
        pg.draw.rect(window, roxo_claro, (ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado))

# Quando o usuário clica no quadrado ele fica mais escuro
def quadrado_selecionado(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    quadrado = 50
    ajuste = 30
    if click_last_status == True and click == True:
        x = math.ceil((mouse_position_x - ajuste) / quadrado) - 1
        y = math.ceil((mouse_position_y - ajuste) / quadrado) - 1
    if 0 <= x <= 8 and 0 <= y <= 8:
        pg.draw.rect(window, roxo_escuro, (ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado))
    return x, y

# CLASSES BUTÕES
class Button(ABC):
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

    @abstractmethod
    def action(self, position):
        pass


class ButtonRestart(Button):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, left, top, width, height, fill):
        super().__init__(text_input, font_position_x, font_position_y, font_color, left, top, width, height, fill)

    def action(self, position, tabuleiro_preenchido=None, escondendo_numeros=None, tabuleiro_data=None, jogo_data=None):
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top, (self.top + self.height)):
            if pg.mouse.get_pressed()[0]:
                pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                self.pressed = True
            else:
                if self.pressed:
                    pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                    tabuleiro_preenchido = True
                    escondendo_numeros = True
                    tabuleiro_data = restart_tabuleiro_data()
                    jogo_data = restart_tabuleiro_data()
                    self.pressed = False

        return tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data


class ButtonAddFile(Button):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, left, top, width, height, fill):
        super().__init__(text_input, font_position_x, font_position_y, font_color, left, top, width, height, fill)

    def action(self, position):
        tabuleiro_file = None
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top, (self.top + self.height)):
            if pg.mouse.get_pressed()[0]:
                pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                self.pressed = True
            else:
                if self.pressed:
                    pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                    tabuleiro_file = controller_gerenciador_de_arquivos.abrindo_arquivo()
                    self.pressed = False

        return tabuleiro_file

class ButtonSolve(Button):
    def __init__(self, text_input, font_position_x, font_position_y, font_color, left, top, width, height, fill):
        super().__init__(text_input, font_position_x, font_position_y, font_color, left, top, width, height, fill)

    def action(self, position):
        if position[0] in range(self.left, (self.left + self.width)) and position[1] in range(self.top, (self.top + self.height)):
            if pg.mouse.get_pressed()[0]:
                pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                self.pressed = True
            else:
                if self.pressed:
                    pg.draw.rect(window, roxo_claro, (self.left, self.top, self.width, self.height), self.fill)
                    self.pressed = False


# Botões
button_restart = ButtonRestart('Reniciar', 540, 50, roxo_claro, 520, 40, 300, 80, 3)
button_add_file = ButtonAddFile('Adicionar', 535, 150, roxo_claro, 520, 140, 300, 80, 3)
button_solve = ButtonSolve('Resolver', 535, 250, roxo_claro, 520, 240, 300, 80, 3)


# retorna a linha y do tabuleiro_data
def linha_escolhida(tabuleiro_data, y):
    linha_sorteada = tabuleiro_data[y]
    return linha_sorteada

# retorna a coluna referente a posição x
#:return: lista que representa a coluna referente a posição x
def coluna_escolhida(tabuleiro_data, x):
    coluna_sorteada = []
    for c in range(8):
        coluna_sorteada.append(tabuleiro_data[c][x])
    return coluna_sorteada


# Escreve os quadrantes de acordo com suas posições
#:parametros: matriz tabuleiro_data e as posições x e y, que são passadas quando a função é chamada dentro do escopo da função preenchendo_quadrantes()
#:return: retorna o quadrante
def quadrante_selecionado(tabuleiro_data, x, y):
    quadrante = []

    # O extend() adiciona os elementos de uma lista dentro de outra lista
    # Contando da esquerda para a direita
    # quadrante 1
    if 0 <= x <= 2 and 0 <= y <= 2:
        quadrante.extend([tabuleiro_data[0][0], tabuleiro_data[0][1], tabuleiro_data[0][2],
                          tabuleiro_data[1][0], tabuleiro_data[1][1], tabuleiro_data[1][2],
                          tabuleiro_data[2][0], tabuleiro_data[2][1], tabuleiro_data[2][2]])
    # quadrante 2
    if 3 <= x <= 5 and 0 <= y <= 2:
        quadrante.extend([tabuleiro_data[0][3], tabuleiro_data[0][4], tabuleiro_data[0][5],
                          tabuleiro_data[1][3], tabuleiro_data[1][4], tabuleiro_data[1][5],
                          tabuleiro_data[2][3], tabuleiro_data[2][4], tabuleiro_data[2][5]])
    # quadrante 3
    if 6 <= x <= 8 and 0 <= y <= 2:
        quadrante.extend([tabuleiro_data[0][6], tabuleiro_data[0][7], tabuleiro_data[0][8],
                          tabuleiro_data[1][6], tabuleiro_data[1][7], tabuleiro_data[1][8],
                          tabuleiro_data[2][6], tabuleiro_data[2][7], tabuleiro_data[2][8]])
    # quadrante 4
    if 0 <= x <= 2 and 3 <= y <= 5:
        quadrante.extend([tabuleiro_data[3][0], tabuleiro_data[3][1], tabuleiro_data[3][2],
                          tabuleiro_data[4][0], tabuleiro_data[4][1], tabuleiro_data[4][2],
                          tabuleiro_data[5][0], tabuleiro_data[5][1], tabuleiro_data[5][2]])
    # quadrante 5
    if 3 <= x <= 5 and 3 <= y <= 5:
        quadrante.extend([tabuleiro_data[3][3], tabuleiro_data[3][4], tabuleiro_data[3][5],
                          tabuleiro_data[4][3], tabuleiro_data[4][4], tabuleiro_data[4][5],
                          tabuleiro_data[5][3], tabuleiro_data[5][4], tabuleiro_data[5][5]])
    # quadrante 6
    if 6 <= x <= 8 and 3 <= y <= 5:
        quadrante.extend([tabuleiro_data[3][6], tabuleiro_data[3][6], tabuleiro_data[3][7],
                          tabuleiro_data[4][6], tabuleiro_data[4][6], tabuleiro_data[4][7],
                          tabuleiro_data[5][6], tabuleiro_data[5][6], tabuleiro_data[5][7]])
    # quadrante 7
    if 0 <= x <= 2 and 6 <= y <= 8:
        quadrante.extend([tabuleiro_data[6][0], tabuleiro_data[6][1], tabuleiro_data[6][2],
                          tabuleiro_data[7][0], tabuleiro_data[7][1], tabuleiro_data[7][2],
                          tabuleiro_data[8][0], tabuleiro_data[8][1], tabuleiro_data[8][2]])
    # quadrante 8
    if 3 <= x <= 5 and 6 <= y <= 8:
        quadrante.extend([tabuleiro_data[6][3], tabuleiro_data[6][4], tabuleiro_data[6][5],
                          tabuleiro_data[7][3], tabuleiro_data[7][4], tabuleiro_data[7][5],
                          tabuleiro_data[8][3], tabuleiro_data[8][4], tabuleiro_data[8][5]])
    # quadrante 9
    if 6 <= x <= 8 and 6 <= y <= 8:
        quadrante.extend([tabuleiro_data[6][6], tabuleiro_data[6][7], tabuleiro_data[6][8],
                          tabuleiro_data[7][6], tabuleiro_data[7][7], tabuleiro_data[7][8],
                          tabuleiro_data[8][6], tabuleiro_data[8][7], tabuleiro_data[8][8]])
    return quadrante


# preenche cada quadrante do sudoku, em sequencia do quadrante 1 ao 9, seguindo a ordem passada na função tabuleiro_completo()
# :paramentros: o tabuleiro_data onde serão preenchidos os numero do sudoku/ As posições x e y referente a cada quadrante
# :return: tabuleiro_data com o quadrante preenchido
def preenchendo_quadrantes(tabuleiro_data, x2, y2):
    quadrante_preenchido = True
    # quantas vezes o while executou
    loop = 0
    try_count = 0
    # numero que é incrementado até 9, para preencher o tabuleiro com numeros de 1 a 9
    numero = 1
    while quadrante_preenchido:
        # esse randint retorna um numero entre o numero inicial do quadrante
        # passado no tabuleiro completo e o numero maximo do quadrante
        x = random.randint(x2, x2+2)
        y = random.randint(y2, y2+2)
        # retorna a linha y do tabuleiro data
        linha_sorteada = linha_escolhida(tabuleiro_data, y)

        # retorna a coluna referente a posição x
        coluna_sorteada = coluna_escolhida(tabuleiro_data, x)

        # o quadrante é referente as posições x e y passadas na função tabuleiro_completo(), que são verificadas na função quadrante_selecionado(), que por sua vez retorna o quadrante em questão
        quadrante = quadrante_selecionado(tabuleiro_data, x, y)

        # verifica se nas posiçoes x e y do tabuleiro tem um 'n' e se o valor da variável numero não está na linha, coluna ou quadrante
        # SE VERDADEIRO: o numero é colocado na posicao x e y do tabuleiro e a variavel numero incrementada
        # SENAO: o while continua
        if tabuleiro_data[y][x] == 'n' and numero not in linha_sorteada and numero not in coluna_sorteada and numero not in quadrante:
            tabuleiro_data[y][x] = numero
            numero += 1

        # A variável loop trabalha junto ao try_count no Controle de Looping, impedindo que o While rode infinitamente
        # Se o looping chegar a 50, o quadrante é reniciado, todas suas posições volta a ser 'n'
        # A variável loop é zerada, a variavel numero volta a 1 e a variavel try_count é incrementada
        loop += 1
        if loop == 50:
            tabuleiro_data[y2][x2] = 'n'
            tabuleiro_data[y2][x2 + 1] = 'n'
            tabuleiro_data[y2][x2 + 2] = 'n'
            tabuleiro_data[y2 + 1][x2] = 'n'
            tabuleiro_data[y2 + 1][x2 + 1] = 'n'
            tabuleiro_data[y2 + 1][x2 + 2] = 'n'
            tabuleiro_data[y2 + 2][x2] = 'n'
            tabuleiro_data[y2 + 2][x2 + 1] = 'n'
            tabuleiro_data[y2 + 2][x2 + 2] = 'n'
            loop = 0
            numero = 1
            try_count += 1

        # Se a variável try_count for igual a 10 o loop While é encerrado
        # Isso siginifica que a função While rodou 500 vezes no total (multiplicando o loop=50*try_count=10)
        if try_count == 10:
            break

        # conta a quantidade de numeros existente no quadrante
        # Verifica se os quadrantes estão vazios, se não estiverem a varivael count é incrementada
        count = 0
        for n in range(9):
            if quadrante[n] != 'n':
                count += 1

        # Se count for igual a 9, siginifica que o quadrante está totalmente preenchido
        # Então, a varivel booleana quadrante_preenchido se torna Falsa e o loop While é encerrado
        # Retornando o tabuleiro com o quadrante preenchido
        if count == 9:
            quadrante_preenchido = False
    return tabuleiro_data


# função que chama outra função preenchendo_quadrantes para cada quadrante do tabuleiro
# :parametros: a matriz tabuleiro_data e a variável booleana tabuleiro_preenchido
# :return: a matriz tabuleiro_data preenchida e a variável booleana tabuleiro_preenchido igual a False
def tabuleiro_completo(tabuleiro_data, tabuleiro_preenchido):
    while tabuleiro_preenchido == True:
        # quadrante 1
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 0, 0)
        # quadrante 2
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 3, 0)
        # quadrante 3
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 6, 0)
        # quadrante 4
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 0, 3)
        # quadrante 5
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 0, 6)
        # quadrante 6
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 3, 3)
        # quadrante 7
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 3, 6)
        # quadrante 8
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 6, 3)
        # quadrante 9
        tabuleiro_data = preenchendo_quadrantes(tabuleiro_data, 6, 6)

        # Verifica se no tabuleiro existe algum 'n'
        # Se existir, o tabuleiro é reniciado
        for i in range(9):
            for j in range(9):
                if tabuleiro_data[i][j] == 'n':
                    tabuleiro_data = restart_tabuleiro_data()

        # Verifica cada posição do tabuleiro, incremetando count se a posição for diferente de 'n'
        count = 0
        for i in range(9):
            for j in range(9):
                if tabuleiro_data[i][j] != 'n':
                    count += 1

        # Se count for igual a 81, significa que o tabuleiro foi completamente preenchido
        # a variavel booleana passa a ser False e encherra o looping While
        if count == 81:
            tabuleiro_preenchido = False
    return tabuleiro_data, tabuleiro_preenchido


# Adiciona alguns numeros do tabuleiro_data ao jogo_data de forma a deixar espaços em branco
# :parametros: matrizes tabuleiro_data e jogo_data/ variável booleana escondendo_numeros
# :return: matriz jogo_data preenchido e variável booleana escondendo_numeros False
def esconder_numeros(tabuleiro_data, jogo_data, escondendo_numeros):
    if escondendo_numeros == True:
        for i in range(60):
            sortear_numero = True
            while sortear_numero == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if jogo_data[y][x] == 'n':
                    jogo_data[y][x] = tabuleiro_data[y][x]
                    sortear_numero = False
            escondendo_numeros = False
    return jogo_data, escondendo_numeros


# função que escreve os numeros na tela
def escrever_numeros(window, jogo_data):
    quadrado = 50
    ajuste = 30
    for i in range(9):
        for j in range(9):
            if jogo_data[i][j] != 'n':
                number = font.render(str(jogo_data[i][j]), True, roxo_claro)
                window.blit(number, (ajuste+j*quadrado+13, ajuste+i*quadrado))
                if jogo_data[i][j] == 'X':
                    number = font.render(str(jogo_data[i][j]), True, 'white')
                    window.blit(number, (ajuste+j*quadrado+13, ajuste+i*quadrado))


# Quando digitamos com o teclado numerico ele vem no formato [0]
# Desse modo, a função trasforma o numero dentro do colchete em um int()
# :parametros: numero digitado pelo usuario
# :return: numero tranformado pela função
def numero_digitado(numero):
    try:
        numero = int(numero[1])
    except:
        numero = int(numero)
    return numero


def checar_numero_digitado(tabuleiro_data, jogo_data, click_x, click_y, numero):
    if 0 <= click_x <= 8 and 0 <= click_y <= 8 and tabuleiro_data[click_y][click_x] == numero and jogo_data[click_y][click_x] == 'n' and numero != 0:
        jogo_data[click_y][click_x] = numero
        numero = 0
    if 0 <= click_x <= 8 and 0 <= click_y <= 8 and tabuleiro_data[click_y][click_x] == numero and jogo_data[click_y][click_x] == numero and numero != 0:
        pass
    if 0 <= click_x <= 8 and 0 <= click_y <= 8 and tabuleiro_data[click_y][click_x] != numero and jogo_data[click_y][click_x] == 'n' and numero != 0:
        jogo_data[click_y][click_x] = 'X'
    if 0 <= click_x <= 8 and 0 <= click_y <= 8 and tabuleiro_data[click_y][click_x] == numero and jogo_data[click_y][click_x] == 'X' and numero != 0:
        jogo_data[click_y][click_x] = numero
        numero = 0
    return jogo_data, numero


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            numero = pg.key.name(event.key)
        elif event.type == pg.KEYUP:
            numero = 0

    # Posicao do mouse
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
    button_solve.update()
    button_solve.hover(mouse)
    tabuleiro_data, tabuleiro_preenchido = tabuleiro_completo(tabuleiro_data, tabuleiro_preenchido)
    jogo_data, escondendo_numeros = esconder_numeros(tabuleiro_data, jogo_data, escondendo_numeros)
    escrever_numeros(window, jogo_data)
    numero = numero_digitado(numero)
    jogo_data, numero = checar_numero_digitado(tabuleiro_data, jogo_data, click_position_x, click_position_y, numero)
    tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data = button_restart.action(mouse, tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data)



    # click_last_status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()

pg.quit()
