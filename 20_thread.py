# https://docs.python.org/3/library/threading.html#thread-objects
# https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
# https://pymotw.com/2/threading/ << Thin one
import threading
import time

def worker(num):
    """thread worker function"""
    time.sleep(5)
    print("Worker: ",num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for i in range(5):
    threads[i].join()