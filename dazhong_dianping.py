#美食url='http://www.dianping.com/luohe/food'

import requests
from bs4 import BeautifulSoup
import xlwt

start_url='http://www.dianping.com/zhengzhou/ch10/r2038'

def get_content(url,headers=None):
    '''
    request得到URL网页内容
    :param url:
    :param headers:
    :return: 内容
    '''
    r=requests.get(url,headers=headers)
    return r.content

def region_url(html):
    '''
    得到初始网页中的不同商区的链接URL
    :param html:
    :return:URL列表
    '''
    soup = BeautifulSoup(html,'html.parser')
    url_list=[i['href'] for i in soup.find('div',id='bussi-nav').find_all('a')]
    print('所有商区的链接')
    print(url_list)
    return url_list

def shop_url(html):
    '''
    得到每个商店的链接URL
    :param html:
    :return: URL列表
    '''
    soup=BeautifulSoup(html,'html.parser')
    div_list=soup.find_all('div',class_='tit')
    print('所有商店的链接')
    print([i.find('a')['href'] for i in div_list])
    return [i.find('a')['href'] for i in div_list]

def get_detail(url):
    '''
    :param url:
    :return:得到每个商店详情页面所需信息
    '''
    headers={ 'Referer':'http://www.dianping.com/zhengzhou/ch10/r2038',
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
             'Cookie':'_lxsdk_cuid=161dba1c51dc8-005d001084fb15-3b60450b-100200-161dba1c51dc8; _lxsdk=161dba1c51dc8-005d001084fb15-3b60450b-100200-161dba1c51dc8; _hc.v="\"a046baa1-939f-4860-a287-18fc993e671a.1519808271\""; s_ViewType=10; _tr.u=qk0Yfa3ULPfmSBlx; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; cy=160; cye=zhengzhou; _lxsdk_s=161e409d127-b13-0bf-527%7C%7C276'}
    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.content,'html.parser')

    name=soup.find('div',class_='breadcrumb').find('span').text
    avgPrice=soup.find('span',id='avgPriceTitle').text
    comment_list=soup.find('span',id='comment_score').find_all('span',class_='item')
    comments=soup.find('span',id='reviewCount').text
    address=soup.find('div',class_='expand-info address').find('span',class_='item').text

    print(url)
    print('店名：'+name)
    print('人均消费：' + avgPrice)
    print('评论数量：'+comments)
    for i in comment_list:
        print(i.text)
    print('地址'+address)
    return (name,avgPrice,comments,comment_list[0].text,comment_list[1].text,comment_list[2].text,address)


if __name__=='__main__':
    items=[]
    #将代码伪装成浏览器
    headers={
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Cookie':'_lxsdk_cuid=161dba1c51dc8-005d001084fb15-3b60450b-100200-161dba1c51dc8; _lxsdk=161dba1c51dc8-005d001084fb15-3b60450b-100200-161dba1c51dc8; _hc.v="\"a046baa1-939f-4860-a287-18fc993e671a.1519808271\""; s_ViewType=10; cy=170; cye=luohe; _tr.u=qk0Yfa3ULPfmSBlx; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=161dba1c522-f4a-dfc-11%7C%7C81'}
    html=get_content(start_url,headers)
    place_url_list=region_url(html)
    all_shop_urls=[]
    for place in place_url_list:
        #遍历所有商圈，得到所有商店的URL
        place_html=get_content(place,headers)
        shop_urls=shop_url(place_html)
        all_shop_urls.extend(shop_urls)
    all_shop_detail=[]
    for url in all_shop_urls[0:10]:
        #遍历所有商店，得到每个商店的详情页面
        item=get_detail(url)
        items.append(item)

    #创建EXCEL
    new_table='DZDP2.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('test')
    headDate=['商户名字','人均消费','评论数量','口味评分','环境评分','服务评分','地址']
    for colnum in range(0,7):
        ws.write(0,colnum,headDate[colnum],xlwt.easyxf('font:bold on'))
    index=1
    #保存数据在EXCEL
    for i in range(len(items)):
        for j in range(0,7):
            ws.write(index,j,items[i][j])
        index+=1
    wb.save(new_table)




