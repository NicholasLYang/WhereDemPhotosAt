import urllib2, json
method = 'flickr.activity.userComments'
uri = 'https://api.flickr.com/services/rest/?method=%s'
url = uri%(method)

print url