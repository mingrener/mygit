import re
from socket import *
from multiprocessing import Process
# 设置静态文件根目录
HMTL_ROOT_DIR = "./source"


class HTTPServer():
    """"""
    def __init__(self):
        self.sv_socket = socket(AF_INET, SOCK_STREAM)
        self.sv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def start(self):
        self.sv_socket.listen(5)
        # print("----1----")
        while True:
            # print("----2----")
            # 获取已连接的客户端信息
            cl_socket, cl_addr = self.sv_socket.accept()
            print("客户端：", str(cl_addr), "已连接上")
            cl_process = Process(target=self.cl_tool, args=(cl_socket,))
            cl_process.start()
            cl_process.join()
            cl_socket.close()

    def cl_tool(self,cl_socket):
        """处理客户端的请求"""
        # 接受并打印客户端发送的报文信息
        request_data = cl_socket.recv(1024)
        request_data = request_data.decode("utf-8")
        print("request data:\r\n", request_data)
        # 解析报文数据
        list_request_data = request_data.split("\r\n")
        request_firt_line = re.split(r"[\s]+", list_request_data[0])
        if "/" == request_firt_line[1]:
            # 如果客户端没有文件路径，则指定默认文件路径
            request_path = HMTL_ROOT_DIR + "/index.html"
        else:
            request_path = HMTL_ROOT_DIR + request_firt_line[1]
        try:
            # 读取文件中的数据
            print(request_path)
            f = open(request_path, "rb")
            file_data = f.read()
            f.close()
        except IOError:
            # 如果文件路径不存在，返回404状态
            start_line_response = "HTTP/1.1 404 Not Found\r\n"
            headers_response = "Server: My Server\r\n"
            body_response = "对不起，找不到该页面..."
        else:
            # 正常的相应数据
            start_line_response = "HTTP/1.1 200 OK\r\n"
            headers_response = "Server: My Server\r\n"
            body_response = file_data.decode("utf-8")
        # 返回响应数据
        response = start_line_response + headers_response + "\r\n" + body_response
        print("response data:\r\n", response)
        cl_socket.send(bytes(response,"utf-8"))
        cl_socket.close()

    def bind(self, port):
        sv_addr = ("", port)
        self.sv_socket.bind(sv_addr)

def main():
    http_server = HTTPServer()
    http_server.bind(6686)
    http_server.start()

if __name__ == "__main__":
    main()

