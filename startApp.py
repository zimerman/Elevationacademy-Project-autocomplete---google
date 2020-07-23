from data import ignore_character, autocompleteData


def print_obj(obj):
    print("Here are suggestion \n\n" + obj.get_completed_sentence() + ' ' + obj.get_source_text()[:-4] + '(' + str(obj.get_offset()) + ')')


def print_completion(list_obj):
    if len(list_obj) == 0:
        print("Not found match suggestions")
    for obj in list_obj:
        print_obj(obj)


def start_app():
    # while():
    user_input = input("Enter search input")
    while user_input[-1] != '#':
        print_completion(autocompleteData(ignore_character(user_input)))
        user_input += input()
        print(user_input)
    user_input = input("Enter search input")


start_app()
