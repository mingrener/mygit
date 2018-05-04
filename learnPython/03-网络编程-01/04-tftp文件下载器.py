#coding=utf-8
from socket import *
import struct
udpSocket = socket(AF_INET, SOCK_DGRAM)
udpSocket.bind(("",6777))
#在本机创建新的同名文件
file_name = input("请输入要下载的文件名：")
fd = open(file_name,"w")
#把文件名发给服务器
ip = input("请输入服务器的IP：")
port = 69
length = len(file_name)
send_infor = struct.pack("!H6sb5sb",1,file_name,0,"octet",0)
udpSocket.sendto(send_infor,(ip,port))
#向新文件中写入数据
while True:
    recv_data,recv_addr = udpSocket.recvfrom(1024)
    resl_recv = struct.unpack("!HH",recv_data[:4])

    if resl_recv[0] == 3:
        akc = struct.pack("!HH",4,resl_recv[1])
        udpSocket.sendto(akc,recv_addr)

        fd.write(recv_data[4:])
    if len(recv_data)<516:
        print("下载完毕")
        break
#关闭文件
fd.close()
udpSocket.close()

