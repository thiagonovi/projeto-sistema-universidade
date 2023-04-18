import os, json
from string_storage import prompt, blank_data, estudante_object_blank, disciplina_object_blank, matricula_object_blank, professor_object_blank, turma_object_blank
from menu import clear


def seletor_arquivo(data_type):
    if data_type == 'a':
        archive = 'data/estudante.json'
        object_blank = estudante_object_blank
        return archive, object_blank
    elif data_type == 'b':
        archive = 'data/disciplina.json'
        object_blank = disciplina_object_blank
        return archive, object_blank
    elif data_type == 'c':
        archive = 'data/professor.json'
        object_blank = professor_object_blank
        return archive, object_blank
    elif data_type == 'd':
        archive = 'data/turma.json'
        object_blank = turma_object_blank
        return archive, object_blank 
    elif data_type == 'e':
        archive = 'data/matricula.json'
        object_blank = matricula_object_blank
        return archive, object_blank


def strings(data_type):
    global data_nome, do_dataType, um_dataType, um_novo_dataType, do_novo_dataType, este_dataType, archive
    if data_type == 'a':
        data_nome = 'estudante'
        do_dataType = 'do estudante'
        um_dataType = 'um estudante'
        um_novo_dataType = 'um novo estudante'
        do_novo_dataType = 'do novo estudante'
        este_dataType = "este estudante"
    elif data_type == 'b':
        data_nome = 'disciplina'
        do_dataType = 'da disciplina'
        um_dataType = 'uma disciplina'
        um_novo_dataType = 'uma nova disciplina'
        do_novo_dataType = 'da nova disciplina'
        este_dataType = "esta disciplina"
    elif data_type == 'c':
        data_nome = 'professor'
        do_dataType = 'do professor'
        um_dataType = 'um professor'
        um_novo_dataType = 'um novo professor'
        do_novo_dataType = 'do novo professor'
        este_dataType = "este professor"
    elif data_type == 'd':
        data_nome = 'turma'
        do_dataType = 'da turma'
        um_dataType = 'uma turma'
        um_novo_dataType = 'uma nova turma'
        do_novo_dataType = 'da nova turma'
        este_dataType = "esta turma"
    elif data_type == 'e':
        data_nome = 'matrícula'
        do_dataType = 'da matrícula'
        um_dataType = 'uma matrícula'
        um_novo_dataType = 'uma nova matrícula'
        do_novo_dataType = 'da nova matrícula'
        este_dataType = "esta matrícula"


def arquivo_novo(archive, blank_data):
    with open(archive) as f:
        if len(f.read()) <= 3:
            data = json.loads(blank_data)
            with open(archive, "w") as f:
                json.dump(data, f, indent=2)


def add_novo_dado_vazio(archive, object_blank):
    with open(archive) as f:
        data = json.load(f)
    new_data = json.loads(object_blank)
    data.append(new_data)
    return data


def add_dados_relacionados(key, data_type):

    archive, object_blank = seletor_arquivo(data_type)
    arquivo_novo(archive, blank_data)

    with open(archive) as f:
        data = json.load(f)
    while True:
        print(f"Digite o código do(a){key} d{este_dataType}")
        while True:
            try:
                new_data = int(input(prompt))
                break
            except ValueError:
                print("Insira somente números nesta opção")
        if any(d.get('codigo') == new_data for d in data):
            break
        else:
            print(f"Não consta no sistema um(a) {key} com o código '{new_data}'. Deseja cadastrar um(a) novo(a){key}? [s]/[n]")
            answear = input(prompt).lower()
            if answear == 's':
                insert_data(data_type)
                break
    return new_data


def add_novas_infos(key, index, data):
    if key == 'codigo':
        while True:
            try:
                novo_dado = int(input(f"{key.capitalize()}: "))
                if any(d.get(key) == novo_dado for d in data):
                    if index == len(data)-1:
                        sugestao = data[len(data)-2][key] + 1
                    else:
                        sugestao = data[len(data)-1][key] + 1
                    print(f"Código já utilizado. Informe um outro número (sugestão: {sugestao})")
                else:
                    dado_final = novo_dado
                    break
            except ValueError:
                print("Infome somente números.")
    elif key in ('disciplina', 'professor', 'aluno'):
        if key == 'aluno':
            special_data_type = 'a'
        elif key == 'professor':
            special_data_type = 'c'
        elif key == 'disciplina':
            special_data_type = 'b'
        dado_final = add_dados_relacionados(key, special_data_type)
    else:
        dado_final = input(f"{key.capitalize()}: ")

    return dado_final


def insert_data(data_type):
    strings(data_type)
    archive, object_blank = seletor_arquivo(data_type)
    arquivo_novo(archive, blank_data)
    data = add_novo_dado_vazio(archive, object_blank)

    print("Informe os seguintes dados: ")
    for key in data[len(data)-1]:
        data[len(data)-1][key] = add_novas_infos(key, len(data)-1, data)
    with open(archive, "w") as f:
        json.dump(data, f, indent=2)

    clear()
    print("Novos dados adicionados ao sistema com sucesso")


def list_data(data_type):
    strings(data_type)
    archive, object_blank = seletor_arquivo(data_type)

    clear()
    with open(archive) as f:
        if len(f.read()) <= 3:
            print(f"Não há nenh{um_dataType} cadastrado no sistema.")
        else:
            with open(archive) as f:
                data = json.load(f)
                i = 0
                print("***************")
                for estudantes in data:
                    print(f"\n{data_nome} n. {i+1}\n")
                    for key, value in data[i].items():
                        print(f"{key.capitalize()}: {value}")
                    i += 1
                print("\n***************\n")


def exclude_data(answear1):
    strings(answear1)
    archive, object_blank = seletor_arquivo(answear1)

    with open(archive) as f:
        if len(f.read()) <= 3:
            clear()
            print(f"Não há nenh{um_dataType} cadastrado no sistema")
        else:
            with open(archive) as f:
                data = json.load(f)
            print(f"Informe o código {do_dataType} que você deseja excluir")
            while True:
                try:
                    codigo = int(input(prompt))
                    break
                except ValueError:
                    print("Código inválido. Tente novamente, informando somente números")
            i = 0
            for index, objt in enumerate(data):
                if objt['codigo'] == codigo:
                    i = 1

                    clear()
                    while True:
                        print(f"É {este_dataType} que deseja excluir? [s/n]")
                        print("***************\n")
                        for key, value in data[index].items():
                            print(f"{key.capitalize()}: {value}")
                        print("\n***************\n")
                        resposta = input(prompt).lower()

                        if resposta == 's':
                            del data[index]
                            with open(archive, "w") as f:
                                json.dump(data, f, indent=2)
                            clear()
                            print(f"Registro {do_dataType} removido com sucesso")
                            break
                        elif resposta == 'n':
                            clear()
                            print("Remoção não concluída.")
                            break
                        else:
                            clear()
                            print("Selecione uma opção válida.")
                    break
                if i == 0:
                    clear()
                    print(f"Não há nenh{um_dataType} com esse código.")

def edit_data(answear1):
    letras = 'ABCDEFG'
    strings(answear1)
    archive, object_blank = seletor_arquivo(answear1)

    with open(archive) as f:
        if len(f.read()) <= 3:
            clear()
            print(f"Não há nenh{um_dataType} cadastrado no sistema")
        else:
            with open(archive) as f:
                data = json.load(f)
             
                print(f"Insira o código {do_dataType} que deseja editar:")
                while True:
                    try:
                        codigo = int(input(prompt))
                        break
                    except ValueError: 
                        print("Código inválido. Informe somente números")
                i = 0
                for index, objt in enumerate(data):
                    if objt['codigo'] == codigo:
                        i = 1
                        clear()
                        while True:
                            print(f"É {este_dataType} que deseja editar? [s/n]")
                            print("***************\n")
                            for key, value in data[index].items():
                                print(f"{key.capitalize()}: {value}")
                            print("\n***************\n")
                            resposta = input(prompt).lower()

                            if resposta == 's':
                                while True:
                                    print("Selecione a informação que deseja editar:")
                                    for key, letra in zip(data[index], letras):
                                        print(f"[{letra}] {key.capitalize()}")
                                    while True:
                                        while True:
                                            try:
                                                resposta2 = input(prompt).upper()
                                                break
                                            except ValueError:
                                                print("Selecione uma opção válida.")
                                        if resposta2 in letras:
                                            break
                                        else:
                                            print("Selecione uma opção válida.")
                                    key = list(data[index])[letras.index(resposta2)]
                                    print("Adicione a nova informação:")
                                    data[index][key] = add_novas_infos(key, index, data)

                                    with open(archive, "w") as f:
                                        json.dump(data, f, indent=2)

                                    print(f"Edição concluída. Deseja editar outra informação d{este_dataType}? [s]/[n]")
                                    resposta_final = input(prompt)
                                    if resposta_final == 's':
                                        clear()
                                    elif resposta_final == 'n':
                                        clear()
                                        print("Edição finalizada com sucesso.")
                                        break
                                break
                                        

                            elif resposta == 'n':
                                clear()
                                print("Edição não concluída.")
                                break
                            else:
                                clear()
                                print("Selecione uma opção válida.")
                if i == 0:
                    print(f"Não consta no sistema {um_dataType} com o código '{codigo}'. Deseja cadastrar {um_novo_dataType}? [s]/[n]")
                    answear = input(prompt).lower()
                    if answear == 's':
                        insert_data(answear1)









