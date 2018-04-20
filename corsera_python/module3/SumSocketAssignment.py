import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def running_count(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    r_c = 0
    span_tags = soup('span')
    for line in span_tags:
        t = line.text
        i = int(t)
        r_c = r_c + i
    return r_c
