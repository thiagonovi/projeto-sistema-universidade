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

