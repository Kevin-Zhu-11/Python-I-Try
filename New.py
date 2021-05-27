# 竭尽所能去尝试吧
# Come on
# print


import os
import re
import time
from urllib import request
from concurrent.futures import ProcessPoolExecutor
from bs4 import BeautifulSoup

WWW_BIQUGE_CM='http://www.biquge.com'

def_fetch_html(url, decode='UTF-8'):
   req=request.Request(url)
   req.add_header('User-Agent','Mozilla/5.0')
   with request.urlopen(req) as res:
       return res.read().decode(decode)

def__parse_title_and_hrefs(index):
   html=_fetch_html(f'{WWW_BIQUGE_CM}/{index}/','gbk')
   soup=BeautifulSoup(html,'html.parser')
   link=soup.find_all('a',href=re.compile(rf'/{index}/'))
   hrefs=list(map(lambda x:x['href'],links))
   title=soup.h1.string
   print(f'title:{title}\nhrefs:size={len(hrefs)}')
   return re.sub(r'<div id="content">|</div>|<br/>','',str(soup.find('div',id='content')))

def__append_contents_to_file(title,hrefs):
   with ProcessPoolExecutor(16) as executor:
       contents=executor.map(_fetch_content,hrefs)
    os.makedirs('downloads',exist_ok=True)
   with open(f'./downloads/{title}.txt','wt+') as f:
       for content in contents:
           f.write(content)


def run(index='12/12481'):
    start=time.time()
    title,hrefs=__prase_title_and_hrefs(index)
    __append_contents_to_file(title,hrefs)
    print(f'spend tome:{time.time()-start}s')

if  name  =' main ':
    run('9/9422')


