import json

file_path = 'C:/Users/enterprise/Desktop/PYTHON/Caca_talentos_2022_python/16.ProjetoFinal_Sudoku\Sudoku/src/user_data/user_data.json'
with open(file_path, encoding='utf-8') as user_data_json:
    user_data = json.load(user_data_json)

lista_user = []

class User:
    def __init__(self, nome, tempo, data):
        self.nome = nome
        self.data = data
        self.tempo = tempo

    def __repr__(self):
        return f"{self.nome, self.data, self.tempo}"

    def ob(self):
        return self.nome, self.data, self.tempo

def read_user_data():
    for i in user_data:
        user = User(i['nome'], i['data'], i['tempo'])
        lista_user.append(user)


def append_new_data(data):
    with open(file_path, 'r+', encoding='utf-8', ) as user_data_json:
        user_data = json.load(user_data_json)
        user_data.append(data)
        user_data_json.seek(0)
        json.dump(user_data, user_data_json, indent=4)


def return_data():
    return lista_user

