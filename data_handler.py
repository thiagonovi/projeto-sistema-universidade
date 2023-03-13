import os, json
from string_storage import prompt, estudante_blank, estudante_object_blank


def insert_data_estudante(archive):
    with open(archive) as f:
        if len(f.read()) <= 1:
            data = json.loads(estudante_blank)
            with open(archive, "w") as f:
                json.dump(data, f, indent=2)

    with open(archive) as f:
        data = json.load(f)
    new_student = json.loads(estudante_object_blank)
    data['estudantes'].append(new_student)

    print("Qual o nome do novo estudante?")
    new_name = input(prompt)
    data['estudantes'][len(data['estudantes'])-1]['nome'] = new_name

    print("Qual a idade no novo estudante?")
    new_age = input(prompt)
    data['estudantes'][len(data['estudantes'])-1]['idade'] = new_age

    print("Qual o curso do novo estudante?")
    new_course = input(prompt)
    data['estudantes'][len(data['estudantes'])-1]['curso'] = new_course 

    print("Qual o telefone do novo estudante?")
    new_phone = input(prompt)
    data['estudantes'][len(data['estudantes'])-1]['telefone'] = new_phone

    print("Qual o e-mail do novo estudante?")
    new_email = input(prompt)
    data['estudantes'][len(data['estudantes'])-1]['e-mail'] = new_email

    print("Qual a média no novo estudante?")
    new_gpa = input(prompt)
    data['estudantes'][len(data['estudantes'])-1]['media'] = new_gpa


    with open(archive, "w") as f:
        json.dump(data, f, indent=2)











