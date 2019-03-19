import urllib.request
import http.client
import bs4 
import re
import time
file_tieba=open('开店吧.txt','a+',encoding='utf-8')
pattern=re.compile('post_content_[0-9]{1,}')
pattern2=re.compile('\?pn=([0-9]{1,})\">尾页</a>')
pattern3=re.compile('<title>(.+?)</title>')
main='https://tieba.baidu.com/f?kw=%E8%90%8C%E6%88%98&ie=utf-8&pn='
def IsRightId(id):
             group=pattern.findall(id)
             if group:
                          
                          return group
                        
             else :
                          return None
def GetEveryPage(url,file,a):
    request = urllib.request.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \
        WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    try:  
        rep=urllib.request.urlopen(url)  
    except http.client.HTTPException as e:  
        print(repr(e))  
    else:  
        rep_utf=rep.read()
        soup=bs4.BeautifulSoup(rep_utf,'html.parser')
        
        for div in soup.find_all('div'):
                                      
                    div_id=div.get('id')  
                    if IsRightId(str(div_id)):
                                #print(div.get_text())
                                a+=1
                                s='第'+str(a)+'楼'                                  
                                file.write(s+'\r\n'+div.get_text()+'\r\n')  
#把贴吧帖子页中的页数提取出来
def changeip(pattern2,url):
    request = urllib.request.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \
        WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    rep_url=urllib.request.urlopen(url)
    rep=rep_url.read().decode('utf-8')
    group=pattern2.findall(rep)
    if  group==[]:
            tieshu=2
    elif int(group[0])<10:
            tieshu=int(group[0])+1
    elif int(group[0])>=6:
            tieshu=10
    return tieshu     
#把贴吧帖子页中的主题提取出来
def titleip(pattern2,url):
    request = urllib.request.Request(url)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \
        WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')    
    rep_url=urllib.request.urlopen(url)
    rep=rep_url.read().decode('utf-8')
    group=pattern2.findall(rep)
    f=str(group[0])
    return f

def fenxi(main,ye):
    mainurl=main+str(ye)
    request = urllib.request.Request(mainurl)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \
        WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')        
    yemian=urllib.request.urlopen(mainurl).read().decode('utf-8')
    url_re2=re.compile(r'<a href="/p/(.+)" title=".+?" target="_blank" class="j_th_tit "')
    shuzu=url_re2.findall(yemian)
    print(shuzu)
    return shuzu
#正文
for ye in range(0,500,50):
    shuzu=fenxi(main,ye)
    jie=1
    for shuzi in shuzu:
        #数字为贴吧主页提取的帖子数字 
        html='http://tieba.baidu.com/p/'+str(shuzi)+'?pn='
        file2=changeip(pattern2,html)
        file_tieba.write('\r\n\r\n'+'第'+str(jie)+'节  '+titleip(pattern3,html)+'\r\n\r\n')
        a=1
        jie+=1
        for i in range(1,file2): 
            url_everypage=html+str(i)
            print(url_everypage)
            print('Processing page:'+str(i)+'/'+str(file2-1)+'......')
            GetEveryPage(url_everypage,file_tieba,a)        
    print('第'+str(ye)+'行结束!')
file_tieba.close()
