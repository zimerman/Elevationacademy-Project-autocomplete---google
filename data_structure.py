import os
import re
listString = []
dictFile = {}
sub_string_dict = {}


def read_from_file():
    for dirpath, dirnames, files in os.walk('python-3.8.4-docs-text', topdown=True):
        for ind, file_name in enumerate(files, 1):
            dictFile[ind] = file_name
            init_list_dict(dirpath+"\\"+file_name, ind)


def init_list_dict(path, ind):
    with open(path, encoding='UTF-8') as the_file:
        temp_list_string = the_file.read().split("\n")
    for index_line, line in enumerate(temp_list_string, 1):
        listString.append({"sentence": line, "source": ind, "offset": index_line})


def init_data():
    for ind_sent in range(len(listString)):
        for index in range(len(listString[ind_sent]["sentence"])):
            for index2 in range(index+1, len(listString[ind_sent]["sentence"])+1):
                sub_string_dict.setdefault((ignore_character(listString[ind_sent]["sentence"])[index:index2]), set()).add(ind_sent)
                sub_string_dict.setdefault((ignore_character(listString[ind_sent]["sentence"])[index2:index]), set()).add(ind_sent)
    for sentence in sub_string_dict.keys():
        sub_string_dict[sentence] = list(sub_string_dict[sentence])
        sub_string_dict[sentence] = sorted(sub_string_dict[sentence], key=lambda k: listString[k]["sentence"])


def ignore_character(string):
    return re.sub('[^a-z0-9' ']+', '', string.lower())



