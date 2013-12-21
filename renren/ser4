#!/usr/bin/python
import urllib
import urllib2
import cookielib
import time

headers={'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/20100824 Firefox/3.6.9'}
postdata= urllib.urlencode({"email":"hewr2010@gmail.com", "password":"22282633"})
url = "http://www.renren.com/PLogin.do";
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
req = urllib2.Request(url,postdata,headers)
res = urllib2.urlopen(req)
login_page = res.read()

cnt = 0
while True:
	req = urllib2.Request("http://blog.renren.com/blog/559111297/919263638")
	res = urllib2.urlopen(req)
	qjh_page = res.read()
	cnt += 1
	print cnt
	time.sleep(60)

