import sys
import re
from socket import *
from multiprocessing import Process


class HTTPServer():
    """"""
    def __init__(self, application):
        self.sv_socket = socket(AF_INET, SOCK_STREAM)
        self.sv_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = application

    def start(self):
        self.sv_socket.listen(5)
        while True:
            # 获取已连接的客户端信息
            cl_socket, cl_addr = self.sv_socket.accept()
            print("客户端：", str(cl_addr), "已连接上")
            cl_process = Process(target=self.cl_tool, args=(cl_socket,))
            cl_process.start()
            cl_process.join()
            cl_socket.close()

    def start_response(self, status, headers):
        self.start_line_response = "HTTP/1.1 " + status + "\r\n"
        self.headers_response = ""
        for header in headers:
            self.headers_response += "%s:%s\r\n"%header


    def cl_tool(self,cl_socket):
        """处理客户端的请求"""
        # 接受并打印客户端发送的报文信息
        request_data = cl_socket.recv(1024)
        request_data = request_data.decode("utf-8")
        print("request data:\r\n", request_data)
        # 解析报文数据
        list_request_data = request_data.split("\r\n")
        request_firt_line = re.split(r"[\s]+", list_request_data[0])
        path = request_firt_line[1]
        # env是wsgi规定的变量，保存所有请求头的参数
        env = {
            "path_infor":path
        }
        # 调用wsgi规定的application接口函数
        body_response = self.app(env, self.start_response)
        # 组装成响应数据
        response = self.start_line_response + self.headers_response + "\r\n" + body_response
        print("response data:","\r\n", response)
        # 返回响应数据
        cl_socket.send(bytes(response,"utf-8"))
        cl_socket.close()

    def bind(self, port):
        sv_addr = ("", port)
        self.sv_socket.bind(sv_addr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Input Python MyWebServer.py module_name:application_name")
    module_name, application_name = sys.argv[1].split(":")
    m = __import__(module_name)
    app = getattr(m, application_name)
    http_server = HTTPServer(app)
    http_server.bind(6686)
    http_server.start()