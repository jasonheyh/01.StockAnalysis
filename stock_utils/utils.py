# -*- coding: utf-8 -*-

import sys
import json
import traceback
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import stock_utils.const as sconst
import pandas as pd
from pyquery import PyQuery as pq

def normalize_date_format(date_str):
    """normalize the format of data"""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    ret = date_obj.strftime("%Y-%m-%d")
    return ret

def price_to_str_int1000(price):
    return str(int(round(float(price) * 1000, 0))) if str(price) is not '' else ''

# 1000*int price to float val
def int1000_price_to_float(price):
    return round(float(price) / 1000.0, 3) if str(price) is not '' else float(0)

# 10^9 int price to float val
def int10_9_price_to_float(price):
    return round(float(price) / float(10**9), 3) if str(price) is not '' else float(0)

# list 参数除重及规整
def unique_and_normalize_list(lst):
    ret = []
    if not lst:
        return ret
    tmp = lst if isinstance(lst, list) else [lst]
    [ret.append(x) for x in tmp if x not in ret]
    return ret

def conver_num(mount):
    '''
    带汉字万的数字转换成Number
    :param mount:
    :return:
    '''
    if ('万' in mount):
        return float(mount.replace('万', "")) * 10000
    else:
        return mount


def get_table_texts(p_url):
    """
    获取URL中的Table的文字数据
    :param p_url:
    :return:
    """
    retText = ""
    page = requests.get(url=p_url + str(i))
    soup = BeautifulSoup(page.text, "html.parser")
    table = soup.find("table", {})
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        if (len(cells) > 0):
            texts = map(lambda x: x.find(text=True).strip(), cells)
            retText = retText + ",".join(list(texts)) + "\n"
    return retText;


def get_stock_info_tencent(stock_list):
    '''
    取得股票基本信息（A股，港股）
    :param stock_list: 股票列表，A股和港股不能一起
    :return:
    '''
    _market = ""
    _stock_list = []
    for for_stock in stock_list:
        if (len(for_stock) == 5):
            _market = "HK"
            for_stock = "hk" + for_stock
        elif (for_stock[0:2] == "60"):
            for_stock = "sh" + for_stock
            _market = "A"
        elif (for_stock[0:2] == "00"):
            for_stock = "sz" + for_stock
            _market = "A"


        _stock_list.append(for_stock)
    url = "http://qt.gtimg.cn/q=" + ",".join(_stock_list)
    stock_info_list = requests.get(url).text.split(";")

    stock_info_dict = {}
    for for_stock in stock_info_list:
        if(for_stock and len(for_stock) > 1):
            _stock_info_str = for_stock.split("=")
            _stock_name = _stock_info_str[0].strip("\n")[4:]
            _stock_info_list = _stock_info_str[1].strip("\"").split("~")
            stock_info_dict.update({_stock_name : _stock_info_list})

    retPd=pd.DataFrame.from_dict(stock_info_dict, orient='index')
    if (_market == "A"):
        retPd.columns = sconst.TENCENT_STOCK_COLUMN
    else :
        retPd.columns = sconst.TENCENT_STOCK_COLUMN_HK

    for for_column in retPd.columns:
        if ("不明" in for_column):
            del retPd[for_column];

    return retPd;

# if __name__ == '__main__':
#     get_stock_info_tencent(['01918','00337'], "HK")

