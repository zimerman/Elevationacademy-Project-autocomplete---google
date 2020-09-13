import re
import os

listString = []
dict_data = {}
dictFile = {}


def ignore_character(string):
    return re.sub('[^a-z0-9' ']+', '', string.lower())


def read_from_file():
    for root, dirs, files in os.walk('data', topdown=True):
        for line_index, file in enumerate(files, 1):
            dictFile[line_index] = root+'\\'+file
            init_data(root+'\\'+file, line_index)


def init_data(file, index_source):
    with open(file, encoding='UTF-8') as the_file:
        templist_string = the_file.read().split("\n")
    for i, string in enumerate(templist_string, 1):
        listString.append({"sentence": string, "source": index_source, "offset": i})


def init_substrings():
    for j in range(len(listString)):
        for index1 in range(len(listString[j]["sentence"]) + 1):
            for index2 in range(index1+1, len(listString[j]["sentence"])+1):
                dict_data.setdefault(ignore_character(listString[j]["sentence"][index1:index2]), set()).add(j)
                dict_data.setdefault(ignore_character(listString[j]["sentence"][index2:index1]), set()).add(j)
    for sentence in dict_data.keys():
        dict_data[sentence] = list(dict_data[sentence])
        dict_data[sentence] = sorted(dict_data[sentence], key=lambda k: listString[k]["sentence"])


read_from_file()
init_substrings()

