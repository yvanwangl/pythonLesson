from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib.request import urlopen
from contextlib import closing


class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHtmlParser()
with closing(urlopen('https://blog.yvanwang.com')) as page:
    for line in page:
        lineParser = parser.feed(line.decode('utf-8'))
        print(lineParser if lineParser is not None else '')
        # print(line)
