from string_storage import prompt, menu_string, data_menu_string, incorrect_option
from os import system, name

def clear():
    system('cls' if name == 'nt' else 'clear')

def menu():
    while True:
        print(menu_string)
        answear = input(prompt).lower()
        if answear in 'abcde':
            break
        else:
            clear()
            print(incorrect_option)

    return answear

def data_menu():
    while True:
        print(data_menu_string)
        answear = input(prompt).lower()
        if answear in 'abcd':
            break
        else:
            clear()
            print(incorrect_option)

    return answear

