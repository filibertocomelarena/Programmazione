from threading import Thread #importa i moduli
from threading import Condition
from threading import RLock
from queue import Queue
import random
import time



queue = Queue(maxsize=3) #coda condivisa
lock = RLock()
cond = Condition()


class Producer(Thread):
    def run(self):
        numero = range(5) #numero in range 5
        global queue
        global cond
        while True:
            num = random.choice(numero) #prendo un numero casuale tra numeri
            cond.acquire() #acquisisco la condition
            while queue.full(): #finchè la coda è piena
                cond.wait()#stai fermino
            queue.put(num)#sennò ci butti numero
            print('produced', num)#e dici che è stato prodotto
            cond.notifyAll()#poi svegli tutti senno rimangono fermi
            cond.release()#rilasci la condition solo dopo
            time.sleep(random.random())#tempo di sleep


class Consumer(Thread):
    def run(self):

        global queue
        global cond
        while True:
            cond.acquire() #acquistiamo la condition
            while queue.empty(): #finchè la cosa è vuota
                cond.wait() #sta bono
            numero = queue.get() #sennò si accede alla coda condivisa
            print('consumato', numero) #si printa che si è consumato
            cond.notifyAll() #si svegliano tutti i thread
            time.sleep(1) #si dorme


if __name__=='__main__':
    Producer().start() #avviare i thread
    Consumer().start()


