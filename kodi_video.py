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
mList = []
titleList = []
linkList = []
imgList = []
pageList = []

soup = BeautifulSoup(getHTML(url),"html.parser")
list = soup.find('ul',class_='cfv')
count = 0

for item in list.select('li'):
 mList.append(item.a.get('href'))
 titleList.append(item.a.get('title'))
 imgList.append(item.img.get('src'))

for page in soup.find_all('a',class_='pagelink'):
  tempPage = str(page.get('href'))
  if page.text == "LAST":
     lastIndex = len(page.get('href')) - 6
     lastPage = int(page.get('href')[lastIndex -1:lastIndex + 1])
     currentLen = len(pageList)  
     while currentLen <= lastPage:
       newPage = tempPage[0:45] + str(currentLen) + ".html"
       pageList.append(newPage)
       currentLen = currentLen + 1
  else:
    pageList.append(page.get('href'))

#while count < len(mList) - 1:
# #print "get video file for ", mList[count],titleList[count]
# html = getHTML(mList[count]) 
# tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
# verify = "javascript:alert"
# confirm = [x for x in tempLink if verify in x] 
# if len(confirm) == 1:
#   mList.remove(mList[count])
#   del titleList[count]
#   del imgList[count]
#   continue
# else:
#   html2 = getHTML(tempLink[0])
#   templink2 = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(html2)
#   search = "grab."
#   result = [s for s in templink2 if search in s]
#   if len(result) > 0:
#      html3 = getHTML(result[0])
#      if html3 == 404:
#          del mList[count]
#          del titleList[count]
#          del imgList[count]
#          continue
#      else:
#          filelink = re.compile('"file":"(.+?)","label"').findall(html3)
#	  if len(filelink)==0:
#            link = tempLink[0]
#          if len(filelink)>=1:
#            link  = filelink[len(filelink)-1].replace('\\','').strip('"')
#          title = titleList[count]
#	  image = imgList[count]
#	  #li = xbmcgui.ListItem(title, iconImage=image)
#	  #xbmcplugin.addDirectoryItem(handle=addon_handle, url=link, listitem=li)
#          #print titleList[count]
#          #print imgList[count]
#          #print link
#   else:
#     del mList[count]
#     continue 
# count = count + 1    
#
#
