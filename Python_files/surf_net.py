"""This is a python code that surf a website and get the sum of the contents of all span tags"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore certification issues
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url_')
#html = urllib.request.urlopen(url)
values = [ ]
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
for t in tags:
    values.append(int(t.contents[0]))
print(sum(values))
#    print(t)
#    print("class:", t.get('class', None))
#    print("content:", t.contents[0])
#    print("Attributes:", t.attrs)

