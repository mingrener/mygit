from multiprocessing import Pool, Manager
import os

def copyFile(name,oldFileName,newFileName,queue):
    fr = open(oldFileName+"/"+name)
    fw = open(newFileName+"/"+name,"w")
    text = fr.read()
    fw.write(text)
    fr.close
    fw.close
    queue.put(name)

def main():
    #获取源文件夹的名字
    oldFileName = input("请输入文件名：")
    #创建一个新的文件夹
    index = oldFileName.rfind("/")
    newFileName = oldFileName[(index+1):]+"-复件"
    os.mkdir(newFileName)

    #获取源文件夹的所有文件名
    listFileNames = os.listdir(oldFileName)



    #使用多进程拷贝文件
    pool = Pool(5)
    queue = Manager().Queue()

    for name in listFileNames:
        pool.apply_async(copyFile,args=(name,oldFileName,newFileName,queue))
    num = 0
    allNum = len(listFileNames)
    while True:
        queue.get()
        num+=1
        rate = num/allNum
        print("\rcopy的进度是：%.2f%%"%(rate*100),end="")
        if num == allNum:
            break
    print("\n")
    #pool.close()
    #pool.join()

if __name__ == "__main__":
    main()
