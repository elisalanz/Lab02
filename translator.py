from dictionary import *

class Translator:

    def __init__(self):
        self.dizionario = Dictionary()

    def printMenu(self):
        stringa ="Translator Alien-Italian"
        print("-"*30+"\n"+f"{stringa:^30}\n"+"-"*30+"\n"+"1. Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n5. Exit\n"+"-"*30+"\n")

    def loadDictionary(self, dict):
        try:
            fileDictionary = open(dict, "r", encoding="utf-8")
            for line in fileDictionary:
                line = line.strip()
                campi = line.split(" ")
                self.dizionario.addWord(campi)
            fileDictionary.close()
        except IOError:
            pass

    def handleAdd(self, entry):
        self.dizionario.addWord(entry)

    def handleTranslate(self, query):
        return self.dizionario.translate(query)

    def handleWildCard(self,query):
        return self.dizionario.translateWordWildCard(query)