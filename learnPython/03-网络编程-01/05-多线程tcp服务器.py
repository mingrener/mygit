from socket import *
import threading
def subService(newS,clientAddr):
    while True:
        infor = newS.recv(1024)
        if len(infor)>0:
            print("[%s:%d]:%s"%(clientAddr[0],clientAddr[1],infor))
        else:
            print("[%s]客户端已关闭"%str(clientAddr))
            break
    newS.close()


s = socket(AF_INET,SOCK_STREAM)

s.bind(("",6677))
print("--1--")
s.listen(10)
print("--2--")

try:
    while True:
        print("--3--")
        newS,clientAddr = s.accept()
        print("--4--")
        t = threading.Thread(target=subService,args=(newS,clientAddr))
        t.start()
finally:
    s.close()


