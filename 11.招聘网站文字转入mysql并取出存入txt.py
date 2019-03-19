import urllib.request
import http.client
import bs4 
import re
from urllib.parse import quote
from lxml import etree
import time
import pymysql
file_tieba=open('智通机械类.txt','a+',encoding='utf-8')
conn=pymysql.connect(host='localhost',user='root',passwd='',db='cazdb',charset='utf8')  
cur=conn.cursor()
pattern=re.compile('clearfix ')
keyword="机械工程师"
money=6000
main=('http://www.job5156.com/s/result/kt0_kw-%s_df1_dt8_dul1_ud90_yf-1_yt11_wyul1_sa%d_sup1_pn'%(keyword,money))
def dai(daiyu):
    b=''
    for fuli in daiyu:
        b+=fuli
    return b


def changcode(wen):
    qukongge=wen.strip()
    fanyi=qukongge.encode('utf8')
    return fanyi

def wenzi(selector):
    jobname= selector.xpath('//h1[@class="job-name "]/text()')
    lxdz=selector.xpath('//p/text()')
    daiyu= selector.xpath('//span[@class="tao-tag"]/text()')
    gongzi=selector.xpath('//dd[@class="col-9 td text-center c-money text-overflow"]/text()')
    nianling=selector.xpath('//dd[@class="col-9 td text-center text-overflow"]/text()')
    xueli=selector.xpath('//dd[@class="col-8 td text-center text-overflow"]/text()')
    zprs=selector.xpath('//dd[@class="col-8 td text-center text-overflow"]/text()')
    ms=selector.xpath('//div[@class="desc content"]/pre/text()')
    miaosu=dai(ms)
    fuli=dai(daiyu)
    print(jobname[0].strip(),lxdz[2].strip(),lxdz[4].strip(),gongzi[0].strip())
    effect_row = cur.executemany("insert into zhaopin values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    [(changcode(jobname[0]),changcode(lxdz[2]),changcode(lxdz[4]),
                                    changcode(fuli),changcode(gongzi[0]),changcode(nianling[0]),
                                      changcode(xueli[0]),changcode(zprs[5]),changcode(miaosu))])
    
    conn.commit()

     
def neirong(selector):    
    qian= selector.xpath('//span[@class="c-money"]/text()')
    name= selector.xpath('//a[@class="comp-name c-gray text-overflow  height-light"]/@title')
    urlgo= selector.xpath('//a[@class="pos-name text-overflow gutter-bottom"]/@href') 
    return qian,name,urlgo
def fenxi(mainurl):
    request = urllib.request.Request(mainurl)
    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; \
        WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
    try:  
        rep=urllib.request.urlopen(mainurl)
    except http.client.HTTPException as e:  
        print(repr(e))  
    else:  
        rep_utf=rep.read()
        soup=bs4.BeautifulSoup(rep_utf,'html.parser',from_encoding="iso-8859-1")
        selector = etree.HTML(rep_utf)
        return selector

def savetxt():
    cur.execute("select * from zhaopin")
    ret2 = cur.fetchmany(5)
    for hi in ret2:
        print(hi)
        for mm in hi:
            file_tieba.write('\r\n'+mm+'\r\n')

        

#正文

for ye in range(1,3):
    mainurl=quote(main+str(ye), safe='/:?=')
    print(mainurl)
    shuzu=fenxi(mainurl)
    qian,name,urlgo=neirong(shuzu)
    print(name)
    for dizhi in urlgo:
        jiexi=fenxi(dizhi)
        wenzi(jiexi)
savetxt()
file_tieba.close()
cursor.close()
conn.close()

 
