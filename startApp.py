from AutoComplete import autocompleteData
from data_structure import ignore_character


def print_obj(obj):
    print(obj.get_completed_sentence() + "(" + obj.get_source_text() + " " + str(obj.get_offset()) + ")")


def print_autocomplete(list_completed):
    if not list_completed:
        print("Not found match suggestions")
        return False
    for obj in list_completed:
        print("Here are suggestion \n")
        print_obj(obj)
    return True


def start_app():
    string = input("press your search")
    while True:
        while string[-1] != '#':
            if not print_autocomplete(autocompleteData(ignore_character((string)))):
                break
            string += input(string)
        string = input("press your search")


start_app()