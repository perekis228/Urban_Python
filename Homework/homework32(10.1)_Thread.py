from threading import Thread
import time

def printing(start):
    for i in range(start, start+10):
        if start > 96:
            print(chr(i), flush=True)
        else:
            print(i, flush=True)
        time.sleep(1)


thread = Thread(target=printing, kwargs=dict(start=1))
thread.start()

printing(97)
thread.join()