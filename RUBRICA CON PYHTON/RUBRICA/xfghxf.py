from threading import Thread
import time

def print_time(name, ritardo):
    for i in range(5):
        time.sleep(ritardo)
for i in range(6):
    thread = Thread(name= 'producer',target= print_time,args = ( ,2))
    thread.start()
    thread.join()
