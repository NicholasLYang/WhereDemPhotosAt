import urllib2, json
import utils
fKey = '20dd8b0f53a96c73c31c2f9ec7a22c9f'
number = 2
latlng = {'lat':'40.8073270', 'lng':'-73.9669800'}
radius = 31
tag = 'zamansky'
method = 'flickr.photos.search'
uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&has_geo=1&method=%s&per_page=%s&api_key=%s&tag=%s&lat=%s&lon=%s&radius=%s'
url = uri%(method, number, fKey, tag, latlng['lat'], latlng['lng'], radius)
request = urllib2.urlopen(url)
result = request.read()
translated = json.loads(result)
print translated