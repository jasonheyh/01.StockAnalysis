# -*- coding:utf-8 -*-
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import time
def get_info(start=1,end=1):
    info = {}  #储存目标数据
    url = 'http://www.szse.cn/main/disclosure/jgxxgk/djggfbd/' #目标链接
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
    }
    # 很好的模拟Post数据的例子
    #爬取所选取页数区间数据，该网页跳转页码，网址不变
    # 通过分析，post的数据中'tab1PAGENUM'是用来控制页码的，通过改变该键的值，来实现页码跳转
    for i in range(start,end+1):
        post_data = urllib.parse.urlencode({'tab1PAGENUM': i}).encode(encoding='UTF8') #需post的数据
        #req = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(url, post_data)  #为data参数赋值
        time.sleep(2) #防止访问太频繁
        soup = BeautifulSoup(res, 'lxml')
        titles = soup.find_all('td', class_='cls-data-th') #标题行
        datas = soup.find_all('td', class_='cls-data-td')  #数据行
        num = int(len(datas) / len(titles))                #数据行数
        #将数据写入本地文件
        with open('test1.txt', 'a') as fs:
            for j in range(num):
                for title, data in zip(titles, datas[12 * j:12 * (j + 1)]):
                    info[title.get_text()] = data.get_text()
                    s = str(info)
                fs.writelines(s)
                fs.writelines('\n')
            print('Done!')
get_info(1,100)
