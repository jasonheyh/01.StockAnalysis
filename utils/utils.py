# -*- coding: utf-8 -*-

import sys
import json
import traceback
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .constant import *

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

