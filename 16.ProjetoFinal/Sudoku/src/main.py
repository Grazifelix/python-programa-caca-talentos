# Este projeto é um Sudoku Solver (Resolvedor de Sudoku)
# Inicio: 01/12/22
# Graziela Maria

# Imports
import tkinter
from tkinter import filedialog
import pygame

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
    return sudoku

# for i in sudoku:
#     print(i)

# retorna o sudoku resolvido
def criar_arquivo_resposta(sudoku):
    resposta = open('../../resposta.txt', 'w')
    for i in sudoku:
        resposta.write(str(i))
        resposta.write('\n')

SCREEN_SIZE = (800, 700)
pygame.init()
window = pygame.display.set_mode(SCREEN_SIZE)
color = (255, 255, 255)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                sudoku = abrindo_arquivo()
                for i in sudoku:
                    print(i)

    window.fill(color)
    pygame.display.flip()

pygame.quit()