import json
import urllib.request
import urllib.error


html = str(input('Please input URL here: '))
url = urllib.request.urlopen(html).read()
running_count = 0
info = json.loads(url)

vals = info['comments']

for item in vals:
    c = item['count']
    running_count = running_count + c

print(running_count)
