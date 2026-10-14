# Assegnamento 1  aa 2021-22 622AA modulo programmazione 9 crediti
# Gruppo:
# Filippo Rocchi  matricola: 495801 email: filipporocchi1991@gmail.com tel:3315064189

import logging
import threading
from queue import Queue

#configurazione del modulo logging
logging_format = "[%(levelname)s] (%(threadName)-10s) %(message)s"
logging.basicConfig(level=logging.INFO, format=logging_format)
#scrittura del log anche su file
file_handler = logging.FileHandler("log_rubrica.txt")
file_handler.setFormatter(logging.Formatter(logging_format))
logging.getLogger().addHandler(file_handler)

class Rubrica:
    """Costruttore: crea una rubrica vuota rappresentata come
    dizionario di contatti vuoto"""

    def __init__(self):
        """crea una nuova rubrica vuota"""  # creo le rubriche, saranno di classe rubrica (p,q,r,rr)
        self.rub = {}
        self.lock = threading.RLock()
        self.coda = Queue(maxsize=3) #lunghezza massima della coda
        self.cond = threading.Condition()

    def __str__(self):
        """Serializza una rubrica attraverso una stringa
        con opportuna codifica (a scelta dello studente)"""  # le rubriche verranno stampate con questa codifica
        # Creo una stringa vuota
        output = ""
        self.lock.acquire()
        # Ciclo su items in rub
        for nomecognome, numero in self.rub.items():
            # con stampa:  nome,cognome : 1234567890
            output += nomecognome + " : " + str(numero) + "\n"
        self.lock.release()
        return output

    def __eq__(self, r):
        """stabilisce se due rubriche contengono
        esattamente le stesse chiavi con gli stessi dati"""  # mette a confronto le rubriche che vengono create

        self.lock.acquire()  # prima rubrica
        r.lock.acquire()  # seconda rubrica

        # Controllo che le due rubriche abbiano la stessa lunghezza
        if len(self.rub) != len(r.rub):
            self.lock.release()
            r.lock.release()
            return False

        # Scorriamo i record della prima rubrica (self)
        for nome_cognome in self.rub.keys():
            # Per ognuno di essi, controllo se esso esista anche nella seconda rubrica (r)
            if nome_cognome in r.rub.keys():
                # Se lo trovo, controllo che anche il numero sia uguale
                if self.rub[nome_cognome] != r.rub[nome_cognome]:
                    # Se non lo e', le due rubriche sono diverse
                    self.lock.release()
                    r.lock.release()
                    return False
            else:
                # Se non c'e' proprio, allora le due rubriche sono diverse
                #rilascio la lock
                self.lock.release()
                r.lock.release()
                return False
        # Alla fine,se le altre condizioni non sono verificate, le due rubriche sono uguali
        self.lock.release()
        r.lock.release()
        return True

    def __add__(self, r):
        """crea una nuova rubrica unendone due (elimina i duplicati)
        e la restituisce come risultato --
        se ci sono contatti con la stessa chiave nelle due rubriche
        ne riporta uno solo"""
        # Creo una nuova rubrica vuota
        nuova_rubrica = Rubrica()
        # Copio per intero la prima rubrica (self) nella nuova rubrica
        self.lock.acquire()
        nuova_rubrica.rub = self.rub.copy()
        self.lock.release()

        # Copio i record dalla seconda rubrica (r) nella nuova rubrica
        r.lock.acquire()
        for chiave, valore in r.rub.items():
            # Se non esiste un record con la stessa chiave
            if not chiave in nuova_rubrica.rub.keys():
                # Lo inserisco
                nuova_rubrica.rub[chiave] = valore
        r.lock.release()

        # Ritorno la nuova rubrica
        return nuova_rubrica

    def load(self, nomefile):
        """carica da file una rubrica eliminando il
        precedente contenuto di self"""
        # formato del file: nome,cognome:telefono\n
        # apro il file e lo 'ripulisco'
        input_file = open(nomefile, "r")

        self.lock.acquire()
        self.rub.clear()
        self.lock.release()

        # leggo una linea del file e lo assegno a line
        line = input_file.readline()
        # dico che, fintanto che line non finisce, fintanto che non sara' None, in pratica:
        while line:
            # separo cognome nome e valori
            data = line.rstrip().split(":")  # data[0] == "nome,cognome", data[1] == "telefono"
            # separo ulteriormente nome e cognome
            nome_cognome = data[0].split(",")  # nome_cognome[0] == "nome", nome_cognome[1] == "cognome"
            # inserisco i dati ottenuti
            self.inserisci(nome_cognome[0], nome_cognome[1], data[1])
            line = input_file.readline()

        input_file.close()

    def inserisci(self, nome, cognome, dati):
        """inserisce un nuovo contatto con chiave (nome,cognome)
        restituisce "True" se l'inserimento e' andato a buon fine e "False"
        altrimenti (es chiave replicata) -- case insensitive"""
        # mi do una codifica dei dati in entrata
        nome = str(nome)
        cognome = str(cognome)
        dati = int(dati)
        # creo la chiave,ma minuscola, per il case insensitive
        chiavi = (nome + "," + cognome).lower()

        # Acquisiamo la lock sulla rubrica
        self.lock.acquire()

        # se la chiave no c'e':
        if chiavi not in self.rub.keys():
            # butto dentro il tutto
            self.rub[chiavi] = int(dati)
            self.lock.release()
            return True
        else:
            # altrimenti...
            self.lock.release()
            return False

    def modifica(self, nome, cognome, newdati):
        """modifica i dati relativi al contatto con chiave (nome,cognome)
        sostituendole con "newdati" -- restituisce "True" se la modifica
        e' stata effettuata e "False" altrimenti (es: la chiave non e' presente )"""
        # elimino il problema di inserimento: solo un tipo di dato consentito
        if type(nome) != str or type(cognome) != str:
            return False
        # creo la chiave da inserire
        chiave = nome + "," + cognome
        self.lock.acquire()
        if chiave in self.rub.keys():
            # se c'e' la aggiorno con un nuovo numero
            self.rub.update({chiave: newdati})
            self.lock.release()
            return True
        else:
            # altrimenti...
            self.lock.release()
        return False

    def cancella(self, nome, cognome):
        """il contatto con chiave (nome,cognome) esiste lo elimina
        insieme ai dati relativi e restituisce True -- altrimenti
        restituisce False"""
        # creo la chiave
        chiave = nome + "," + cognome
        # verifico se essa esiste nel dizionario
        #stesso procedimento : lock/release
        self.lock.acquire()
        for i in self.rub.keys():
            if chiave == i:
                # se c'e', la elimino:
                self.rub.pop(i)
                self.lock.release()
                return True
            else:
                self.lock.release()
                return False

    def cerca(self, nome, cognome):
        """restitusce i dati del contatto se la chiave e' presente
        nella rubrica e "None" altrimenti -- case insensitive"""
        # codifico i dati
        nome = str(nome)
        cognome = str(cognome)
        chiave = nome + "," + cognome
        # se la chiave e' presente la restituisco
        self.lock.acquire()
        if chiave in self.rub:
            dati = self.rub[chiave]
            self.lock.release()
            return dati
        self.lock.release()
        return None

    def store(self, nomefile):
        """salva su file il contenuto della rubrica secondo
        un opportuno formato (a scelta dello studente)"""
        # il formato da me scelto
        # prevede un contatto per linea
        # nome,cognome:telefono\n
        # Apro il file in output
        output_file = open(nomefile, "w")
        # Ciclo sui record della rubrica
        self.lock.acquire()
        for nome_cognome, numero in self.rub.items():
            # Li scrivo nel file secondo il formato "nome,cognome:telefono\n"
            output_file.write(nome_cognome + ":" + str(numero) + "\n")

        self.lock.release()
        # Chiudo il file
        output_file.close()

    def ordina(self, crescente=True):
        """serializza su stringa il contenuto della rubrica come in
        Nannipieri Felice 32255599\n
        Neri Paolo 347555776\n
        Rossi Mario 3478999\n
        Rossi Mario Romualdo 3475599\n
        Tazzini Tazzetti Gianna 33368999\n
        le chiavi ordinate lessicograficamente per Cognome -- Nome
        in modo crescente (True) o decrescente (False)
        Fra nome, cognome e telefono seve essere presente ESATTAMENTE uno spazio
        Restituisce la stringa prodotta"""

        # Stringa prodotta da restituire in output
        output = ""
        # Creo una Lista con i record da ordinare
        rubrica_ordinata = []  # [... (cognome, nome, numero_telefono), ...]

        # Aggiungiamo alla lista i record, anteponendo il cognome al nome
        self.lock.acquire()
        for nome_cognome, numero in self.rub.items():
            data = nome_cognome.split(",")  # data[0] == nome, data[1] == cognome
            # nell'appendere i dati alla lista , uso la funzione title per renderli maiuscoli
            rubrica_ordinata.append((data[1].title(), data[0].title(), numero))
        self.lock.release()

        # Ordiniamo la lista seguendo il criterio specificato nel parametro <crescente>
        # reverse ha un parametro true inverso al true in entrata, quindi lo nego.
        rubrica_ordinata.sort(reverse=(not crescente))
        # Serializziamo la lista seguendo il formato desiderato
        for record in rubrica_ordinata:
            output += record[0] + " " + record[1] + " " + str(record[2]) + "\n"

        # Ritorniamo la stringa prodotta
        return output

    def suggerisci(self, nome, cognome):
        """Il metodo suggerisci viene invocato da un thread per effettuare un suggerimento di un contatto nella rubrica.
        Prende come parametro il nome ed il cognome del contatto e lo inserisce in una coda (di lunghezza massima 3).
        Non si puo' inserire un elemento nella coda se la coda e' piena."""
        self.cond.acquire()

        #finchè la coda è piena...
        while self.coda.full():
            #aspetto che si liberi un posto
            self.cond.wait()  # Internamente, rilascia la lock
        #aggiungo un elemnto in coda
        self.coda.put((nome, cognome))

        self.cond.notify_all() #notifico i thread in attesa
        self.cond.release()

    def suggerimento(self):
        """Il metodo suggerimento viene invocato da un thread per ottenere un suggerimento recuperato dalla rubrica.
        Il thread legge gli elementi presenti in una coda di lunghezza 3. Se la coda e' vuota, attende l'inserimento di
        un elemento, altrimenti prende il primo elemento della coda e lo stampa."""

        self.cond.acquire()
        #finchè la coda è vuota aspetto un produttore che inserisce un elemento...
        while self.coda.empty():
            self.cond.wait()
        #recupero un suggerimento dalla coda
        record = self.coda.get()
        #stampo a video il suggerimento
        logging.info(record[0] + " " + record[1])
        self.coda.task_done() #informo la coda del termine dell'operazione

        self.cond.notify_all()
        self.cond.release()
