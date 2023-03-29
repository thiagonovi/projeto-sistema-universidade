from data_handler import *

def ultimate_menu_handler(answear1, answear2):
    if answear1 == 'a':
        data = "data/estudante.json"
        if answear2 == 'a':
            insert_data_estudante(data)
        elif answear2 == 'b':
            list_data(data)
        elif answear2 == 'c':
            #print("Em desenvolvimento")
            exclude_data(data, answear1) #to create
        elif answear2 == 'd':
            print("Em desenvolvimento")
            # alter_data(data) to create
    elif answear1 == 'b':
        data = "data/disciplina.json"
    elif answear1 == 'c':
        data = "data/professor.json"
    elif answear1 == 'd':
        data = "data/turma.json"
    elif answear1 == 'e':
        data = "data/matricula.json"
    






#def menu_handler(answear):
#    if answear == 'a':
#        data = "data/estudante.json"
#    if answear == 'b':
#        data = "data/disciplina.json"
#    if answear == 'c':
#        data = "data/professor.json"
#    if answear == 'd':
#        data = "data/turma.json"
#    if answear == 'e':
#        data = "data/matricula.json"
#
#    return data
#
#def data_menu_handler(answear, data):
#    if answear == 'a':
#        print("Executar função a")
#    if answear == 'b':
#        print("Executar função b")
#    if answear == 'c':
#        print("Executar função c")
#    if answear == 'd':
#        print("Executar função d")
#

