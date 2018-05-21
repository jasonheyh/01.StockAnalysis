#-*- coding:utf-8 -*-
import requests
import pandas as pd
import sqlite3

from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

CONST_TABLE_NAME = 'yjyz'
CONST_STOCK_CODE = '股票代码'
CONST_DATE = '公告日期'
CONST_YEAR = "2018"
CONST_PERIED = "MIDDLE"

conn= sqlite3.connect("../../db/stock.db")

print("#####爬虫_抓取业绩预增信息 开始#####")

search_day = ""
if (CONST_PERIED == "MIDDLE") :
    search_day = CONST_YEAR + "-06-30"
else:
    search_day = CONST_YEAR + "-12-31"


url = "http://ds.emoney.cn/DataCenter2/DataCenter/yjyg_0?SortName=PublDate&SortFlag=&BlockName=&Stock=&Year=" + search_day + "&DataType=&index="
page = requests.get(url + "1")
doc = pq(page.text)
max_page = ""
if doc(".Pagination"):
    max_page = doc(".Pagination").find("a").eq(-2).text()
#
def get_cell_texts(x):
    labels = x.findAll(text=True)
    labels = map(lambda x: x.strip(), labels)
    return "\"" + "".join(labels) + "\""

def get_table_texts(p_url):
    """
    获取URL中的Table的文字数据
    :param p_url:
    :return:
    """
    retText = ""
    page = requests.get(url=p_url)
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find("tbody")
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if (len(cells) > 0):
            texts = map(get_cell_texts, cells)
            texts = list(texts)
            retText = retText + ",".join(texts) + "\n"
    return retText;
#
# def converNum(mount):
#     if ('万' in mount):
#         return float(mount.replace('万', "")) * 10000
#     else:
#         return mount
#
def split_yeji_change_from(change):
    if "～" in str(change) :
        change_list = change.split("～")
        return change_list[0].replace("%","")
    else:
        return str(change).replace("%","")

def split_yeji_change_to(change):
    if "～" in str(change) :
        change_list = change.split("～")
        return change_list[1].replace("%","")
    else:
        return ""


for i in range(1, int(max_page) + 1 ):
    print("page:" + str(i))
    fs = open('yjyz.csv', 'w')
    fs.write("股票代码,股票名称,日期,业绩变动,业绩变动幅度,预告类型,每股收益_最新估算_元,每股收益_上年同期_元,流通股本_万股,市净率,市盈率\n")
    fs.write(get_table_texts(url + str(i)))
    fs.close()

    pd_ret_data = pd.read_table("yjyz.csv", sep=',')
    pd_ret_data[CONST_STOCK_CODE] = pd_ret_data[CONST_STOCK_CODE].apply(lambda x: str(x).zfill(6))
    pd_ret_data['业绩变动幅度_From_per'] = pd_ret_data['业绩变动幅度'].apply(split_yeji_change_from)
    pd_ret_data['业绩变动幅度_to_per'] = pd_ret_data['业绩变动幅度'].apply(split_yeji_change_to)
    pd_ret_data = pd_ret_data.replace("--","")
    pd_ret_data = pd_ret_data.drop(columns=['业绩变动幅度'])

    pd_ret_data.to_sql(CONST_TABLE_NAME, conn, if_exists='append', index=False)

conn.close()

print("#####爬虫_抓取业绩预增信息 结束#####")
