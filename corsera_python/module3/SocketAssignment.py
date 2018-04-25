import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


def assignment1(url_lib, url):
    html = url_lib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    r_c = 0
    for line in soup('span'):
        t = line.text
        i = int(t)
        r_c = r_c + i
    return r_c


def assignment2(url_lib, url, rng, pos):
    text = ""
    u = url
    for i in range(rng):
        h = url_lib.request.urlopen(u).read()
        soup2 = BeautifulSoup(h, 'html.parser')
        tag = soup2('a')
        text = tag[pos].text
        u = tag[pos].get('href', None)
    return text
