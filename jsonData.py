import json

user = dict(name='lihuan', age=20)


# with open('writeFiles/jsonTemp.txt', 'w') as f:
#     f.write(json.dumps(user))

# with open('writeFiles/jsonTemp.txt', 'w') as f:
#     json.dump(user, f)

# with open('writeFiles/jsonTemp.txt', 'r') as f:
#     print(json.load(f))

def student2json(s):
    return {
        'name': s.name,
        'age': s.age,
        'score': s.score
    }


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


student = Student('wangyafei', 23, 90)

sJson = json.dumps(student, default=lambda obj: obj.__dict__)


def json2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(sJson, object_hook=json2student).name)
