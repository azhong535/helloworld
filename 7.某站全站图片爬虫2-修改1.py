import urllib.request
import re
import os
import time
url_re=re.compile(r'img data-original="(http:.+?\.jpg)"')
def url_open(url):
	html=urllib.request.urlopen(url).read()
	return html
def get_img_addrs(html):
	img_addrs=url_re.findall(html)
	img_addrs=list(set(img_addrs))
	return img_addrs
def download_huaban_img():
        b=534075
        x=0
        foot='F:\某站点全部图片'  
        if (os.path.exists(foot)):

                pass
        else:
                os.mkdir(foot)
        os.chdir(foot) 
        while(b<5296100):
                url="http://www.mcc676.com/article-show-id-"+str(b)+'.html'
                print(b)
                b+=1
                html=url_open(url)
                img_addrs=get_img_addrs(html.decode('utf-8'))
                for imgurl in img_addrs:
                        print (imgurl)
                        time.sleep(0.3)
                        urllib.request.urlretrieve(imgurl,"%s-%s.jpg" %(b-1,x))
                        x+=1         
download_huaban_img()
#由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。52809
