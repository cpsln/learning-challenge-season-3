# web scraping from url

import re,urllib
import urllib.request
u=urllib.request.urlopen('https://www.redbus.in/info/contactus')
text=u.read()
n=re.findall('[0-9-]{7}[0-9-]+',str(text))
for i in n:
    print(i)
