import request,re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys

url = "http://xemphimso.com/xem-phim-chieu-rap.html"
response = urllib2.urlopen(url)
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
 
 getLink = urllib2.urlopen(each)
 html = getLink.read()
 tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
 getTempLink = urllib2.urlopen(tempLink[0])
 html2 = getTempLink.read()
 vlinks = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
 subvlinks.append(vlinks[len(vlinks)-1])
 #print len(vlinks)
 #print tempLink
 #print subvlinks 
for item in subvlinks:
 getFile = urllib2.urlopen(item)
 html3 = getFile.read()
 filelink = re.compile('"file":"(.+?)","label"').findall(html)
 print filelink
 if len(filelink)==0:
   link = item 

 if len(filelink)>=1:
   link  = filelink[len(filelink)-1].replace('\\','').strip('"')
 #linkList.append(link)

count = 0

#while (count <= len(titleList - 1)):
# print titleList[count] + "\n" +  linkList[count]
 #count = count + 1
