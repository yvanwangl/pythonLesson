def hello(name):
    print('hello ' + name)


class UserInfo(object):
    age = 5

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattr__(self, item):
        return self.item

    def __setattr__(self, key, value):
        self[key] = value

user = UserInfo('wangyafei', 22)
print(user.name)
user['name'] = 'lihuan'
print(user.name)
print(user.age)
print(UserInfo.age)
print('a' + '\t' + 'b')
