class Dictionary:
    def __init__(self):
        self.paroleConTraduzione = dict()

    def addWord(self, parolaETraduzione): #
        parolaAliena = parolaETraduzione[0]
        traduzioneAggiunta = parolaETraduzione[1]
        if parolaAliena in self.paroleConTraduzione.keys():
            traduzioniPrecedenti = self.paroleConTraduzione.get(parolaAliena)
            nuovaTraduzione = traduzioniPrecedenti +" "+ traduzioneAggiunta
            self.paroleConTraduzione[parolaAliena] = nuovaTraduzione
        else:
            self.paroleConTraduzione[parolaAliena] = traduzioneAggiunta


    def translate(self, parolaDaTradurre):
        output = ""
        if parolaDaTradurre in self.paroleConTraduzione.keys():
            output += self.paroleConTraduzione.get(parolaDaTradurre) + "\n"
        else:
            output += "Traduzione non trovata\n"
        return output

    def translateWordWildCard(self, query):
        output = ""
        prova = ""
        alfabeto = "abcdefghijklmnopqrstuvwxyzàèéìòùäëïöüâêîôûàçñ"
        selezione = []
        for lettera in alfabeto:
            prova = query.replace("?", lettera, 1)
            if prova in self.paroleConTraduzione.keys():
                selezione.append(prova)
        if len(selezione)==0:
            output += "Traduzione non trovata\n"
        else:
            for parolaAliena in selezione:
                output += f"{parolaAliena}: " + self.translate(parolaAliena)
        return output

    def __str__(self):
        myStr = ""
        for key, value in self.paroleConTraduzione.items():
            myStr += key + ": " + value + "\n"
        return myStr