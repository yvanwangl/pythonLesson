from urllib.request import urlopen
import json
import pdb

tags_list = list()


def json_hook(obj):
    for key, value in obj:
        if key is 'tags':
            for v in value:
                tags_list.append(v)


with urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    # print('status:', f.status, f.reason)
    # for k, v in f.getheaders():
    #     print('%s: %s' % (k, v))
    json.loads(data.decode('utf-8'), object_hook=json_hook)


    print(tags_list)
    # print(f.read())
