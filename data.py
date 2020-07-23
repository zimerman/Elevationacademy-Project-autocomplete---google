from AutoComplete import Autocomplete
import re
sub_string_dict = {}
dictFile = {1: "about.txt"}
listString = []

def read_from_file():
    for key, value in dictFile.items():
        with open(value) as the_file:
            temp_list_string = the_file.read().split("\n")
        for index_line, line in enumerate(temp_list_string,1):
            listString.append({"sentence": line, "source": 1, "offset": index_line})


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
    return re.sub('[^a-z0-9]+', '', string.lower())


def is_exist_completion(list_dict, completion_sentences):
    for item in list_dict:
        if listString[item["index"]]["sentence"] == completion_sentences:
            return True
    return False


def change(string, count, list_dict):
    print("i amm change")
    score = 0
    index = len(string)
    for lenghString, word in enumerate(string[::-1], 1):
        for x in range(ord('a'), ord('z') + 1):
            if sub_string_dict.get(string.replace(word, chr(x))):
                if chr(x) != string[-lenghString]:
                    if index < 5:
                        score = 5 - index
                    else:
                        score = 1
                    i = 0
                    while count < 5 and i < len(sub_string_dict[string.replace(word, chr(x),1)]):
                        if not is_exist_completion(list_dict, listString[sub_string_dict[string.replace(word, chr(x),1)][i]]["sentence"]):
                            list_dict.append({"index": sub_string_dict[string.replace(word, chr(x),1)][i], "score": 2 * len(string) - score})
                        i = i + 1
                        count = count + 1


def add(string, count, list_dict):
    print("i amm add")
    index = len(string)
    for lenghString, word in enumerate(string[::-1],1):
        for x in range(ord('a'), ord('z') + 1):
            if sub_string_dict.get(string.replace(word, word+chr(x))):
                    if index < 5:
                        score = 5 - index
                    else:
                        score = 1
                    i = 0
                    while count < 5 and i < len(sub_string_dict[string.replace(word, word+chr(x))]):
                        if not is_exist_completion(list_dict, listString[sub_string_dict[string.replace(word, word+chr(x), 1)][i]]["sentence"]):
                            list_dict.append({"index": sub_string_dict[string.replace(word, word+chr(x))][i], "score": 2 * len(string) - 2 * score})
                        i = i + 1
                        count = count + 1
        index = index - 1
    return list_dict


def delete(string, count, list_dict):
    print("i amm delete")
    flag = 0
    index = len(string)
    for lenghString, word in enumerate(string[::-1], 1):
            if sub_string_dict.get(string.replace(word, "", 1)):
                if index < 5:
                    score = 5 - index
                else:
                    score = 1
                i = 0
                while count < 5 and i < len(sub_string_dict[string.replace(word, "", 1)]):
                    if not is_exist_completion(list_dict, listString[sub_string_dict[string.replace(word, "", 1)][i]]["sentence"]):
                        list_dict.append({"index": sub_string_dict[string.replace(word, "", 1)][i], "score": 2 * len(string) - 2*score})
                    i = i + 1
                    count = count + 1


def changeInput(string, count, list_dict):
    change(string, count, list_dict)
    delete(string, count, list_dict)
    add(string, count, list_dict)
    list_dict = sorted(list_dict, key=lambda x: x["score"], reverse=True)
    return list_dict


def autocompleteData(string):
    list_dict = []
    list1 = []
    count = 0
    if sub_string_dict.get(string):
        for index in sub_string_dict[string]:
            if count < 5:
                list_dict.append({"index": index, "score": 2 * len(string)})
            count = count+1
        if count < 5:
            changeInput(string, count, list_dict)
    else:
        changeInput(string, count, list_dict)
    i = len(list1)
    for dict in list_dict:
        if i < 5:
            list1.append(Autocomplete(listString[dict["index"]]["sentence"], dictFile[listString[dict["index"]]["source"]],listString[dict["index"]]["offset"], dict["score"]))
        i = i + 1
    return list1


read_from_file()
init_data()
