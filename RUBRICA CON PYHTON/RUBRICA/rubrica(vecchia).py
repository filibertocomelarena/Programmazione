# Assegnamento 1  aa 2021-22 622AA modulo programmazione 9 crediti
# Gruppo:
# Nome Cognome Matricola email telefono
# (Nome Cognome Matricola email telefono)

class Rubrica:
    """ Costruttore: crea una rubrica vuota rappresentata come
        dizionario di contatti vuoto """

    def __init__(self):
        """ crea una nuova rubrica vuota """  # creo le rubriche, saranno di classe rubrica (p,q,r,rr)
        self.rub = {}

    def __str__(self):
        """ Serializza una rubrica attraverso una stringa
        con opportuna codifica (a scelta dello studente) """  # le rubriche verranno stampate con questa codifica
        #Creo una stringa vuota
        output = ""
        #Ciclo su items in rub
        for nomecognome, numero in self.rub.items():
            #con stampa:  nome,cognome : 1234567890
            output += nomecognome + " : " + str(numero) + "\n"
        return output

    def __eq__(self, r):
        """stabilisce se due rubriche contengono
        esattamente le stesse chiavi con gli stessi dati"""  # mette a confronto le rubriche che vengono create

        # Controllo che le due rubriche abbiano la stessa lunghezza
        if len(self.rub) != len(r.rub):
            return False

        # Scorriamo i record della prima rubrica (self)
        for nome_cognome in self.rub.keys():
            # Per ognuno di essi, controllo se esso esista anche nella seconda rubrica (r)
            if nome_cognome in r.rub.keys():
                # Se lo trovo, controllo che anche il numero sia uguale
                if self.rub[nome_cognome] != r.rub[nome_cognome]:
                    # Se non lo è, le due rubriche sono diverse
                    return False
            else:
                # Se non c'è proprio,allora le due rubriche sono diverse
                return False

        # Alla fine,se le altre condizioni non sono verificate, le due rubriche sono uguali
        return True

    def __add__(self, r):
        """crea una nuova rubrica unendone due (elimina i duplicati)
        e la restituisce come risultato --
        se ci sono contatti con la stessa chiave nelle due rubriche
        ne riporta uno solo """
        # Creo una nuova rubrica vuota
        nuova_rubrica = Rubrica()
        # Copio per intero la prima rubrica (self) nella nuova rubrica
        nuova_rubrica.rub = self.rub.copy()
        # Copio i record dalla seconda rubrica (r) nella nuova rubrica
        for chiave, valore in r.rub.items():
            # Se non esiste un record con la stessa chiave
            if not chiave in nuova_rubrica.rub.keys():
                # Lo inserisco
                nuova_rubrica.rub[chiave] = valore
        # Ritorno la nuova rubrica
        return nuova_rubrica

    def load(self, nomefile):
        """ carica da file una rubrica eliminando il
        precedente contenuto di self """
        # formato del file: nome,cognome:telefono\n
        # apro il file e lo 'ripulisco'
        input_file = open(nomefile, 'r')
        self.rub.clear()
        #leggo una linea del file e lo assegno a line
        line = input_file.readline()
        #dico che, fintanto che line no finisce, fintanto che non sarà None in pratica:
        while line:
            #separo cognome nome e valori
            data = line.rstrip().split(':')  # data[0] == "nome,cognome", data[1] == "telefono"
            #separo ulteriormente nome e cognome
            nome_cognome = data[0].split(',')  # nome_cognome[0] == "nome", nome_cognome[1] == "cognome"
            #inserisco i dati ottenuti
            self.inserisci(nome_cognome[0], nome_cognome[1], data[1])
            line = input_file.readline()

        #chiudo
        input_file.close()



    def inserisci(self, nome, cognome, dati):
        """ inserisce un nuovo contatto con chiave (nome,cognome)
        restituisce "True" se l'inserimento è andato a buon fine e "False"   
        altrimenti (es chiave replicata) -- case insensitive """
        #mi do una codifica dei dati in entrata
        nome = str(nome)
        cognome = str(cognome)
        dati = int(dati)
        #creo la chiave,ma minuscola, per il case insensitive
        chiavi = (nome + ',' + cognome).lower()
        #se la chiave no c'è:
        if chiavi not in self.rub.keys():
            #butto dentro il tutto
            self.rub[chiavi] = int(dati)
            return True
        else:
            #altrimenti...
            return False


    def modifica(self, nome, cognome, newdati):
        """ modifica i dati relativi al contatto con chiave (nome,cognome)
        sostituendole con "newdati" -- restituisce "True" se la modifica
        è stata effettuata e "False" altrimenti (es: la chiave non è presente )"""
        #elimino il problema di inserimento: solo un tipo di dato consentito
        if type(nome) != str or type(cognome) != str:
            return False
        #creo la chiave da inserire
        chiave = nome + ',' + cognome
        if chiave in self.rub.keys():
            #se c'è la aggiorno con un nuovo numero
            self.rub.update({chiave: newdati})
            return True
        else:#altrimenti...
            return False


    def cancella(self, nome, cognome):
        """ il contatto con chiave (nome,cognome) esiste lo elimina
        insieme ai dati relativi e restituisce True -- altrimenti
        restituisce False """
        #creo la chiave
        chiave = (nome + ',' + cognome)
        #verifico se essa esiste nel dizionario
        for i in self.rub.keys():
            if chiave == i:
                #se c'è, la elimino:
                self.rub.pop(i)
                return True
            else:
               return False


    def cerca(self, nome, cognome):
        """ restitusce i dati del contatto se la chiave e' presente
        nella rubrica e "None" altrimenti -- case insensitive """
        #codifico i dati
        nome = str(nome)
        cognome = str(cognome)
        chiave = nome + ',' + cognome
        #se la chiave è presente la restituisco
        if chiave in self.rub:
            return self.rub[chiave]
        else:
            return None


    def store(self, nomefile):
        """ salva su file il contenuto della rubrica secondo
        un opportuno formato (a scelta dello studente)"""
        # il formato da me scelto
        # prevede un contatto per linea
        # nome,cognome:telefono\n
        # Apro il file in output
        output_file = open(nomefile, 'w')
        # Ciclo sui record della rubrica
        for nome_cognome, numero in self.rub.items():
        # Li scrivo nel file secondo il formato "nome,cognome:telefono\n"
            output_file.write(nome_cognome + ':' + str(numero) + "\n")

        # Chiudo il file
        output_file.close()



    def ordina(self, crescente=True):
        """ serializza su stringa il contenuto della rubrica come in
            Nannipieri Felice 32255599\n
            Neri Paolo 347555776\n
            Rossi Mario 3478999\n
            Rossi Mario Romualdo 3475599\n
            Tazzini Tazzetti Gianna 33368999\n
            le chiavi ordinate lessicograficamente per Cognome -- Nome
            in modo crescente (True) o decrescente (False)
            Fra nome, cognome e telefono seve essere presente ESATTAMENTE uno spazio
            Restituisce la stringa prodotta """

        # Stringa prodotta da restituire in output
        output = ""
        #Creo una Lista con i record da ordinare
        rubrica_ordinata = []  # [... (cognome, nome, numero_telefono), ...]
        # Aggiungiamo alla lista i record, anteponendo il cognome al nome
        for nome_cognome, numero in self.rub.items():
            data = nome_cognome.split(',')  # data[0] == nome, data[1] == cognome
            #nell'appendere i dati alla lista , uso la funzione title per renderli maiuscoli
            rubrica_ordinata.append((data[1].title(), data[0].title(), numero))
        # Ordiniamo la lista seguendo il criterio specificato nel parametro <crescente>
        #reverse ha un parametro true inverso al true in entrata, quindi lo nego.
        rubrica_ordinata.sort(reverse=(not crescente))
        # Serializziamo la lista seguendo il formato desiderato
        for record in rubrica_ordinata:
                       output += record[0] + ' ' + record[1] + ' ' + str(record[2]) + "\n"
        # Ritorniamo la stringa prodotta
        return output

