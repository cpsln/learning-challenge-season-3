#web scraping

import re,urllib
import urllib.request
sites=['https://www.google.com/','https://www.rediff.com/']
for s in sites:
    print('\nSearching....',s)
    u=urllib.request.urlopen(s)
    text=u.read()
    # print(text)
    # print(type(text))
    title=re.findall('<title>.*</title>',str(text),re.IGNORECASE)
    print(title[0])