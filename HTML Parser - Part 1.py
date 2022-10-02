# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name,value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name,value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
parser.close()
