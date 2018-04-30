import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

counts = dict()
for line in file_handle:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
l = [(v, k) for k, v in counts.items() if v > 2]
for i in l:
    print(i)