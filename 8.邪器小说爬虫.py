import urllib.request
import re
txt=''
#下载页面
def getSrc(url):
    html_src = urllib.request.urlopen(url).read().decode('GBK')  
    return html_src
#找到页面中的url
def findUrls(html):
    splitM=html.split('\n')
    for i in splitM:
        if '正文' in i:
            UrlList=re.findall('(\d{7}.html)',i)
    return UrlList
def txt_zi(html):
    neirong=html.split('\r\n')
    for zi in neirong:
        if '<title>邪' in zi:
            title=zi.replace('<title>邪器_ ','').replace('</title>','').replace('_爱上中文','')  
            print ('现在打印 '+title)
        if 'contents' in zi:
            txt='\r\n'+title+'\r\n'+zi.replace(" ","").replace("<br />","").replace("<div id=\"contents\">","").replace("</div>","").replace('<br/><br/>&nbsp;&nbsp;&nbsp;&nbsp;','').replace('<divid="contents">&nbsp;&nbsp;&nbsp;&nbsp;','')+'\r\n'
            break
    return txt  
#程序入口
mainUrl='http://www.aszw8.com/book/16/16420/'
urlList=findUrls(getSrc(mainUrl))
for wangzhi in urlList:
    dizhi=mainUrl+wangzhi
    txt=txt_zi(getSrc(dizhi))
    wfile=open('F:\仙剑问情.txt','r+')
    wfile.read()
    wfile.write(txt)
    wfile.close()
    





