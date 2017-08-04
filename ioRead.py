# try:
#     f = open('temps.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 读取文件内容
# with open('temp.txt', 'r') as f:
#     print(f.read())

# read file in lines, return a list
# with open('readFiles/temp.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# read binary file , read mode 'rb'
# with open('readFiles/image.png', 'rb') as f:
#     print(f.read())


# read file with encoding config, such as gbk
# with open('readFiles/gbk.txt', 'r', encoding='gbk', errors='ignore') as f:
#     print(f.read())

# write file
with open('writeFiles/writeTemp.txt', 'w') as f:
    print(f.write('test content'))
