"""This is a python code that surf a website, get the href attribute of an anchor tags at a particular position and repeat a given number of times"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore certification issues
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url_')
#html = urllib.request.urlopen(url)
html_list = [ ]
pos = int(input("Enter the position:"))
no_of_times = int(input("Enter how many times:"))
print("Retrieving:", url)
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')
for t in tags:
    html_list.append(t.get('href', None))

for i in range(no_of_times):
    List = [ ]
    new_url = html_list[pos - 1]
    print("Retrieving:", new_url)
    new_html = urllib.request.urlopen(new_url, context = ctx).read()
    new_soup = BeautifulSoup(new_html, "html.parser")
    lnks = new_soup('a')
    for hr in lnks:
        w = hr.get('href', None);
        List.append(w)
    html_list = List[ : ]

#    print(t)
#    print("class:", t.get('class', None))
#    print("content:", t.contents[0])
#    print("Attributes:", t.attrs)

