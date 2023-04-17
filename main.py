from menu import menu, data_menu, clear
from menu_handler import ultimate_menu_handler

clear()
while True:
    answear1 = menu()
    clear()
    while True:
        answear2 = data_menu()
        if answear2 != 'e':
            ultimate_menu_handler(answear1, answear2)
        else:
            clear()
            break
ultimate_menu_handler(answear1, answear2)
