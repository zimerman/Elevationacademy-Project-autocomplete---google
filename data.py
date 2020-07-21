

def initData():
    my_dict ={}
    with open("about.txt", "r") as file:
        listWords = file.read().split("\n")
    for j in range(len(listWords)):
        for i in range(len(listWords[j])):
            my_dict.setdefault((listWords[j])[:i+1], set()).add(j)
        listLetters = listWords[j].split()
        for k in range(len(listLetters)):
            for s in range(len(listLetters[k])):
                my_dict.setdefault((listLetters[k])[:s + 1], set()).add(j)


initData()
