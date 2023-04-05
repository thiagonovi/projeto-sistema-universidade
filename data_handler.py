import os, json
from string_storage import prompt, blank_data, estudante_object_blank, disciplina_object_blank, matricula_object_blank, professor_object_blank, turma_object_blank
from menu import clear


def insert_data(data_type):


    if data_type == 'a':
        archive = 'data/estudante.json'
        object_blank = estudante_object_blank

        with open(archive) as f:
            if len(f.read()) <= 1:
                data = json.loads(blank_data)
                with open(archive, "w") as f:
                    json.dump(data, f, indent=2)

        with open(archive) as f:
            data = json.load(f)
        new_data = json.loads(object_blank)
        data.append(new_data)

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
        with open(archive) as f:
            if len(f.read()) <= 1:
                data = json.loads(blank_data)
                with open(archive, "w") as f:
                    json.dump(data, f, indent=2)

        with open(archive) as f:
            data = json.load(f)
        new_data = json.loads(object_blank)
        data.append(new_data)

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
        with open(archive) as f:
            if len(f.read()) <= 1:
                data = json.loads(blank_data)
                with open(archive, "w") as f:
                    json.dump(data, f, indent=2)

        with open(archive) as f:
            data = json.load(f)
        new_data = json.loads(object_blank)
        data.append(new_data)

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
        with open(archive) as f:
            if len(f.read()) <= 1:
                data = json.loads(blank_data)
                with open(archive, "w") as f:
                    json.dump(data, f, indent=2)

        with open(archive) as f:
            data = json.load(f)
        new_data = json.loads(object_blank)
        data.append(new_data)

        print("Qual o código da nova turma?")
        while True:
            try:
                new_code = int(input(prompt))
                data[len(data)-1]['codigo'] = new_code
                break
            except ValueError:
                print("Insira somente números nesta opção")

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
                    print(f"Não consta no sistema um aluno com o código '{new_student}'. Deseja cadastrar um novo aluno? [y]/[n]")
                    answear = input(prompt).lower()
                    if answear == 'y':
                        insert_data('a')
        data[len(data)-1]['alunos'] = class_list

    elif data_type == 'e':
        archive = 'data/matricula.json'
        object_blank = matricula_object_blank
        with open(archive) as f:
            if len(f.read()) <= 1:
                data = json.loads(blank_data)
                with open(archive, "w") as f:
                    json.dump(data, f, indent=2)

        with open(archive) as f:
            data = json.load(f)
        new_data = json.loads(object_blank)
        data.append(new_data)

        print("Qual o código da nova matrícula?")
        while True:
            try:
                new_code = int(input(prompt))
                data[len(data)-1]['codigo'] = new_code
                break
            except ValueError:
                print("Insira somente números nesta opção")


    with open(archive, "w") as f:
        json.dump(data, f, indent=2)

    clear()
    print("Novos dados adicionados ao sistema com sucesso")


def list_data(data_type):
    if data_type == 'a':
        archive = "data/estudante.json"
        string1 = "Nenhum estudante listado"
        string2 = "Estudante"
    elif data_type == 'b':
        archive = "data/disciplina.json"
        string1 = "Nenhuma disciplina listada"
        string2 = "Disciplina"
    elif data_type == 'c':
        archive = "data/professor.json"
        string1 = "Nenhum professor listado"
        string2 = "Professor"
    elif data_type == 'd':
        archive = "data/turma.json"
        string1 = "Nenhuma turma listada"
        string2 = "Turma"
    elif data_type == 'e':
        archive = "data/matricula.json"
        string1 = "Nenhuma matricula listada"
        string2 = "Matrícula"
    clear()
    with open(archive) as f:
        if len(f.read()) <= 3:
            print(f"{string1} no sistema")
        else:
            with open(archive) as f:
                data = json.load(f)
                i = 0
                print("***************")
                for estudantes in data:
                    print(f"\n{string2} n. {i+1}\n")
                    for key, value in data[i].items():
                        print(f"{key.capitalize()}: {value}")
                    i += 1
                print("\n***************\n")


def exclude_data(archive, answear1):
    with open(archive) as f:
            data = json.load(f)
    
    if answear1 == 'a':
        string1 = "do estudante"
        string2 = "nenhum estudante"
        string3 = "este estudante"
    print(f"Informe o código {string1} que você deseja excluir")
    try:
        codigo = int(input(prompt))
    except ValueError:
        clear()
        print("Código inválido. Tente novamente, informando somente números")
    else:
        i = 0
        for index, objt in enumerate(data):
            if objt['codigo'] == codigo:
                i = 1

                clear()
                while True:
                    print(f"É {string3} que deseja excluir? [s/n]")
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
                        print(f"Registro {string1} removido com sucesso")
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
                print(f"Não há {string2} com esse código.")
        









