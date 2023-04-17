import os, json
from string_storage import prompt, blank_data, estudante_object_blank, disciplina_object_blank, matricula_object_blank, professor_object_blank, turma_object_blank
from menu import clear

def strings(data_type):
    global data_nome, do_dataType, um_dataType, um_novo_dataType, do_novo_dataType, este_dataType
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

def add_codigo(arg):
    print("Qual o código do novo estudante?")
    while True:
        try:
            new_code = int(input(prompt))
            data[len(data)-1]['codigo'] = new_code
            break
        except ValueError:
            print("Insira somente números nesta opção")

   

def add_dados_relacionados(archive, data_type):
    strings(data_type)

    with open(archive) as f:
        data = json.load(f)
    while True:
        print(f"Digite o código {do_dataType} d{este_dataType}")
        while True:
            try:
                new_data = int(input(prompt))
                break
            except ValueError:
                print("Insira somente números nesta opção")
        if any(d.get('codigo') == new_data for d in data):
            break
        else:
            print(f"Não consta no sistema {um_dataType} com o código '{new_data}'. Deseja cadastrar {um_novo_dataType}? [s]/[n]")
            answear = input(prompt).lower()
            if answear == 's':
                insert_data(data_code)
                break
    data[len(data)-1][data_type] = data




def insert_data(data_type):


    if data_type == 'a':
        archive = 'data/estudante.json'
        object_blank = estudante_object_blank

        arquivo_novo(archive, blank_data)
        data = add_novo_dado_vazio(archive, object_blank)

        print("Qual o código do novo estudante?")
        while True:
            try:
                new_code = int(input(prompt))
                data[len(data)-1]['codigo'] = new_code
                break
            except ValueError:
                print("Insira somente números nesta opção")

        print("Qual o nome do novo estudante?")
        new_name = input(prompt)
        data[len(data)-1]['nome'] = new_name

        print("Qual o CPF do novo estudante?")
        new_cpf = input(prompt)
        data[len(data)-1]['cpf'] = new_cpf

        print("Qual a idade no novo estudante?")
        new_age = input(prompt)
        data[len(data)-1]['idade'] = new_age

        print("Qual o curso do novo estudante?")
        new_course = input(prompt)
        data[len(data)-1]['curso'] = new_course 

        print("Qual o telefone do novo estudante?")
        new_phone = input(prompt)
        data[len(data)-1]['telefone'] = new_phone

        print("Qual o e-mail do novo estudante?")
        new_email = input(prompt)
        data[len(data)-1]['e-mail'] = new_email


    elif data_type == 'b':
        archive = 'data/disciplina.json'
        object_blank = disciplina_object_blank 

        arquivo_novo(archive, blank_data)
        data = add_novo_dado_vazio(archive, object_blank)

        print("Qual o código da nova disciplina?")
        while True:
            try:
                new_code = int(input(prompt))
                data[len(data)-1]['codigo'] = new_code
                break
            except ValueError:
                print("Insira somente números nesta opção")

        print("Qual o nome da nova disciplina?")
        new_name = input(prompt)
        data[len(data)-1]['nome'] = new_name

    elif data_type == 'c':
        archive = 'data/professor.json'
        object_blank = professor_object_blank

        arquivo_novo(archive, blank_data)
        data = add_novo_dado_vazio(archive, object_blank)

        print("Qual o código do novo professor?")
        while True:
            try:
                new_code = int(input(prompt))
                data[len(data)-1]['codigo'] = new_code
                break
            except ValueError:
                print("Insira somente números nesta opção")

        print("Qual o nome do novo professor?")
        new_name = input(prompt)
        data[len(data)-1]['nome'] = new_name

        print("Qual o CPF do novo professor?")
        new_cpf = input(prompt)
        data[len(data)-1]['cpf'] = new_cpf

        print("Qual a idade do novo professor?")
        new_age = input(prompt)
        data[len(data)-1]['idade'] = new_age

        print("Qual a disciplina do novo professor?")
        new_course = input(prompt)
        data[len(data)-1]['curso'] = new_course 

        print("Qual o telefone do novo professor?")
        new_phone = input(prompt)
        data[len(data)-1]['telefone'] = new_phone

        print("Qual o e-mail do novo professor?")
        new_email = input(prompt)
        data[len(data)-1]['e-mail'] = new_email



    elif data_type == 'd':
        archive = 'data/turma.json'
        object_blank = turma_object_blank

        arquivo_novo(archive, blank_data)
        data = add_novo_dado_vazio(archive, object_blank)

        print("Qual o código da nova turma?")
        while True:
            try:
                new_code = int(input(prompt))
                data[len(data)-1]['codigo'] = new_code
                break
            except ValueError:
                print("Insira somente números nesta opção")

        arquivo_novo("data/professor.json", blank_data)
        add_dados_relacionados('data/professor.json', 'professor')

        arquivo_novo('data/disciplina.json', blank_data)
        add_dados_relacionados('data/disciplina.json', 'disciplina')

        arquivo_novo('data/estudante.json', blank_data)

        class_list = []
        with open("data/estudante.json") as fe:
            student_data = json.load(fe)
        while True:
            print("Digite o código do aluno que fará parte da nova turma (digite [0] para encerrar)")
            while True:
                try:
                    new_student = int(input(prompt))
                    break
                except ValueError:
                    print("Insira somente números nesta opção")
            if new_student == 0:
                break
            else:
                if any(d.get('codigo') == new_student for d in student_data):
                    class_list.append(new_student)
                else:
                    print(f"Não consta no sistema um aluno com o código '{new_student}'. Deseja cadastrar um novo aluno? [s]/[n]")
                    answear = input(prompt).lower()
                    if answear == 's':
                        insert_data('a')
        data[len(data)-1]['alunos'] = class_list

    elif data_type == 'e':
        archive = 'data/matricula.json'
        object_blank = matricula_object_blank

        arquivo_novo(archive, blank_data)
        data = add_novo_dado_vazio(archive, object_blank)

        print("Qual o código da nova matrícula?")
        while True:
            try:
                new_code = int(input(prompt))
                data[len(data)-1]['codigo'] = new_code
                break
            except ValueError:
                print("Insira somente números nesta opção")

        add_dados_relacionados('data/estudante.json', 'aluno')


    with open(archive, "w") as f:
        json.dump(data, f, indent=2)

    clear()
    print("Novos dados adicionados ao sistema com sucesso")


def list_data(data_type):
    strings(data_type)

    clear()
    with open(archive) as f:
        if len(f.read()) <= 3:
            print(f"Não há nenh{um_dataType} com esse código.")
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

    with open(archive) as f:
        if len(f.read()) <= 3:
            clear()
            print(f"Não há nenh{um_dataType} cadastrado no sistema")
        else:
            with open(archive) as f:
                data = json.load(f)
            print(f"Informe o código {do_dataType} que você deseja excluir")
            try:
                codigo = int(input(prompt))
            except ValueError:
                clear()
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
                                    key = list(data[index])[letras.index(input(prompt).upper())]
                                    print("Adicione a nova informação:")
                                    if key == 'codigo':
                                        while True:
                                            try:
                                                nova_info = int(input(prompt))
                                                break
                                            except ValueError:
                                                print("Insira somente números nesta opção")
                                    else:
                                        nova_info = input(prompt)

                                    data[index][key] = nova_info

                                    with open(archive, "w") as f:
                                        json.dump(data, f, indent=2)

                                    clear()
                                    print(f"Edição concluída. Deseja editar outra informação d{este_dataType}? [s]/[n]")
                                    resposta_final = input(prompt)
                                    if resposta_final == 's':
                                        pass
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









