import time
from concurrent.futures import ThreadPoolExecutor
import threading

def viewThread(n):
    print(f"Thread {n} Started")
    print(f"Accessing thread {n} : {threading.get_ident()}")
    print(f"Thread {n} Execution Complete {threading.current_thread()}")

def main():
    executor = ThreadPoolExecutor(max_workers=3)
    tA = executor.submit(viewThread,1)
    time.sleep(2)
    tB = executor.submit(viewThread,2)
    time.sleep(2)
    tC = executor.submit(viewThread,3)

if __name__ == '__main__':
    main()




from concurrent.futures import ThreadPoolExecutor
import threading

from functools import reduce

def fibonacci(n):
    print(f"Sequence {n} Started: {threading.get_ident()}")
    fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])
    print(fibs)
    print(f"Sequence {n} Completed: {threading.current_thread()}")

def cazzabubbolo(n):
    print(f'ah, ma {n} è ronco!')

def main():
    executor = ThreadPoolExecutor(max_workers=3)
    tA = executor.submit(fibonacci,5)
    tB = executor.submit(fibonacci,7)
    tC = executor.submit(fibonacci,6)
    tD =executor.submit(cazzabubbolo,233)

if __name__ == '__main__':
    main()