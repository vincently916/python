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
imgList = []

soup = BeautifulSoup(getHTML(url),"html.parser")
list = soup.find('ul',class_='cfv')
count = 0

for item in list.select('li'):
 mList.append(item.a.get('href'))
 titleList.append(item.a.get('title'))
 imgList.append(item.img.get('src'))

#while count < len(mList) - 1:
#   print mList[count]
#   print titleList[count]
#   count = count + 1
#
#count = 0

#for mList[count] in mList:
while count < len(mList) - 1:
 #print "get video file for ", mList[count],titleList[count]
 html = getHTML(mList[count]) 
 tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
 verify = "javascript:alert"
 confirm = [x for x in tempLink if verify in x] 
 if len(confirm) == 1:
   #print 'invalid link', confirm
   mList.remove(mList[count])
   del titleList[count]
   del imgList[count]
   continue
 else:
   html2 = getHTML(tempLink[0])
   vlinks = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
   #vlinks = re.compile('a onclick="(.+?)" href="(.+?)"').findall(html2)
   #print vlinks[0] 
   search = "grab."
   result = [s for s in vlinks if search in s]
   if len(result) > 0:
      html3 = getHTML(result[0])
      if html3 == 404:
          #print "link broken", mList[count]
          
          #print "remove from mlist", mList[count]
          #print "remove from title list", titleList[count]
	  #print "remove from imgList", imgList[count]
          del mList[count]
          del titleList[count]
          del imgList[count]
          continue
      else:
          filelink = re.compile('"file":"(.+?)","label"').findall(html3)
          #print "link for mlink", mList[count] 
	  if len(filelink)==0:
            link = tempLink[0]
          if len(filelink)>=1:
            link  = filelink[len(filelink)-1].replace('\\','').strip('"')
            linkList.append(link)
          #print "add video for ", titleList[count]
          #print link
   else:
     del mList[count]
     continue 
 count = count + 1    

count = 0

while count < len(titleList) - 1:
   print titleList[count]
   print linkList[count]
   count = count + 1
