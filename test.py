import requests
import pandas as pd
from bs4 import BeautifulSoup
import lxml

url='https://tieba.baidu.com/f?kw=tibette'
r=requests.get(url)
html=r.text
soup=BeautifulSoup(html,'lxml')
# print(soup.body)
l=[x for x in soup.findAll('a')]
df=pd.DataFrame(l,columns=[url])
# print(df)

links=[i for i in soup.findAll('a') if i.has_attr('href') and i.attrs['href'][0:5]!='https'
       and i.attrs['href'][0:4]!='http']
relative_urls=set([i.attrs['href'] for i in links])
for i in relative_urls:
    print(i)
absolute_urls={'https://tieba.baidu.com/'+i for i in relative_urls}
absolute_urls.discard(url)

for i in absolute_urls:
    ri=requests.get(i)
    soupi=BeautifulSoup(ri.text,'lxml')
    li=[x.text for x in soupi.findAll('a')]
    dfi=pd.DataFrame(li,columns=[i])
    df=df.join(dfi,how='outer')
print(df)
