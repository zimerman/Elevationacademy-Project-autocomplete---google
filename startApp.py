from AutoComplete import get_best_5completions
from data_structure import ignore_character
from tkinter import *


def print_autocomplete(list_completed):
    if not list_completed:
        list_box.insert(END, "Not found match suggestions")
        name.delete(0, END)
    else:
        list_box.insert(END, "Here are suggestion")
    list_box.insert(END, "\n")
    for obj in list_completed:
            list_box.insert(END, obj.get_completed_sentence() + "(" + obj.get_source_text() + " " + str(obj.get_offset()) + ")")
            list_box.insert(END, "\n")


def start_app(string):
    if string[-1] != '#':
        print_autocomplete(get_best_5completions(ignore_character((string))))
    else:
        name.delete(0, END)


def click():
    list_box.delete(0, END)
    start_app(name.get())


root = Tk()
Label(root, text="enter your search").grid(column=0, row=0)
root.title("Auto complete")
name = Entry(width=80)
name.grid(row=1, column=0)
button = Button(root, text='Search', width=10, height=1, command=click)
button.grid(row=1, column=1)
list_box = Listbox(root, width=80)
list_box.grid(row=2, column=0)
mainloop()


