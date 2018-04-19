# -*- coding: utf-8 -*-
import tushare as ts
import lxml;
import requests
import pandas as pd
import sqlite3
import sys
csvPd = pd.read_csv('./stock.csv')
df1 = ts.get_stock_basics()
print(csvPd)
pd2 = df1[df1['name'].map(lambda x:x.replace(" ","")).isin(csvPd.stockName)]

pd2.to_csv("stockInfo.csv",encoding="utf-8")
# print(pd2.loc[:,['name','pe']])
print("終わりました")

# df1 = df1.loc[['603658','603228','601633','600816','600312','300516','300463','300026','300017','002833','002745','002701','002415','002294','002202'],['name','industry','area','pe','bvps','totalAssets']]
# print(df1)
# print(df1.to_json(orient='index'))



