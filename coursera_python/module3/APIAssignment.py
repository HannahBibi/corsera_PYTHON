import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

address = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters.')

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js, indent=2))

r_list = js["results"]
first_in_list = r_list[0]
place_id = first_in_list['place_id']

print(place_id)
