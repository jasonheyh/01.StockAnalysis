#-*- coding:utf-8 -*-

import requests
import json
import pandas as pd
import csv, sqlite3
conn= sqlite3.connect("../../db/stock.db")

print("#####东方财富爬虫_抓取A股高管增持信息 开始#####")

cursor = conn.execute("SELECT max(日期) from agzc")
maxDateInTable = ""
for row in cursor:
    maxDateInTable = row[0]
if(not maxDateInTable):
    maxDateInTable = "2017-01-01"
# maxDateInTable = "2017-01-01"

#分级A的数据接口
for i in range(1, 10000):
    url = 'http://datainterface.eastmoney.com/EM_DataCenter/JS.aspx?type=GG&sty=GGMX&p=' + str(i) + '&ps=100'
    r = requests.get(url=url)
    retData = r.text.replace("\"])", "").replace("([\"","").replace("\",\"","\n")
    # print(retData)
    with open('agzc.csv', 'w') as fs:
        fs.write("变动比例,变动人,代码,董监高人员姓名,持股种类,日期,变动股数,变动后持股数,成交均价,名称,变动人与董监高的关系,名称缩写,变动原因,变动金额,职务,市场代码\n")
        fs.writelines(retData)
    paRetData = pd.read_table("agzc.csv",sep=',')
    # print(paRetData)
    # paRetData.to_sql('huigou', conn, if_exists='append', index=False)
    paRetData['代码'] = paRetData['代码'].apply(lambda x: str(x).zfill(6))
    minDate = paRetData['日期'].min()
    print(minDate)
    if (minDate <= maxDateInTable):
        paRetData = paRetData[paRetData['日期'] > maxDateInTable]
        paRetData.to_sql('agzc', conn, if_exists='append', index=False)
        break
    else:
        paRetData.to_sql('agzc', conn, if_exists='append', index=False)

conn.close()

print("#####东方财富爬虫_抓取A股高管增持信息 结束#####")

