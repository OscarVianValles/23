from abc import ABC, abstractmethod

class Sentence:
    def __init__(self, words:[str]):
        self.__words = words

    def __str__(self) -> str:
        sentenceString = ""
        for word in self.__words:
            sentenceString += word + " "
        return sentenceString[:-1]

class FormattedSentence(ABC, Sentence):
    def __init__(self, wrappedSentence:Sentence):
        self.wrappedSentence = wrappedSentence

    @abstractmethod
    def __str__(self) -> str:
        pass

class BorderedSentence(FormattedSentence):
    def __str__(self) -> str:
        borderString =  "┌" + "─" * (len(str(self.wrappedSentence)) + 2) + "┐\n"
        borderString += "│ " + str(self.wrappedSentence) + " │\n"
        borderString += "└" + "─" * (len(str(self.wrappedSentence)) + 2) + "┘"
        return borderString

class FancySentence(FormattedSentence):
    def __str__(self) -> str:
        return "░░▒▓███ " + str(self.wrappedSentence) + " ███▓▒░░"

class UpperCaseSentence(FormattedSentence):
    def __str__(self) -> str:
        return str(self.wrappedSentence).upper()


if __name__ == "__main__":
    s = Sentence(["Test", "Test"])
    print(s)
    b = FancySentence(s)
    print(b)
    c = BorderedSentence(UpperCaseSentence(b))
    print(c)
