#coding=utf-8

import re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys

def getHTML(url):
  req = urllib2.Request(url)
  req.add_unredirected_header('User-agent','Mozilla/5.0')
  try:
     response = urllib2.urlopen(req).read()
  except urllib2.HTTPError, e:
     response = e.getcode()
  return response

  

url = "http://xemphimso.com/xem-phim-chieu-rap.html"
subvlinks = []
mList = []
titleList = []
linkList = []

soup = BeautifulSoup(getHTML(url),"html.parser")
list = soup.find('ul',class_='cfv')


for item in list.select('li'):
 mList.append(item.a.get('href'))
 #print (item.a.get('href'))
 #print item.read.strip().encode('utf-8')
 titleList.append(item.a.get('title'))
# img.append(item.a.get('src'))

for mLink in mList:
 
 html = getHTML(mLink) 
 tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
 verify = "javascript"
 confirm = str(tempLink).find(verify) 
 if confirm != -1:
   mList.remove(mLink)
   continue
 else:
   html2 = getHTML(tempLink[0])
   
   vlinks = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
   #vlinks = re.compile('a onclick="(.+?)" href="(.+?)"').findall(html2)
   #print vlinks[0] 
   search = "grab."
   result = [s for s in vlinks if search in s]
   if len(result) > 0:
   #   #subvlinks.append(result)
   #   print "get the file for ", result
      html3 = getHTML(result[0])
      if html3 == 404:
   #     print "link broken"
         mList.remove(mLink)
         continue
      else:
        filelink = re.compile('"file":"(.+?)","label"').findall(html3)
        #if len(filelink)==0:
        #  link = item
        if len(filelink)>=1:
          link  = filelink[len(filelink)-1].replace('\\','').strip('"')
          #print link
          linkList.append(link)
   else:
     mList.remove(mLink)
     continue     
print len(mList), len(linkList)
#for item in subvlinks:
 #html3 = getHTML(item)
 #filelink = re.compile('"file":"(.+?)","label"').findall(html3)
 #if len(filelink)==0:
  # link = item 

 #if len(filelink)>=1:
 #  link  = filelink[len(filelink)-1].replace('\\','').strip('"')
 #linkList.append(link)
 #print link

