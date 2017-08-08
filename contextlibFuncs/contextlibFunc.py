from contextlib import contextmanager, closing
from urllib.request import urlopen

# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s' % self.name)
#
# with Query('wangyafei') as q:
#     print(q.query())

# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s' % self.name)
#
#
# @contextmanager
# def create_query(name):
#     print('Begin')
#     yield Query(name)
#     print('End')
#
#
# with create_query('lihuan') as q:
#     q.query()


# @contextmanager
# def print_h(name):
#     print('<%s>' % name)
#     yield
#     print('</%s>' % name)
#
#
# with print_h('h1') as p:
#     print('Hello')
#     print('World!')


with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
