import re
from socket import *
from multiprocessing import Process


def clTool(cl_socket,cl_addr):
    #接受客户端发送的HTML报文信息
    request_data = cl_socket.recv(1024)
    request_data = request_data.decode("utf-8")
    print("request data:\r\n", request_data)
    # 解析报文数据
    list_all_data = request_data.split("\r\n")
    # 提取请求方式
    #print("第一行%s"%list_all_data[0])
    list_firt_line = re.split(r"[\s]+",list_all_data[0])
    if "GET" in list_firt_line:
        # 返回服务器页面信息
        start_line_response = "HTTP/1.1 200 OK\r\n"
        headers_response = "Server: My Server\r\n"
        body_response = "hello world"
        response = start_line_response + headers_response + "\r\n" + body_response
        print("response data:\r\n",response)
        cl_socket.send(response.encode("utf-8"))
        cl_socket.close()

# 创建服务器端socket
sv_socket = socket(AF_INET,SOCK_STREAM)
sv_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sv_addr = ("",6686)
sv_socket.bind(sv_addr)
sv_socket.listen(5)
#print("----1----")
while True:
    #print("----2----")
    # 获取已连接的客户端信息
    cl_socket, cl_addr = sv_socket.accept()
    print("客户端地址：",str(cl_addr))
    cl_process = Process(target=clTool, args=(cl_socket,cl_addr))
    cl_process.start()
    cl_process.join()
    cl_socket.close()

