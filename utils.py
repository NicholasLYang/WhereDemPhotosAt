
import urllib2, json
fKey = '20dd8b0f53a96c73c31c2f9ec7a22c9f'

def searchPhotos(number, tag, latitude, longitude):
# Takes the number of photos, the Flickr api key, the tag and a location, then returns a list of dictionaries with the format 'title':title, 'photo_id':photo_id, 
    method = 'flickr.photos.search'
    uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&has_geo=1&method=%s&per_page=%s&api_key=%s&tag=%s&lat=%s&lon=%s'
    url = uri%(method, number, fKey, tag, latitude, longitude)
    request = urllib2.urlopen(url)
    result = request.read()
    translated = json.loads(result)
    out = []
    for key in translated['photos']['photo']:
        a = {}
        a['user'] = key['owner']
        a['photo_id'] = key['id']
        a['title'] = key['title']
        out.append(a)
    return out

def findLocation(a):
# Takes the list from function above and returns list of dictionaries with format 'title':title, 'longitude':longitude, 'latitude':latitude
    method = 'flickr.photos.geo.getLocation'
    uri = 'https://api.flickr.com/services/rest/?format=json&nojsoncallback=1&method=%s&api_key=%s&photo_id=%s'
    out = []
    for photo in a:
        photo_id = photo['photo_id']
        url = uri%(method, fKey, photo_id)
        request = urllib2.urlopen(url)
        result = request.read()
        translated = json.loads(result)
        d = {}
        d['longitude'] = translated['photo']['location']['longitude']
        d['latitude'] = translated['photo']['location']['latitude']
        d['title'] = photo['title']
        out.append(d)
    return out
