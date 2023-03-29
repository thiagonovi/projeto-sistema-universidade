import os, json
from string_storage import prompt, estudante_blank, estudante_object_blank
from menu import clear


def insert_data_estudante(archive):
    with open(archive) as f:
        if len(f.read()) <= 1:
            data = json.loads(estudante_blank)
            with open(archive, "w") as f:
                json.dump(data, f, indent=2)

    with open(archive) as f:
        data = json.load(f)
    new_student = json.loads(estudante_object_blank)
    data.append(new_student)

    print("Qual o código do novo estudante?")
    new_code = int(input(prompt))
    data[len(data)-1]['codigo'] = new_code

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

    print("Qual a média no novo estudante?")
    new_gpa = input(prompt)
    data[len(data)-1]['media'] = new_gpa


    with open(archive, "w") as f:
        json.dump(data, f, indent=2)

    clear()
    print("Estudante inserido no sistema com sucesso")

def list_data(archive):
    clear()
    with open(archive) as f:
        if len(f.read()) <= 3:
            print("Nenhum estudante listado no sistema")
        else:
            with open(archive) as f:
                data = json.load(f)
                i = 0
                print("***************")
                for estudantes in data:
                    print(f"\nEstudante n. {i+1}\n")
                    for key, value in data[i].items():
                        print(f"{key.capitalize()}: {value}")
                    i += 1
                print("\n***************\n")

def exclude_data(archive):
    with open(archive) as f:
            data = json.load(f)
    
    print("Qual o código do estudante que você deseja excluir do sistema?")
    codigo = int(input(prompt))
    for index, objt in enumerate(data):
        if objt['codigo'] == codigo:
            del data[0]
            with open(archive, "w") as f:
                    json.dump(data, f, indent=2)











