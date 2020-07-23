class Autocomplete:
    def __init__(self,completed_sentence,source_text,offset,score):
        self.__completed_sentence =completed_sentence
        self.__source_text = source_text
        self.__offset = offset
        self.__score = score

    def print(self):
        print(self.__completed_sentence)
        print(self.__source_text)
        print(self.__offset)
        print(self.__score)

    def get_completed_sentence(self):
        return self.__completed_sentence

    def get_source_text(self):
        return self.__source_text

    def get_offset(self):
        return self.__offset

    def get_score(self):
        return self.__score
