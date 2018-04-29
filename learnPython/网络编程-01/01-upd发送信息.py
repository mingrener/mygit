from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.sendto(b"hei",("192.168.1.14",8082))
