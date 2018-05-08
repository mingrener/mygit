import time


def application(env, start_reponse):

    status = "200 OK"
    headers = [
        ("Content-Type","text/html")
    ]
    start_reponse(status, headers)

    return time.ctime()