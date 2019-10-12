# -*- coding: utf-8 -*-
# url='https://www.duitang.com/napi/blog/list/by_search/?kw=%E5%8A%A8%E6%BC%AB&start=48&limit=1000'
import requests
import urllib.parse
import threading


thread_lock=threading.BoundedSemaphore(value=5)

#得到每一个页面中的所有内容
def get_page(url):
    page = requests.get(url)
    page = page.content   #得到BYTES
    page = page.decode('utf-8')  #将BYTES转为str
    return page

#print(get_page(url))
#得到一个页面中的所有图片的URL，放入列表URLS
#startpart为URL的开始标志，endpart为URL的结束标志
def fingall_url(page,startpart,endpart):
    urls=[]
    end=0
    while (page.find(startpart,end))!=-1:
        start=page.find(startpart,end)+len(startpart)  #URL开始坐标
        end=page.find(endpart,start)     #URL结束坐标
        urls.append(page[start:end])
    return urls

#得到所有的Page,大概有3600张照片，观察后每次可以取100，需要36次
def get_allPages(label):
    url = 'https://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000'
    pages = []
    label = urllib.parse.quote(label)
    for index in range(0,3600,100):
        u = url.format(label,index)
        print(u)
        page = get_page(u)
        pages.append(page)
    return pages

#得到所有页面的所有的URL
def find_allpages_urls(pages):
    all_urls = []
    for page in pages:
        us = fingall_url(page,'"path":"','"')
        all_urls.extend(us)
    return all_urls

#得到一个图片链接，放入文件中
def download_pics(url,n):
    r = requests.get(url)
    path = 'picture/'+str(n)+'.jpg'
    with open(path,'wb') as file:
        file.write(r.content)

        #解锁
    thread_lock.release()

#下载所有图片
def main(label):
    pages = get_allPages(label)
    all_urls = find_allpages_urls(pages)
    #print(all_urls)
    n = 0
    for url in all_urls:
        n+=1
        print('正在下载第{}张图片'.format(n))
        #上锁
        thread_lock.acquire()
        t=threading.Thread(target = download_pics,args=(url,n))
        t.start()


main('吴世勋')