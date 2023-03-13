from string_storage import prompt, menu_string, data_menu_string

def menu():
    print(menu_string)

    answear = input(prompt).lower()
    return answear

def data_menu():
    print(data_menu_string)

    answear = input(prompt).lower()
    return answear

