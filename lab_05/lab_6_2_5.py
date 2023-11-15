import time
from queue import Queue
from threading import Thread
#from multiprocessing import Process, Queue, freeze_support


def worker(other_q, n):
    while True:
        item = other_q.get()
        if n == 1:
            pass
            time.sleep(0.5)
        elif n == 2:
            pass
            time.sleep(1)
        if item is None:
            break
        print("process data:", n, item)


q = Queue(2)
th1 = Thread(target=worker, args=(q, 1,))
th2 = Thread(target=worker, args=(q, 2,))
th1.start()
th2.start()

for i in range(50):
    print(f"put {i} inside q")
    q.put(i)

q.put(None)
q.put(None)


th1.join()
th2.join()

print("All is done")
