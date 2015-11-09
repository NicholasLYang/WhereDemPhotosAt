import urllib2, json
import utils
key = '20dd8b0f53a96c73c31c2f9ec7a22c9f'
latitude = '40.8073270'
longitude = '-73.9669800'
tag = 'zamansky'
a = utils.searchPhotos(2, tag, latitude, longitude)
print a
b = utils.findLocation(a)
print b