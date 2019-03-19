import urllib.request
import http.client
import http.cookiejar
import bs4 
import re
import time
from lxml import etree
from urllib.parse import quote
import sys
import getpass
file_tieba=open('关于你好.txt','a+',encoding='gbk')
pattern=re.compile('http://zhidao.baidu.com/question/(.+?.html)\?')
pattern2=re.compile('<span class="ask-title ">(.+?)</span>')
pattern3=re.compile('ask-title ')
pattern4=re.compile('con')
wenti='你好'
s_utf=quote(wenti.encode("gbk") )

main='https://zhidao.baidu.com/search?word='+s_utf+'&ie=gbk&site=-1&sites=0&date=0&pn='
def IsRightId(id):
             group=pattern.findall(id)
             if group:
                          
                          return group
                        
             else :
                          return None

def fenxi(main,ye):
    mainurl=main+str(ye)
    cj = http.cookiejar.CookieJar()                                                
    handler = urllib.request.HTTPCookieProcessor(cj)                               
    opener = urllib.request.build_opener(handler)                                  
    urllib.request.install_opener(opener)
    
    request = urllib.request.Request(mainurl)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    yemian=urllib.request.urlopen(mainurl).read().decode('gbk')
     
    return yemian
#把字符集合并成字符串
def dai(daiyu):
    b=''
    for fuli in daiyu:
        b+=fuli
    return b
#正文获取当前cook
#把当前页地址解析成地址数组集
for ye in range(0,600,10):
    yemian=fenxi(main,ye)
    soup=bs4.BeautifulSoup(yemian,'html.parser') 
    jie=1
    shuzu=[]
    for div in soup.find_all('a'):
        div_id=div.get('href')
        if IsRightId(div_id):
            shuzu+=IsRightId(div_id)           
    print(shuzu)
    for shuzi in shuzu:

        #数字为贴吧主页提取的帖子数字
        wangzhi="https://zhidao.baidu.com/question/"+shuzi
        file_tieba.write('\r\n'+wangzhi+'\r\n')
        
        file2=fenxi(wangzhi,None)
        selector = etree.HTML(file2)
        title= selector.xpath('//span[@class="ask-title "]/text()')
        print(title)
        miaosuji= selector.xpath('//div[@class="line mt-5 q-content"]/span[@class="con"]/text()')
        goodji= selector.xpath('//pre[@class="best-text mb-10"]/text()')
        shijian=selector.xpath('//span[@class="grid-r f-aid pos-time answer-time f-pening"]/text()')
        otherji= selector.xpath('//div[@class="answer-text line"]/span[@class="con"]/text()')
        zuiwen=selector.xpath('//pre[@class="qRA"]/text()')
        zuida=selector.xpath('//pre[@class="aRA"]/text()')
        miaosu=dai(miaosuji)
        good=dai(goodji)
        other=dai(otherji)
        if  miaosuji==[] and goodji==[]:
            file_tieba.write('\r\n\r\n'+'第'+str(jie)+'章  问:'+title[0])
        elif miaosuji==[] and goodji !=[]:
            file_tieba.write('\r\n\r\n'+'第'+str(jie)+'章  问:'+title[0]+'\r\n最佳答案：'+good+shijian[0])
        elif miaosuji !=[] and goodji ==[]:
            file_tieba.write('\r\n\r\n'+'第'+str(jie)+'章  问:'+title[0]+'\r\n问题描述：'+miaosu+'\r\n')
        else:
            file_tieba.write('\r\n\r\n'+'第'+str(jie)+'章  问:'+title[0]+'\r\n问题描述： '+miaosu+'\r\n最佳答案：'+good+shijian[0])
        file_tieba.write('答：'+other)
        jie+=1
        zonghe=zuiwen+zuida
        for dayin in zonghe:
            file_tieba.write('答：'+dayin)
    print('第'+str(ye)+'行结束!')
file_tieba.close()



#https://yq.aliyun.com/ziliao/125794
