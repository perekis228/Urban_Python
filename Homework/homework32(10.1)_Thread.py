from threading import Thread
import time

def printing(start):
    for i in range(start, start+10):
        if start > 96:
            print(chr(i), flush=True)
        else:
            print(i, flush=True)
        time.sleep(1)


thread1 = Thread(target=printing, kwargs=dict(start=1))
thread2 = Thread(target=printing, kwargs=dict(start=97))
thread1.start()
thread2.start()

thread1.join()
thread2.join()
