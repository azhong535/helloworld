import urllib.request
import http.client
import bs4 
import re
from urllib.parse import quote
from lxml import etree
import time
file_tieba=open('智通机械类.txt','a+',encoding='utf-8')
pattern=re.compile('clearfix ')
keyword="机械工程师"
money=7000
main=('http://www.job5156.com/s/result/kt0_kw-%s_df1_dt8_dul1_ud90_yf-1_yt11_wyul1_sa%d_sup1_pn'%(keyword,money))
def dai(daiyu):
    b=''
    for fuli in daiyu:
        b+=fuli
    return b
def wenzi(selector):
    jobname= selector.xpath('//h1[@class="job-name "]/text()')
    lxdz=selector.xpath('//p/text()')
    daiyu= selector.xpath('//span[@class="tao-tag"]/text()')
    gongzi=selector.xpath('//div[@class="salary"]/text()')
    nianling=selector.xpath('//div[@class="text-overflow"]/span/text()')
    xueli=selector.xpath('//div[@class="text-overflow"]/span/text()')
    zprs=selector.xpath('//div[@class="emp_msg"]/span/text()')
    ms=selector.xpath('//div[@class="desc content job_description"]/pre/text()')
    miaosu=dai(ms)
    fuli=dai(daiyu)
    
    print(jobname[0].strip(),lxdz[2].strip(),lxdz[4].strip(),nianling[0].strip())
    if gongzi[0] is True:
        file_tieba.write('  招聘职位：'+jobname[0].strip()+'  联系人：'+lxdz[2].strip()+'  公司地址:'+lxdz[1].strip()+"  福利待遇："+fuli.strip()+'  工资：'+gongzi[0].strip()+'  年龄：'+nianling[1].strip()
                     +'  学历:'+xueli[0].strip()+'  招聘人数:'+zprs[4].strip()+'\r\n职位描述：\r\n'+miaosu.strip()+'\r\n')
    else:
        file_tieba.write('  招聘职位：'+jobname[0].strip()+'  联系人：'+lxdz[2].strip()+'  公司地址:'+lxdz[1].strip()+"  福利待遇："+fuli.strip()+'  年龄：'+nianling[1].strip()
                     +'  学历:'+xueli[0].strip()+'  招聘人数:'+zprs[4].strip()+'\r\n职位描述：\r\n'+miaosu.strip()+'\r\n')
        
    
 
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
#正文
for ye in range(0,60):
    mainurl=quote(main+str(ye), safe='/:?=')
    print(mainurl)
    shuzu=fenxi(mainurl)
    qian,name,urlgo=neirong(shuzu)
    i=0
    print(name)
    for dizhi in urlgo:
        file_tieba.write('\r\n'+'第'+str(i+ye*15)+"章 :"+'\r'+name[i].strip()+qian[i].strip()+'\r\n'+str(dizhi)+'\r\n')
        i+=1
        print(i,dizhi)
        jiexi=fenxi(dizhi)
        wenzi(jiexi)
file_tieba.close()
 
