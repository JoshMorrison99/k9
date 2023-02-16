import sys
from urllib.parse import urlparse, parse_qs

def main(urls):
    wordlist = set()
    for url in urls:
        url_parse = urlparse(url)
        if(url_parse.query):
            params = parse_qs(url_parse.query)
            if(params != '{}'):
                for param in params:
                    wordlist.add(param)
    for i in wordlist:
        print(i)

main(sys.stdin)
