#-*- coding:utf-8 -*-
import requests
import pandas as pd
import sqlite3

from bs4 import BeautifulSoup
import re

CONST_TABLE_NAME = 'hkgt_ss'
CONST_DATE = '日期'

print("#####东方财富爬虫_抓取沪港股通 开始#####")

conn= sqlite3.connect("../../db/stock.db")
cursor = conn.execute("SELECT max(" + CONST_DATE + ") from " + CONST_TABLE_NAME)
max_date = ""
for row in cursor:
    max_date = row[0]
if(not max_date):
    max_date = "2014-11-18"

url = 'http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get?type=HSGTHIS&token=70f12f2f4f091e459a279469fe49eca5&filter=(MarketType=2)&js=var%20xFLaawVQ={%22data%22:(x),%22pages%22:(tp)}&ps=20&p=%page%&sr=-1&st=DetailDate&rt=50864488'

def get_table_texts(p_url, page):
    """
    获取URL中的Table的文字数据
    :param p_url:
    :return:
    """
    _url = p_url.replace("%page%", str(page))
    page = requests.get(url=_url)
    pattern = "var.*={"
    _data = re.sub(pattern, "{" , page.text)
    _data = eval(_data)

    return _data['data']

def converNum(mount):
    if ('万' in mount):
        return float(mount.replace('万', "")) * 10000
    else:
        return mount

for i in range(1, 100):
    pd_ret_data = pd.DataFrame()
    jsonData = get_table_texts(url, i)
    for item in jsonData:
        tradeData = pd.DataFrame.from_dict(item,orient='index').T
        if(len(pd_ret_data) > 0):
            pd_ret_data = pd_ret_data.append(tradeData, ignore_index=False)
        else:
            pd_ret_data = tradeData

    pd_ret_data = pd_ret_data.reset_index(drop=True)
    pd_ret_data.rename(columns={'DetailDate': '日期',
                            'DRZJLR': '当日资金流入',
                            'DRYE': '当日余额',
                            'LSZJLR': '历史资金累计流入',
                            'DRCJJME': '当日成交净买额',
                            'MRCJE': '买入成交额',
                            'MCCJE': '卖出成交额'}, inplace=True)
    pd_ret_data= pd_ret_data.drop(pd_ret_data.columns[0:1], 1)
    pd_ret_data= pd_ret_data.drop(pd_ret_data.columns[7:], 1)
    pd_ret_data = pd_ret_data.applymap(lambda x : round(x, 2) if (isinstance(x, float)) else x)
    minDate = pd_ret_data[CONST_DATE].min()
    print(minDate)
    if (minDate <= max_date):
        paRetData = pd_ret_data[pd_ret_data[CONST_DATE] > max_date]
        paRetData.to_sql(CONST_TABLE_NAME, conn, if_exists='append', index=False)
        break
    else:
        pd_ret_data.to_sql(CONST_TABLE_NAME, conn, if_exists='append', index=False)

conn.close()

print("#####东方财富爬虫_抓取沪港股通 结束#####")
