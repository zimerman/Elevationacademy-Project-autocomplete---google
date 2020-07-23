from AutoCompleteData import AutoCompleteData
from data_structure import listString, sub_string_dict, dictFile


def is_exist_completion(list_dict, completion_sentences):
    for item in list_dict:
        if listString[item["index"]]["sentence"] == completion_sentences:
            return True
    return False


def change(string, count, list_dict):
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
                        if not is_exist_completion(list_dict, listString[list_dict[string.replace(word, chr(x),1)][i]]["sentence"]):
                            list_dict.append({"index": sub_string_dict[string.replace(word, chr(x),1)][i], "score": 2 * len(string) - score})
                            count = count + 1
                        i = i + 1


def add(string, count,list_dict):
    index = len(string)
    for lenghString, word in enumerate(string[::-1],1):
        index = index - 1
        for x in range(ord('a'), ord('z') + 1):
            newSub =string.replace(word,chr(x)+word)
            if sub_string_dict.get(newSub):
                if index < 5:
                    score = 5 - index
                else:
                    score = 1
                i = 0
                while count < 5 and i < len(sub_string_dict[newSub]):
                    if not is_exist_completion(list_dict, listString[sub_string_dict[newSub][i]]["sentence"]):
                        list_dict.append({"index": sub_string_dict[newSub][i], "score": 2 * len(string) - 2 * score})
                        count = count + 1
                    i = i + 1


def delete(string, count, list_dict):
    index = len(string)
    for lenghString, word in enumerate(string[::-1],1):
        index = index-1
        newSub = string[:-lenghString] + string[len(string) - lenghString+1:]
        if sub_string_dict.get(newSub):
            if index < 5:
                score = 5 - index
            else:
                score = 1
            i = 0
            while count < 5 and i < len(sub_string_dict[newSub]):
                if not is_exist_completion(list_dict, listString[dict_data[newSub][i]]["sentence"]):
                    list_dict.append({"index": sub_string_dict[newSub][i], "score": 2 * len(string) - 2 * score})
                    count = count + 1
                i = i + 1


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
            list1.append(AutoCompleteData(listString[dict["index"]]["sentence"], dictFile[listString[dict["index"]]["source"]],listString[dict["index"]]["offset"], dict["score"]))
        i = i + 1
    return list1
