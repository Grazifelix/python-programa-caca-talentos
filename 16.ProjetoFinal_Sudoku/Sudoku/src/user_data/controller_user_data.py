import json

file_path = 'C:/Users/enterprise/Desktop/PYTHON/Caca_talentos_2022_python/16.ProjetoFinal_Sudoku/Sudoku/src/user_data/user_data.json'
lista_user = []


class User:
    def __init__(self, nome, data, tempo):
        self.nome = nome
        self.data = data
        self.tempo = tempo

    def __repr__(self):
        return f"{self.nome, self.data, self.tempo}"


# Abrindo arquivo json
def open_json():
    with open(file_path, 'r+', encoding='utf-8') as f:
        data = json.load(f)
    return data


# escrevendo arquivo json
def write_json(new_data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4)


# retornando lista com valores json
def return_data():
    return lista_user

# inserindo um unico novo elemento a lista de objetos
def append_new_data_in_list(new_data):
    new_data = User(new_data["nome"], new_data["data"], new_data["tempo"])
    if len(lista_user) == 6:
        lista_user.remove(lista_user[0])
    lista_user.append(new_data)


# Lendo dados do json e os transformando em objetos da classe User
def convert_json_data_to_object():
    data = open_json()
    for i in data:
        user = User(i["nome"], i["data"], i["tempo"])
        lista_user.append(user)


# atualizando dados do json
def update_user_data(user_new_data):
    data = open_json()
    new_data = []
    delete_control = True
    if len(data) < 6:
        data.append(user_new_data)
        write_json(data)
    else:
        for d in data:
            if data[0] and delete_control:
                delete_control = False
            else:
                new_data.append(d)
        new_data.append(user_new_data)
        write_json(new_data)
