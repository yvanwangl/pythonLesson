from collections import defaultdict

dd = defaultdict(lambda: 'NaN')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
