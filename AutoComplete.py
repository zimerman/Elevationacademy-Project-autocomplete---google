from data_structure import dict_data
from data_structure import dictFile
from data_structure import listString
from AutoCompleteData import Autocomplete


def is_exist_completion(list_dict, complete_string):
    for dict_complate in list_dict:
        if listString[dict_complate["index"]]["sentence"] == complete_string:
            return True
    return False


def change(string, count, list_dict):
    index = len(string)
    for index_string, word in enumerate(string[::-1], 1):
        index = index-1
        for x in range(ord('a'), ord('z')+1):
            sub_string = string[:-index_string]+chr(x)+string[len(string)-index_string+1:]
            if dict_data.get(sub_string):
                if chr(x) != string[-index_string]:
                    score = get_score(index)
                    add_completion(sub_string, count, 2*len(string)-score, list_dict)


def add(string, count, list_dict):
    index = len(string)
    for word in string[::-1]:
        index = index-1
        for x in range(ord('a'), ord('z')+1):
            sub_string = string.replace(word, chr(x)+word)
            if dict_data.get(sub_string):
                score = get_score(index)
                add_completion(sub_string, count, 2*len(string)-2*score, list_dict)


def delete(string, count, list_dict):
    index = len(string)
    for index_string, word in enumerate(string[::-1], 1):
        index = index-1
        sub_string = string[:-index_string] + string[len(string)-index_string+1:]
        if dict_data.get(sub_string):
            score = get_score(index)
            add_completion(sub_string, 2*len(string)-2*count, score, list_dict)


def fix_input(string, count, list_dict):
    change(string, count, list_dict)
    delete(string, count, list_dict)
    add(string, count, list_dict)
    list_dict = sorted(list_dict, key=lambda k: k["score"], reverse=True)


def get_best_5completions(string):
    list1 = []
    list_dict = []
    count = 0
    if dict_data.get(string):
        for index in dict_data[string]:
            if count < 5:
                list_dict.append({"index": index, "score": 2*len(string)})
                count = count+1
        if count < 5:
            fix_input(string, count, list_dict)
    else:
        fix_input(string, count, list_dict)
    i = 0
    for item in list_dict:
        if i < 5:
            i = i+1
            list1.append(Autocomplete(listString[item["index"]]["sentence"],
                         dictFile[listString[item["index"]]["source"]], listString[item["index"]]["offset"], item["score"]))
    return list1


def add_completion(string, count, score, list_dict):
    for item in dict_data[string]:
        if not is_exist_completion(list_dict, listString[item]["sentence"]) and count < 5:
            list_dict.append({"index": item, "score": score})
            count = count+1


def get_score(index):
    if index < 5:
        return 5-index
    else:
        return 1
