from threading import Thread
from socket import *
udpSocket = None
def recvData():
    while True:
        recv_infor = udpSocket.recvfrom(1024)
        print("\r>>%s:%s\n<<"%(str(recv_infor[1]),recv_infor[0].decode("gb2312")),end="")
def sendData():
    ip = input("请输入IP地址：")
    port = input("请输入端口号：")
    addr = (ip,int(port))
    while True:
        send_infor = input("<<")
        udpSocket.sendto(send_infor.encode("gb2312"),addr)
def main():
    print("00")
    global udpSocket
    udpSocket = socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("",7667))
    print("0")
    tr = Thread(target=recvData)
    ts = Thread(target=sendData)
    print("1")
    tr.start()
    ts.start()
    tr.join()
    ts.join()
if __name__=="__main__":
    main()
