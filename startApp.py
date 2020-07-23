from AutoComplete import autocompleteData
from data_structure import ignore_character
from data_structure import read_from_file, init_data


def print_obj(obj):
    print(obj.get_completed_sentence() + ' ' + obj.get_source_text()[:-4] + '(' + str(obj.get_offset()) + ')')


def print_completion(list_obj):
    if len(list_obj) == 0:
        print("Not found match suggestions")
        return False
    for obj in list_obj:
        print("Here are suggestion \n")
        print_obj(obj)
    return True


def start_app():
    user_input = input("Enter search input")
    while True:
        while user_input[-1] != '#':
            if not print_completion(autocompleteData(ignore_character(user_input))):
                break
            user_input += input()
            print(user_input)
        user_input = input("Enter search input")


read_from_file()
init_data()
start_app()
