from menu import menu, data_menu, clear
from menu_handler import ultimate_menu_handler

while True:
    clear()
    answear1 = menu()
    clear()
    answear2 = data_menu()
    if answear2 != 'e':
        break
ultimate_menu_handler(answear1, answear2)
