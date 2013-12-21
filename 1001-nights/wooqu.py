#!/usr/bin/python
import urllib
import urllib2
import cookielib
import time

headers={'User-Agent':'Mozilla/5.0 (Windows;U;Windows NT 5.1;zh-CN;rv:1.9.2.9)Gecko/20100824 Firefox/3.6.9'}
postdata= urllib.urlencode({"username":"hewr1993", "password":"95259378"})
url = "https://www.wooqu.org/user/login";
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
req = urllib2.Request(url,postdata,headers)
res = urllib2.urlopen(req)
login_page = res.read()

cnt = 0
while True:
	f = open("info.txt")
	actID = f.readline()[0:-1]
	realName = f.readline()[0:-1]
	Class = f.readline()[0:-1]
	phoneNumber = f.readline()[0:-1]
	studentID = f.readline()[0:-1]
	addon = f.readline()[0:-1]

	postdata= urllib.urlencode({"actID":actID, "realName":realName, "class":Class, "phoneNumber":phoneNumber, "studentID":studentID, "addon":addon})
	url = "https://www.wooqu.org/activity/signupact"
	req = urllib2.Request(url, postdata, headers)
	res = urllib2.urlopen(req)
	wooqu_page = res.read()
	cnt += 1
	print "[%d] %s" % (cnt, wooqu_page)
	time.sleep(3)

