from string_storage import prompt, menu_string, data_menu_string, incorrect_option, confirmation_exit
from os import system, name

def clear():
    system('cls' if name == 'nt' else 'clear')

def exit_menu():
    while True:
        print(confirmation_exit)
        exit_answear = input(prompt)
        if exit_answear == 'a':
            exit()
        elif exit_answear == 'b':
            clear()
            break
        else:
            clear()
            print(incorrect_option)


def menu():
    while True:
        print(menu_string)
        answear = input(prompt).lower()
        if answear in 'abcde':
            break
        elif answear == 'f':   
            clear()
            exit_menu()
        else:
            clear()
            print(incorrect_option)

    return answear

def data_menu():
    while True:
        print(data_menu_string)
        answear = input(prompt).lower()
        if answear in 'abcde':
            break
        else:
            clear()
            print(incorrect_option)

    return answear

