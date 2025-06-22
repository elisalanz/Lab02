import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    txtIn = input()

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?\n")
        txtIn = input()
        okInput = True
        controllo = (txtIn.strip()).split(" ")
        for campo in controllo:
            if campo.isalpha()==False:
                okInput = False
        if okInput:
            nuovaParola = ((txtIn.lower()).strip()).split(" ", 1)
            t.handleAdd(nuovaParola)
        else:
            print("Parola o traduzione non valida")
        print()

    elif int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?\n")
        txtIn = input()
        while txtIn.isalpha()==False:
            txtIn = input()
        print(t.handleTranslate(txtIn.lower()))

    elif int(txtIn) == 3:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        print(t.handleWildCard((txtIn.strip()).lower()))

    elif int(txtIn) == 4:
        print(t.dizionario)

    elif int(txtIn) == 5:
        break
