from collections import OrderedDict

# d = dict([('a', 1), ('b', 2), ('c', 3)])
# print(d)
#
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)
# print(od.keys())
#
# for odKey in od.keys():
#     print(odKey)

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self)-contains_key >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if contains_key:
            del self[key]
            print('set:', (key, value))
        else:
            print('add', (key, value))
        OrderedDict.__setitem__(self, key, value)
