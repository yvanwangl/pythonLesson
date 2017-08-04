import pickle

# user = dict(name='wangyafei', age=22)
# with open('writeFiles/pickTemp.txt', 'wb') as f:
#     pickle.dump(user, f)

with open('writeFiles/pickTemp.txt', 'rb') as f:
    print(pickle.load(f))
