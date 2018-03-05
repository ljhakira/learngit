import urllib2
cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
f = opener.open('http://www.xxxx.net/?act=login&name=user01')
data = '<root>Hello</root>'
request = urllib2.Request(
        url     = 'http://www.xxxx.net/?act=send',
        headers = {'Content-Type' : 'text/xml'},
        data    = data)
opener.open(request)
//nothing
//creat a new branch is quick

Creating a new branch is quick & simple.

