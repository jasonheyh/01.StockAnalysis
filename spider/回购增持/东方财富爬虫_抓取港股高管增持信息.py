#-*- coding:utf-8 -*-
import requests
import pandas as pd
import sqlite3

from bs4 import BeautifulSoup

CONST_TABLE_NAME = 'hkzc'
CONST_STOCK_CODE = '股票代码'
CONST_DATE = '日期'

print("#####东方财富爬虫_抓取港股高管增持信息 开始#####")

conn= sqlite3.connect("../../db/stock.db")
cursor = conn.execute("SELECT max(" + CONST_DATE + ") from " + CONST_TABLE_NAME)
max_date = ""
for row in cursor:
    max_date = row[0]
if(not max_date):
    max_date = "2017-01-10"
# max_date = "2017-01-10"
url = 'http://hk.eastmoney.com/hold_%page%.html?code=&sdate=&edate='

def get_table_texts(p_url, page):
    """
    获取URL中的Table的文字数据
    :param p_url: 
    :return: 
    """
    retText = ""
    _url = p_url.replace("%page%", str(page))
    page = requests.get(url=_url)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find("div", {'class' : 'data'})
    for row in table.findAll("ul"):
        cells = row.findAll("li")
        if (len(cells) > 0):
            texts = map(strip, cells)
            texts = list(texts)[1:]
            retText = retText + ",".join(texts) + "\n"
    return retText;

def strip(x):
    if(x.find(text=True)):
        return x.find(text=True).strip()
    else:
        return "";

def converNum(mount):
    if ('万' in mount):
        return float(mount.replace('万', "")) * 10000
    else:
        return mount

for i in range(1, 10000):
    fs = open('hkzc.csv', 'w')
    fs.write("股票代码,股票名称,机构名称,变动方向,变动股份数,变动后数量,变动后持股率,日期\n")
    fs.write(get_table_texts(url, i))
    fs.close()

    pd_ret_data = pd.read_table("hkzc.csv", sep=',')
    pd_ret_data[CONST_STOCK_CODE] = pd_ret_data[CONST_STOCK_CODE].apply(lambda x: str(x).zfill(5))
    pd_ret_data['变动股份数'] = pd_ret_data['变动股份数'].apply(converNum)
    pd_ret_data['变动后数量'] = pd_ret_data['变动后数量'].apply(converNum)
    pd_ret_data['变动后数量'] = pd_ret_data['变动后数量'].apply(lambda x: round(x,0))
    minDate = pd_ret_data[CONST_DATE].min()
    print(minDate)
    if (minDate <= max_date):
        pd_ret_data = pd_ret_data[pd_ret_data[CONST_DATE] > max_date]
        pd_ret_data.to_sql(CONST_TABLE_NAME, conn, if_exists='append', index=False)
        break
    else:
        pd_ret_data.to_sql(CONST_TABLE_NAME, conn, if_exists='append', index=False)

conn.close()

print("#####东方财富爬虫_抓取港股高管增持信息 结束#####")
