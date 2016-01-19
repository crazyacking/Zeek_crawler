#常用的文件操作总结
#
# file=open('/home/crazyacking/Code_Fantasy/Zeek_crawler/webfile/cnblogs.html','r',1)
#open(文件路径,读写模式,是否使用缓存)
# content=file.readline()
# content=file.readlines()
# content=file.read(10) #指定读取多少个字节
# # file.write("Hello World")
# # file.writelines()
# file.seek(10) #随机访问,10表示偏移量(从第10个字符开始)
# for i in range(3):
#     print(i,file.readline())
#
# for i in range(3):
#     print(file.readline(),end='')
#
# file.close()

#语句结束后自动关闭文件
# with open('/home/crazyacking/Code_Fantasy/Zeek_crawler/webfile/cnblogs.html','r',1) as file:
    # pass
    # do something
    # print(file.read())

# -------------------------------------------
#对文件内容进行迭代
# import sys

# def process(string):
#     print("process:",string)
#
# file=open('/home/crazyacking/Code_Fantasy/Zeek_crawler/webfile/test.txt','r',1)

# way 1
# ch=file.read(1)
# while ch:
#     process(ch)
#     ch=file.read(1)

# while True:
#     ch=file.read(1)
#     if not ch:
#         break
#     #do something
#     # process(ch)
#     ch=file.read(1)

#对行进行迭代
# while True:
#     line=file.readline()
#     if not line:
#         break
#     #do something
#     process(line)
#     line=file.readline()

#对每一个字符进行迭代
# content=file.read()
# for ch in content:
#     process(ch)


#使用fileinput迭代
# import fileinput
# for line in fileinput.input('/home/crazyacking/Code_Fantasy/Zeek_crawler/webfile/test.txt',False,'',0,'r'):
#     process(line)

# 按行迭代
# for line in file:
#     process(line)

#对标准输入进行迭代
# for line in sys.stdin:
#     print(line)

# file.close()