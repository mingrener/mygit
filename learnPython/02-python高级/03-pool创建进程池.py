from multiprocessing import Pool
import time
import os

def worker():
    for i in range(5):
        print("==pid=%d======="%os.getpid())
        time.sleep(2)
po = Pool(3)
for i in range(10):
    print("------%d-------"%i)
    po.apply_async(worker)
    time.sleep(2)
po.close()
po.join()
