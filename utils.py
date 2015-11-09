
import urllib2, json
fKey = '20dd8b0f53a96c73c31c2f9ec7a22c9f'

def searchPhotos(number, tag, latitude, longitude):
# Takes the number of photos, the Flickr api key, the tag and a location, then returns a dictionary with the format 'userid':'photoid'
    method = 'flickr.photos.search'
    uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&has_geo=1&method=%s&per_page=%s&api_key=%s&tag=%s&lat=%s&lon=%s'
    url = uri%(method, number, fKey, tag, latitude, longitude)
    request = urllib2.urlopen(url)
    result = request.read()
    translated = json.loads(result)
    a = {}
    for key in translated['photos']['photo']:
        l = [key['owner'], key['id']]
        a[key['title']] = l
    return a

def findLocation(a):
# Takes the dictionary from function above and returns location        
    method = 'flickr.photos.geo.getLocation'
    uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&method=%s&api_key=%s&photo_id=%s'
    out = {}
    for key in a:
        photoid = a[key][1]
        url = uri%(method, fKey, photoid)
        request = urllib2.urlopen(url)
        result = request.read()
        translated = json.loads(result)
        list = [translated['photo']['location']['longitude'], translated['photo']['location']['latitude']]
        out[key] = list
    return out
