import os
for i in range(10):
    name = "python大师_%d"%i
    f = open(name, "w")
    f.close
file_list = os.listdir()
for temp in file_list:
        os.rename(temp,"[志伟出品]-%s"%temp)

