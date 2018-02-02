#!/usr/bin/python
# coding: UTF-8

import tushare as ts
import time
import pandas as pd

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

import matplotlib.pyplot as plt

# from pandas_datareader import data, wb
from datetime import datetime

# end = datetime.now()
# start = datetime(end.year - 1, end.month, end.day)
# alibaba = data.DataReader('BABA', 'yahoo', start, end)
# alibaba['Adj Close'].plot(legend=True, figsize=(10,4))
# plt.show()

print('数据来源版本:'+ts.__version__)

# #沪深300指数K线数据
# print(ts.get_hist_data('hs300'))
# #沪深300指数60分钟K线数据
# print(ts.get_hist_data('hs300',ktype='60'))

#复权数据
# #中通客车的前复权数据
# print(ts.get_h_data('000957'))
#
# #中通客车后复权数据
# print(ts.get_h_data('000957',autype='hfq'))

#中通客车不复权数据')
# print(ts.get_h_data('000957',autype=None))
#行业分类
# print('行业分类:\n',ts.get_industry_classified())
# #概念分类
# print('概念分类:\n',ts.get_concept_classified())
# #地域分类
# print('地域分类:\n',ts.get_area_classified())
# #创业板分类
# print('创业板分类:\n',ts.get_gem_classified())
# #风险警示板分类
# print('风险警示板分类:\n',ts.get_st_classified())
# #沪深300成分股及权重
# print('沪深300成分股及权重:\n',ts.get_hs300s())

#中通客车10日历史数据
# ztkchist = ts.get_hist_data('000957')
# print(ztkchist.tail(10))

# #中通客车周K线数据
# print(ts.get_hist_data('000957',ktype="W"))
# #中通客车月K线数据
# print(ts.get_hist_data('000957',ktype="M"))
# #中通客车5分钟K线
# print(ts.get_hist_data('000957',ktype='5'))
# #中通客车30分钟K线数据
# print(ts.get_hist_data('000957',ktype='30'))
# #中通客车60分钟K线数据
# print(ts.get_hist_data('000957',ktype='60'))

#中通客车实时报价
# ztkcrealtime = ts.get_realtime_quotes('000957')
# print(ztkcrealtime[['code','name','price','bid','ask','volume','amount','time']])

#中通客车大单交易,大单为500手
# ztkcdd=ts.get_sina_dd('000957',date='2017-04-28',vol=100)
# ztkcdd.to_excel("./中通客车20160805大单交易.xlsx")

#新股
# newts = ts.new_stocks()
# print(newts)

#沪市融资融券数据
zgpa_margin=ts.sh_margin_details(start='2017-01-01',end='2017-04-28', symbol='601318')
# print zgpa_margin.tail(10)
zgpa_history = ts.get_hist_data('601318',start='2017-01-01',end='2017-04-28')
# print zgpa_history.tail(10)
result = zgpa_margin.join(zgpa_history,on='opDate')
result.plot(legend=True, figsize=(10,4))
plt.show()
result.to_excel('./沪市融资融券数据.xlsx')
# print(ztkc_margin)

#信息地雷
# guba = ts.guba_sina(True)
# print(guba)
# print(guba.ix[1]['content'])

#个股信息地雷
# print(ts.get_notices('000957'))

#中通客车历史分笔数据
# ztkctick = ts.get_tick_data('000957','2016-08-05')
# print(ztkctick.head(100))

#当日所有股票
# all = ts.get_today_all()
# all.to_excel('./今日股票数据.xlsx')
# print(ts.get_today_all())