import urllib
from urllib.request import urlopen

url = "https://passport.csdn.net/account/login"
values = {'username':'freehope_9@live.com','password':'freehope17453'}
data = urllib.parse.urlencode(values)
request = urllib.request.Request(url)
print(request)
with urlopen(request) as html:
    print(html.read())

