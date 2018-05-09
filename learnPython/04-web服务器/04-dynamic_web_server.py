import sys
import re
from socket import *
from multiprocessing import Process
# 设置静态文件根目录
HMTL_ROOT_DIR = "./source"
WSGI_PYTHON_DIR = "./wsgipython"
sys.path.insert(0,WSGI_PYTHON_DIR)

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
            client_socket, cl_addr = self.sv_socket.accept()
            print("客户端：", str(cl_addr), "已连接上")
            cl_process = Process(target=self.client_tool, args=(client_socket,))
            cl_process.start()
            cl_process.join()
            client_socket.close()

    def start_response(self, status, headers):
        self.start_line_response = "HTTP/1.1 " + status + "\r\n"
        self.headers_response = ""
        for header in headers:
            self.headers_response += "%s:%s\r\n"%header


    def client_tool(self,client_socket):
        """处理客户端的请求"""
        # 接受并打印客户端发送的报文信息
        request_data = client_socket.recv(1024)
        request_data = request_data.decode("utf-8")
        print("request data:\r\n", request_data)
        # 解析报文数据
        list_request_data = request_data.split("\r\n")
        request_firt_line = re.split(r"[\s]+", list_request_data[0])
        # 判断请求文件名是否".py"结尾
        if request_firt_line[1].endswith(".py"):
            try:
                # 动态导入请求的模块
                m = __import__((request_firt_line[1])[1:-3])
                # env是wsgi规定的变量，保存所有请求头的参数
                env = {}
                # 调用wsgi规定的application接口函数
                body_response = m.application(env, self.start_response)
            except Exception:
                # 如果请求的模块名输入错误，返回404状态码
                self.start_line_response = "HTTP/1.1 404 Not Found\r\n"
                self.headers_response = ""
                body_response = "Not Found"
            finally:
            # 组装响应数据
                response = self.start_line_response + self.headers_response +"\r\n" + body_response
        else:
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
                # 正常的响应数据
                start_line_response = "HTTP/1.1 200 OK\r\n"
                headers_response = "Server: My Server\r\n"
                body_response = file_data.decode("utf-8")
            # 组装成响应数据
            response = start_line_response + headers_response + "\r\n" + body_response
        print("response data:\r\n", response)
        # 返回响应数据
        client_socket.send(bytes(response,"utf-8"))
        client_socket.close()

    def bind(self, port):
        sv_addr = ("", port)
        self.sv_socket.bind(sv_addr)

def main():
    http_server = HTTPServer()
    http_server.bind(6686)
    http_server.start()

if __name__ == "__main__":
    main()

