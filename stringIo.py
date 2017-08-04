from io import StringIO, BytesIO

# f = StringIO()
# print(f.write('hello'))
# print(f.write('world!'))


# read line use StringIO
# f = StringIO('Hi\nHello\nWorld')
# print(f.getvalue())
# while True:
#     line = f.readline()
#     if line == '':
#         break
#     print(line.strip())

# read line use BytesIO
# b = BytesIO()
# b.write('中文'.encode('utf-8'))
# print(b.getvalue())
# b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(b.read())


