class WordSet:
    replacePuncs = [',', '.', '\'', '!']
    def __init__(self):
       self.words = set() 

    def addText(self, text):
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)

    @staticmethod
    def cleanText(text):
        for punc in WordSet.replacePuncs:
            text = text.replace(punc, '')
        return text.lower()

wordSet = WordSet()

wordSet.addText('Hi, I\'m Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)