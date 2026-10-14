# Script di test Assegnamento 1 622AA 2020/21 (non modificare)
from rubrica import *

def testEqual(x,y):
    """ stampa l'esito del test e restituisce 0 se il test è stato passato
    e 1 se è stato fallito"""
    if x == y:
        print(" -> ", "Pass")
        return 0
    else:
        print(" -> ", "Expected: ", y," Got: ", x)
        return 1


def printR(r):
    """ stampa ausiliaria """
    print("inizio stampa --------------------------------")
    print(r)
    print("fine stampa --------------------------------")

def testRubrica():
    #contiamo i test falliti
    testFalliti=0
    print("==========> Inizio nuovo test <=============\n\n")
    # creo una rubrica
    p = Rubrica()
    # stampo la rubrica
    print("==========> Test stampa")
    printR(p)
    # test inserimento
    print("==========> Test inserimento")
    testFalliti += testEqual(p.inserisci("gigi", "rossi", 3456789), True)
    testFalliti += testEqual(p.inserisci("Gigi", "rossi", 3456789), False)
    testFalliti += testEqual(p.inserisci("mario", "rossi", 3478999), True)
    testFalliti += testEqual(p.inserisci("mario romualdo", "rossi", 3475599), True)
    testFalliti += testEqual(p.inserisci("mario romualdo", "rossi", 3475599), False)
    # test ricerca
    print("==========> Test cerca")
    testFalliti +=testEqual(p.cerca("gigi", "rossi"), 3456789)
    testFalliti +=testEqual(p.cerca("Dario", "Bianchi"), None)
    #test modifica
    print("==========> Test modifica")
    testFalliti +=testEqual(p.modifica("Dario", "Bianchi",4567890), False)
    testFalliti +=testEqual(p.modifica("gigi", "rossi",3478899776), True)
    testFalliti +=testEqual(p.modifica([1,3], "rossi",3478899776), False)
    testFalliti +=testEqual(p.cerca("gigi", "rossi"), 3478899776)
    #test store, load
    print("==========> Test load/store")
    p.store("___testfile1.txt")
    printR(p)
    q = Rubrica()
    q.load("___testfile1.txt")
    printR(q)
    r = Rubrica()
    testFalliti +=testEqual(r.inserisci("Paolo", "Neri", 347555776), True)
    testFalliti +=testEqual(r.inserisci("Gianna", "Tazzini Tazzetti", 33368999), True)
    testFalliti +=testEqual(r.inserisci("FELICE", "nannipieri", 32255599), True)
    r.store("___testfile2.txt")
    rr=Rubrica()
    rr.load("___testfile2.txt")
    printR(r)
    printR(rr)
    # test uguaglianza
    print("""==========> Test "==" """)
    testFalliti +=testEqual(r == rr, True)
    testFalliti +=testEqual(q is p, False)
    testFalliti +=testEqual(q==p,True)
    testFalliti +=testEqual(q is r, False)
    testFalliti +=testEqual(q == r, False)
    # test addizione
    print("""==========> Test "+" """)
    c = q+r
    printR(c)
    testFalliti +=testEqual(c.cerca("gigi", "rossi"), 3478899776)
    d = c+q
    testFalliti +=testEqual(d==c,True)
    #test cancella
    print("""==========> Test cancella """)
    testFalliti +=testEqual(d.cancella("gigi", "rossi"), True)
    testFalliti +=testEqual(d.cancella("gigi", "rossi"), False)
    testFalliti +=testEqual(d == c, False)
    #test ordina
    print("""==========> Test ordina crescente""")
    print(d.ordina(True))
    print("""==========> Test ordina decrescente""")
    print(d.ordina(False))
    testFalliti += testEqual(r.ordina(True)==rr.ordina(True),True)
    testFalliti += testEqual(r.ordina(False) == rr.ordina(False), True)
    # abbiamo finito ?
    if testFalliti == 0:
        print("\t****Test completati -- effettuare la consegna come da README")
    else:
        print("Test falliti: ",testFalliti)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testRubrica()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
