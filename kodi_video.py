import re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys

url = "http://xemphimso.com/xem-phim-chieu-rap.html"
req = urllib2.Request(url)
req.add_unredirected_header('User-agent','Mozilla/5.0')
response = urllib2.urlopen(req)
html = response.read()
subvlinks = []
soup = BeautifulSoup(html,"html.parser")

list = soup.find('ul',class_='cfv')
mlist = []
titleList = []
linkList = []

for item in list.select('li'):
 mlist.append(item.a.get('href'))
 #print (item.a.get('href'))
 #print item.read.strip().encode('utf-8')
 titleList.append(item.a.get('title'))
for each in mlist:
 each = str(each).strip('\'"')
 req1 = urllib2.Request(each)
 req1.add_unredirected_header('User-agent','Mozilla/5.0')
 getLink = urllib2.urlopen(req1)
 html = getLink.read()
 tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
 verify = "javascript"
 confirm = [link for link in tempLink if verify in link]
 if len(confirm) > 0:
   continue
 else:
   print str(tempLink).strip('\'"')
 #tempLink = str(tempLink).strip('\'"')
  #req2 = urllib2.Request(tempLink[0])
 #req2.add_unredirected_header('User-agent','Mozilla/5.0')
 #getTempLink = urllib2.urlopen(req2)
 #html2 = getTempLink.read()
 #vlinks = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
 #subvlinks.append(vlinks[len(vlinks)-1])
 #print len(vlinks)
 #print tempLink
 #print subvlinks 
for item in subvlinks:
 item = str(item).strip('\'"')
 print item
  #req3 = urllib2.Request(item)
 #req3.add_unredirected_header('User-agent','Mozilla/5.0')
 #getFile = urllib2.urlopen(req3)
 #html3 = getFile.read()
 #filelink = re.compile('"file":"(.+?)","label"').findall(html3)
 #if len(filelink)==0:
 #  link = item 

 #if len(filelink)>=1:
 #  link  = filelink[len(filelink)-1].replace('\\','').strip('"')
 #linkList.append(link)
 #print link

