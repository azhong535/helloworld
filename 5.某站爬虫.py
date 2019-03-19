import urllib.request
import re
import os
foot='huaban001'
url_re=re.compile(r'<img src="(http://img4.26ts.com.+?\.jpg)"')
url='http://www.cthjt.com/article2gga?8625.html'

def url_open(url):
	html=urllib.request.urlopen(url).read()
	return html
def get_img_addrs(html):
	img_addrs=url_re.findall(html)
	img_addrs=list(set(img_addrs))
	return img_addrs

def save_img(img_addrs):
        x=0
        for imgurl in img_addrs:
                print (imgurl)
                urllib.request.urlretrieve(imgurl,"%s.jpg" %x)
                x+=1

def download_huaban_img():
        
	os.mkdir(foot)
	os.chdir(foot)
	html=url_open(url)
	img_addrs=get_img_addrs(html.decode('gbk'))
	save_img(img_addrs)

download_huaban_img()
