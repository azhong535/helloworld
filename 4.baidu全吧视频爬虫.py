import urllib.request
import re
import os
import time
from bs4 import BeautifulSoup
import socket
import http.client
x=0
url_re=re.compile(r'data-video="(http://tb-video.bdstatic.com/.+?[\.jpg,\.png,\.gif,\.mp4,\.js])"')
pattern1=re.compile('\?pn=([0-9]{1,})\">尾页</a>')
pattern2=re.compile(r'<a href="/p/(.+)" title=".+?" target="_blank" class="j_th_tit "')
main='http://tieba.baidu.com/f?kw=%E7%B4%A0%E8%83%B8&ie=utf-8&pn='
def get_img_addrs(html):
	img_addrs=url_re.findall(html)
	img_addrs2=list(set(img_addrs))
	return img_addrs2
def download_huaban_img(url2,yeshu,x):   
        request = urllib.request.Request(url2)
        #模拟登陆，防服务器拒绝
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \
            WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
        try:
            html = urllib.request.urlopen(request)
        except socket.timeout:
            pass
        except urllib.request.URLError:
            pass
        except http.client.BadStatusLine:
            pass

        soup = BeautifulSoup(html,'html.parser')
        group=url_re.findall(str(soup))
        for div in group:
            time.sleep(0.3)
            print(div)
            urllib.request.urlretrieve(div,"%s-%s.Mp4" %(yeshu,x))
            x+=1
def tieip(main,ye,pattern1):
        group=fenxi(main,ye,pattern1)
        print(group)
        if  group==[]:
            tieshu=2
        elif int(group[0])<6:
            tieshu=int(group[0])+1
        elif int(group[0])>=6:
            tieshu=6
        return tieshu
def fenxi(main,ye,pattern):
        mainurl=main+str(ye)
        request = urllib.request.Request(mainurl)
        request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \
            WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')        
        yemian=urllib.request.urlopen(mainurl).read().decode('utf-8')
        shuzu=pattern.findall(yemian)
        return shuzu

#正文
foot='萌妹子'
if (os.path.exists(foot)):
        pass
else:
        os.mkdir(foot)       
os.chdir(foot) 
for ye in range(0,250,50):
        shuzu=fenxi(main,ye,pattern2)
        print(shuzu)
        for shuzi in shuzu:
                #数字为贴吧主页提取的帖子数字
                html='http://tieba.baidu.com/p/'+str(shuzi)+'?pn='
                file2=tieip(html,1,pattern1)
                x=1
                for i in range(1,file2): 
                        url_everypage=html+str(i)
                        print(url_everypage)
                        print('Processing page:'+str(i)+'/'+str(file2-1)+'......')
                        download_huaban_img(url_everypage,shuzi,x)




                      
