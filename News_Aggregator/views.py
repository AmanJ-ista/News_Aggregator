from django.shortcuts import render
from bs4 import *
import requests
from bs4 import *
import html5lib



#TOI
URL = "https://timesofindia.indiatimes.com/briefs"
r = requests.get(URL)
a = r.content
head=[]
b = BeautifulSoup(r.content, 'html5lib')
headings = b.find_all('h2')
headings = headings[2:-13]
for x in headings:
    head.append(x.get_text())

img = []
c = b.find_all('div', class_='posrel')
for x in c:
    img.append(x.find('img').get('data-src'))



link=[]
c=b.find_all('div',class_='brief_box')

for x in c:
    link.append(x.find('a'))
for y in link:
    if y==None:
        pass
    else:
         print("https://timesofindia.indiatimes.com/"+y.get('href'))




combo2=dict(zip(head,img))



#Indian Express

URL = "https://indianexpress.com/latest-news/"
a = requests.get(URL)
b = a.content
parsed = BeautifulSoup(b, 'html5lib')
a = parsed.find_all('div', class_='title')
c = []
title = []
for x in a:
    c.append(x.find('a'))
for x in c:
    title.append(x.get_text())

para = parsed.find_all('div', class_='articles')
paragraph = []
for x in para:
    paragraph.append(x.find('p').get_text())

img = parsed.find_all('div', class_='snaps')
images = []
for x in img:
    images.append(x.find('img').get('data-lazy-srcset'))

combo1=dict(zip(paragraph,images))

param={'combo2':combo2,'combo1':combo1}


def news(request):
    a=request.GET.get('email1')
    print(a)
    return render(request, 'first.html', param)
