from unidecode import unidecode
import requests,re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys

url = "http://xemphimso.com/xem-phim-chieu-rap.html"
response = requests.get(url)
subvlinks = []
soup = BeautifulSoup(response.text,"html.parser")

list = soup.find('ul',class_='cfv')
mlist = []
for item in list.select('li'):
 mlist.append(item.a.get('href'))
 #print (item.a.get('href'))
 #print item.text.strip().encode('utf-8')

for each in mlist:
 getLink = requests.get(each)
 tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(getLink.text)
 getTempLink = requests.get(tempLink[0])
 vlinks = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(getTempLink.text)
 subvlinks.append(vlinks[len(vlinks)-1])
 #print len(vlinks)
 #print tempLink
 #print subvlinks 
for item in subvlinks:
 getFile = requests.get(item)
 filelink = re.compile('"file":"(.+?)","label"').findall(getFile.text)
 if len(filelink)==0:
   link = item 

 if len(filelink)>=1:
   link  = filelink[len(filelink)-1].replace('\\','').strip('"')
 #print link

