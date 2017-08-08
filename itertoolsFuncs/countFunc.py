import itertools

# for it in itertools.count(1):
#     print(it)

# for it in itertools.cycle('abc'):
#     print(it)

# for it in itertools.repeat('b'):
#     print(it)

# for it in itertools.repeat('b', 3):
#     print(it)

# for it in itertools.takewhile(lambda x: x <= 10, itertools.count(1)):
#     print(it)

# for it in itertools.chain('abc', 'xyz'):
#     print(it)

# for key, group in itertools.groupby('AaBBBcc'):
#     print(key, list(group))

for key, group in itertools.groupby('AaBBbCc', lambda x: x.upper()):
    print(key, list(group))
