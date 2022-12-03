import tkinter
from tkinter import filedialog


# Selecionando um arquivo que representa um sudoko de dentro sistema do usuário
# :return: arquivo selecionado pelo usuário
def abrir_arquivo_do_sistema():
    tk_screen = tkinter.Tk()
    # Esconde a janela do tkinter
    tk_screen.withdraw()
    arquivo = filedialog.askopenfilename()
    tk_screen.destroy()
    return arquivo


# Abrindo arquivo que possue o sudoku escrito
# return: retorna as irformações do arquivo em forma de matriz
def abrindo_arquivo():
    # abre arquivo selecionado
    arquivo_sudoku = open(abrir_arquivo_do_sistema())
    sudoku = []
    for a in arquivo_sudoku:
        lista = []
        for j in a:
            if j != '\n' and j != '[' and j != ']' and j != ',' and j != ' ':
                lista.append(int(j))

        sudoku.append(lista)
    print(sudoku)
    return sudoku


# Retorna o problema do sudoku resolvido em um novo arquivo
def criar_arquivo_resposta(sudoku):
    resposta = open('../../resposta.txt', 'w')
    for i in sudoku:
        resposta.write(str(i))
        resposta.write('\n')
