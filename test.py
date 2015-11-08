import urllib2, json
method = 'flickr.photos.geo.getLocation'
photoid = '21870769994'
key = '20dd8b0f53a96c73c31c2f9ec7a22c9f'
uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&method=%s&api_key=%s&photo_id=%s'
url = uri%(method, key, photoid)
request = urllib2.urlopen(url)
result = request.read()
# print result
translated = json.loads(result)
print translated['photo']['location']['longitude']