from multiprocessing import Process
import time
def test():
    while True:
        print("------test------")
        time.sleep(1)
ret = Process(target=test)
ret.start()
while True:
    print("------main----")
    time.sleep(1)
