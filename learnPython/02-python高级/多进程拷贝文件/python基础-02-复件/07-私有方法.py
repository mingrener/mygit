class phone:
    def __get_message(self):
        return "----发送短信-----"
    def send_massage(self, money):
        if money>100:
            msg = self.__get_message()
        else:
            msg = "余额不足，请先充值..."
        print(msg)


xiaomi = phone()
xiaomi.send_massage(200)
xiaomi.send_massage(20)

