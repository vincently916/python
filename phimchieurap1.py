# import xbmcgui
# import xbmcplugin,xbmcaddon,xbmcvfs
import re
from bs4 import BeautifulSoup
import urllib,urllib2,os,sys

url = "http://xemphimso.com/xem-phim-chieu-rap.html"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}
search = "grab."

# Initialize the movies home page list, titles list, sub videos links list, and the video list
mlist = []
linkList = []
titleList = []
subvlink = []
imgList = []


################################
# Begin Scraping the site
################################

# Scrape the web page
req = urllib2.Request(url)
req.add_unredirected_header('User-agent','Mozilla/5.0')
response = urllib2.urlopen(req)
soup = BeautifulSoup(response.read(),"html.parser")
html = soup.find('ul',class_='cfv')

# Get the movies page an titles list
for item in html.select('li'):
 mlist.append(item.a.get('href'))
 titleList.append(item.a.get('title'))
 imgList.append(item.img.get('src'))
 
# Get sub video links before we get to the actual video file link
for mlink in mlist:
 req1 = urllib2.Request(mlink)  
 req1.add_unredirected_header('User-agent','Mozilla/5.0')
 response1 = urllib2.urlopen(req1)
 html1 = re.compile('<a class="btn-watch" href="(.+?)"').findall(response1.read())
 verify = "javascript"
 confirm = [link for link in html1 if verify in link]
 if len(confirm) > 0:
   mlist.remove(mlink)
   continue
 else:
  req2 = urllib2.Request(str(html1[0]))
  req2.add_unredirected_header('User-agent','Mozilla/5.0')
  response2 = urllib2.urlopen(req2)
  html2 = re.compile('<script type="text/javascript" src="(.+?)"></script>').findall(response2.read())
  search_result = [vlink for vlink in html2 if search in vlink]
  subvlink.append(search_result[0])

# Get the actual video file link
for subLink in subvlink:
  req3 = urllib2.Request(subLink) 
  req3.add_unredirected_header('User-agent','Mozilla/5.0')
  response3 = urllib2.urlopen(req3)
  fileLink = re.compile('"file":"(.+?)","label"').findall(response3.read())
  if len(fileLink) == 0:
   link = item 

  if len(fileLink) >= 1:
    link  = fileLink[len(fileLink)-1].replace('\\','').strip('"')
  print link
   # linkList.append(link)
#### End web page scraping ######

#############################
#Begin Kodi Section
#############################

# Generate the list for Kodi
# addon_handle = int(sys.argv[1])
# xbmcplugin.setContent(addon_handle, 'movies')

# count = 0
# while (count <= len(titleList) - 1):
  # url = linkList[count]
  # li = xbmcgui.ListItem(titleList[count], iconImage='http://xemphimso.com/images/film/xemphimso_kungfu-pho.jpg')
  # xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
  # count = count + 1
  
# xbmcplugin.endOfDirectory(addon_handle)
###End######