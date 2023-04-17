from data_handler import *

def ultimate_menu_handler(answear1, answear2):
    if answear2 == 'a':
        insert_data(answear1)
    elif answear2 == 'b':
        list_data(answear1)
    elif answear2 == 'c':
        exclude_data(answear1) 
    elif answear2 == 'd':
        edit_data(answear1)
   






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

