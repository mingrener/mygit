from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(("",4332))
recv = udpSocket.recvfrom(1024)
print("%s:%s"%(str(recv[1],recv[0])))
