import os
import time
ret = os.fork()
print(ret)
print("-"*30)
"""while True:"""
if ret==0:
    print("-----子进程---%d-%d--"%(os.getpid(),os.getppid()))
    time.sleep(1)
else:
    print("-----父进程---%d---"%os.getpid())
    time.sleep(1)
