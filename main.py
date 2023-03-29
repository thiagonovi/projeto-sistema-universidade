from menu import menu, data_menu, clear
from menu_handler import ultimate_menu_handler

clear()
while True:
    answear1 = menu()
    if answear1 in 'bcde':
        clear()
        print("Em Desenvolvimento")
    else:
        clear()
        while True:
            answear2 = data_menu()
            if answear2 != 'e':
                if answear2 == 'd': 
                    clear()
                    print("Em Desenvolvimento")
                else:
                    ultimate_menu_handler(answear1, answear2)
            else:
                clear()
                break
ultimate_menu_handler(answear1, answear2)
