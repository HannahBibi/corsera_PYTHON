import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def assignment1(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    r_c = 0
    span_tags = soup('span')
    for line in span_tags:
        t = line.text
        i = int(t)
        r_c = r_c + i
    return r_c

def assignment2(url, rng, pos):
    text = ""
    u = url
    for i in range(rng):
        h = urllib.request.urlopen(u).read()
        soup2 = BeautifulSoup(h, 'html.parser')
        tag = soup2('a')
        text = tag[pos].text
        u = tag[pos].get('href', None)
    return text
