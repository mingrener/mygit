import time
from MyWebServer import HTTPServer

# 设置静态文件根目录
HMTL_ROOT_DIR = "./source"


class Application(object):
    def __init__(self, urls):
        self.urls = urls
    def __call__(self, env, start_response):
        path = env["path_infor"]
        # 静态地址："/static/"
        if path.startswith("/static/"):
            static_path = path[7:]
            if "/" == static_path:
                # 如果客户端没有文件路径，则指定默认文件路径
                request_path = HMTL_ROOT_DIR + "/index.html"
            else:
                request_path = HMTL_ROOT_DIR + static_path
            try:
                # 读取文件中的数据
                print(request_path)
                f = open(request_path, "rb")
                file_data = f.read()
                f.close()
            except IOError:
                # 如果文件路径不存在，返回404状态
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "Not Found"
            else:
                # 正常的响应数据
                status = "200 OK"
                headers = [
                    ("Content-Type", "text/html")
                ]
                start_response(status, headers)
                return file_data.decode("utf-8")

        for url,handler in urls:
            # 判断路由信息中是否有请求路径
            if url == path:
                return handler(env, start_response)
        # 如果不在路由信息中
        status = "404 Not Found"
        headers = []
        start_response(status,headers)
        return "Not Found"


def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type","text/html")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type","text/html")
    ]
    start_response(status, headers)
    return "hello Gong Zhiwei"

# urls指路由信息
urls = [
    ("/",show_ctime),
    ("/ctime.py",show_ctime),
    ("/sayhello.py",say_hello)
]

# if __name__ == "__main__":
app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(6686)
#     http_server.start()