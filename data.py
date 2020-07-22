from AutoComplete import Autocomplete
dict = {}
dictFile = {1:"about.txt"}
listString = []
def readFromFile():
    for key,value in dictFile.items():
        with open(value) as the_file:
            templistString = the_file.read().split("\n")
        for str in templistString:
            listString.append({"sentence" :str, "source": key})


def initData():
    for j in range(len(listString)):
        for index in range(len(listString[j]["sentence"])+1):
            dict.setdefault(listString[j]["sentence"][:index+1], set()).add(j)
        listwords = listString[j]["sentence"].split(" ")
        for i in range(len(listwords)):
            for k in range(len(listwords[i])+1):
                dict.setdefault(listwords[i][:k + 1], set()).add(j)
    for sentence in dict.keys():
        dict[sentence] = sorted(dict[sentence],
            key=lambda k: listString[k]["sentence"][(listString[k]["sentence"]).index(sentence):])


readFromFile()
initData()
print(dict)

print(len(dict))
def change(string,count,list1):
    print("i amm change")
    flag = 0
    score = 0
    for lenghString, word in enumerate(string[::-1],1):
        for x in range(ord('a'), ord('z') + 1):
            if dict.get(string.replace(word, chr(x))):
                    if chr(x) != string[-lenghString]:
                        if lenghString <= len(string) - 4:
                            score = 1
                        else:
                            score = lenghString - 1
                        i = 0
                        while count < 5 and i < len(dict[string.replace(word, "",1)]):
                            list1.append(Autocomplete(listString[i]["sentence"], dictFile[listString[i]["source"]], listString[i]["sentence"].find(string[:-lenghString]),2 * len(string) - score).print())
                            i = i + 1
                            count = count + 1
                        flag = 1
                        return flag


def add(string,count,list1):
    print("i amm add")
    flag = 0
    for lenghString, word in enumerate(string[::-1],1):
        for x in range(ord('a'), ord('z') + 1):
            if dict.get(string.replace(word, word+chr(x))):
                    if lenghString <= len(string) - 4:
                        score = 1
                    else:
                        score = lenghString - 1
                    i = 0
                    while (count < 5 and i < len(dict[string.replace(word, word+chr(x))])):
                        list1.append(Autocomplete(listString[i]["sentence"], dictFile[listString[i]["source"]], listString[i]["sentence"].find(string.replace(word, word+chr(x))),2 * len(string) - score*2).print())
                        i = i + 1
                        count = count + 1
                    flag = 1
                    return flag


def delete(string, count, list1):
    print("i amm delete")
    flag = 0
    for lenghString, word in enumerate(string[::-1],1):
            if dict.get(string.replace(word, "",1)):
                if lenghString <= len(string) - 4:
                    score = 1
                else:
                    score = lenghString - 2
                i = 0
                while count < 5 and i < len(dict[string.replace(word, "",1)]):
                    list1.append(Autocomplete(listString[i]["sentence"], dictFile[listString[i]["source"]], listString[i]["sentence"].find(string.replace(word, "",1)),
                                              2 * len(string) - 2*score).print())
                    i = i + 1
                    count = count + 1
                flag = 1
                return flag


def changeInput(string, count, list1):

    if(change(string,count,list1)):
        return
    else:
        if(delete(string,count,list1)):
            return
        else:
            if(add(string, count, list1)):
                return


def autocompleteData(string):
    list1 = []
    count = 0
    if(dict.get(string)):
        for index in dict[string]:
            if count < 5:
                list1.append(Autocomplete(listString[index]["sentence"], dictFile[listString[index]["source"]],listString[index]["sentence"].find(string),2*len(string)).print())
            count = count+1
        if count < 5:
            changeInput(string,count,list1)
    else:
       changeInput(string,count,list1)
    return list1


str = "wond"
print(autocompleteData(str))
