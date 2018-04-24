try:
    print(num)
    
except SyntaxError:
    print("语法错误")
except Exception as ret:
    print("异常了，请处理。。。")
    print(ret)
else:
    print("-------没异常")
finally:
    print("----我不知道有没有异常-----")
print("--------dada------------")
