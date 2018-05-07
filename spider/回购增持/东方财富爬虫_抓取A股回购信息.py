#-*- coding:utf-8 -*-
import requests
import pandas as pd
import sqlite3

from bs4 import BeautifulSoup

conn= sqlite3.connect("../../db/stock.db")

print("#####东方财富爬虫_抓取A股回购信息 开始#####")

cursor = conn.execute("SELECT max(日期) from aghg")
maxDateInTable = ""
for row in cursor:
    maxDateInTable = row[0]
if(not maxDateInTable):
    maxDateInTable = "2016-12-30"
# maxDateInTable = "2015-05-08"

url = 'http://ds.emoney.cn/DataCenter2/DataCenter/gphg_0?SortName=&SortFlag=&hidBlockName=&' \
      'hidStartDate=2015-05-08&hidEndDate=2100-12-30&hidStock=&BuybackProgress=&index=' #目标链接

def getTableTexts(p_url):
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

for i in range(1, 1000):
    fs = open('aghg.csv', 'w')
    fs.write("股票代码,股票名称,日期,回购进度,币种,股份类型,数量,金额,比例,价格上限,价格下限,用途,最新价,PE,是否破净\n")
    fs.write(getTableTexts(url))
    fs.close()

    pdRetData = pd.read_table("aghg.csv", sep=',')
    pdRetData = pdRetData.replace("--", 0)
    minDate = pdRetData['日期'].min()
    pdRetData['股票代码'] = pdRetData['股票代码'].apply(lambda x: str(x).zfill(6))
    print(minDate)
    if (minDate <= maxDateInTable):
        paRetData = pdRetData[pdRetData['日期'] > maxDateInTable]
        paRetData.to_sql('aghg', conn, if_exists='append', index=False)
        break
    else:
        pdRetData.to_sql('aghg', conn, if_exists='append', index=False)

conn.close()

print("#####东方财富爬虫_抓取A股回购信息 结束#####")

