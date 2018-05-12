# coding:utf-8
from datetime import timedelta, datetime

import IPython
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import charts
import json
import numpy as np
import tushare as ts

CONSTANT_COLUMN_YM = '年月'
CONST_COLUMN_DATE = '日期'

conn = sqlite3.connect("../../db/stock.db")

def ag_hgtj_company(p_base_data):
    '''
    A股的高管增持统计（根据公司）
    :return:
    '''
    CONST_TABLE_NAME = 'agzc'
    CONST_STOCK_NAME = "股票名称"
    CONST_SUM_COLUMN = '变动金额'
    p_base_data = p_base_data

    series = [{
        'type': 'column',
        'name': '增持金额',
        'data': [],
        "borderWidth": 0,
        "tooltip": {
            "headerFormat": '<span style="font-size:11px">{series.name}</span><br>',
            "pointFormat": '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}百万</b> of total<br/>'
        },
        "dataLabels": {
            "enabled": True,
            "rotation": -90,
            "color": '#FFFFFF',
            "align": 'right',
            "format": '{point.y:.1f}',
            "y": -30
        }
    }]

    pdData = pd.read_sql("SELECT * from " + CONST_TABLE_NAME + " where 日期 > '" + CONST_BASE_DATE + "' ", conn)
    sumPdData = pdData.groupby(CONST_STOCK_NAME).sum()
    # sumPdData = sumPdData.sort_values(by=CONST_SUM_COLUMN, ascending=False).head(30)
    sumPdData = sumPdData.sort_values(by=CONST_SUM_COLUMN, ascending=False)
    sumPdData[CONST_SUM_COLUMN] = sumPdData[CONST_SUM_COLUMN].apply(lambda x: round(x / 1000000, 2))
    df1 = ts.get_stock_basics()
    # list1 = sumPdData.index.tolist()
    # pd2 = df1[df1['name'].isin(list1)].sort_values(by='pe', ascending=False)
    sumPdData = sumPdData.reset_index()
    sumPdData = pd.merge(sumPdData, df1, how='inner', left_on=[CONST_STOCK_NAME], right_on=['name'])
    sumPdData = sumPdData[(sumPdData['pe'] < 35) & (sumPdData[CONST_SUM_COLUMN] > 1)].head(30)
    IPython.core.display.publish_display_data({'text/html': (sumPdData[['name', 'pe', 'industry', 'timeToMarket', CONST_SUM_COLUMN]]).to_html()})
    sumPdData = sumPdData.set_index(CONST_STOCK_NAME)
    options = {
        'title': {'text': '回购统计_公司'},
        'subtitle': {'text': ''},
        "xAxis": {
            "type": 'category',
            "crosshair": True
        },
        "yAxis": {
            # "min": 0,
            "title": {
                "text": '金额 (百万)'
            }
        }
    }
    totalHgMoney = []
    for key, value in sumPdData[CONST_SUM_COLUMN].to_dict().items():
        totalHgMoney.append([key, value])
    series[0]['data'] = totalHgMoney
    IPython.core.display.publish_display_data({'text/html': charts.plot(series, options=options, show='inline').data})

def ag_hgtj_hangye(p_base_data):
    '''
    A股的高管增持统计（根据行业）
    :return:
    '''
    CONST_TABLE_NAME = 'agzc'
    CONST_STOCK_NAME = "股票名称"
    CONST_SUM_COLUMN = '变动金额'
    CONST_BASE_DATE = p_base_data

    series = [{
        'type': 'column',
        'name': '增持金额',
        'data': [],
        "borderWidth": 0,
        "tooltip": {
            "headerFormat": '<span style="font-size:11px">{series.name}</span><br>',
            "pointFormat": '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}百万</b> of total<br/>'
        },
        "dataLabels": {
            "enabled": True,
            "rotation": -90,
            "color": '#FFFFFF',
            "align": 'right',
            "format": '{point.y:.1f}',
            "y": -30
        }
    }]

    pdData = pd.read_sql("SELECT * from " + CONST_TABLE_NAME + " where 日期 > '" + CONST_BASE_DATE + "' ", conn)
    sumPdData = pdData.groupby(CONST_STOCK_NAME).sum()
    sumPdData = sumPdData.sort_values(by=CONST_SUM_COLUMN, ascending=False)
    sumPdData[CONST_SUM_COLUMN] = sumPdData[CONST_SUM_COLUMN].apply(lambda x: round(x / 1000000, 2))
    df1 = ts.get_stock_basics()
    sumPdData = sumPdData.reset_index()
    sumPdData = pd.merge(sumPdData, df1, how='inner', left_on=[CONST_STOCK_NAME], right_on=['name'])
#     IPython.core.display.publish_display_data({'text/html': (sumPdData[['name', 'pe', 'industry', 'timeToMarket', CONST_SUM_COLUMN]]).to_html()})
    sumPdData = sumPdData.groupby('industry').sum()
    sumPdData = sumPdData.sort_values(by=CONST_SUM_COLUMN, ascending=True)
    sumPdData[CONST_SUM_COLUMN] = sumPdData[CONST_SUM_COLUMN].apply(lambda x: round(x, 1))
    options = {
        'title': {'text': '回购统计_行业'},
        'subtitle': {'text': ''},
        "xAxis": {
            "type": 'category',
            "crosshair": True
        },
        "yAxis": {
            "min": 0,
            # "title": {
                "text": '金额 (百万)'
            }
        }
    }
    totalHgMoney = []
    for key, value in sumPdData[CONST_SUM_COLUMN].to_dict().items():
        totalHgMoney.append([key, value])
    series[0]['data'] = totalHgMoney
    IPython.core.display.publish_display_data({'text/html': charts.plot(series, options=options, show='inline').data})


def ag_hgtj_month(p_base_data):
    '''
    A股的高管增持统计（根据月份）
    :return:
    '''
    CONST_TABLE_NAME = 'agzc'
    CONST_SUM_COLUMN = '变动金额'
    CONST_BASE_DATE = p_base_data

    series = [{
        'type': 'column',
        'name': '增持金额',
        'data': [],
        "borderWidth": 0,
        "tooltip": {
            "headerFormat": '<span style="font-size:11px">{series.name}</span><br>',
            "pointFormat": '<span style="color:{point.color}">{point.name}</span>: <b>{point.y}亿</b> of total<br/>'
        },
        "dataLabels": {
            "enabled": True,
            "rotation": -90,
            "color": '#FFFFFF',
            "align": 'right',
            "format": '{point.y:.1f}',
            "y": -30
        }
    }]

    pdData = pd.read_sql("SELECT * from " + CONST_TABLE_NAME + " where " + CONST_COLUMN_DATE + " > '" + CONST_BASE_DATE + "' ", conn)
    pdData[CONSTANT_COLUMN_YM] = pdData[CONST_COLUMN_DATE].apply(lambda x: x[0:7])
    sumPdData = pdData.groupby(CONSTANT_COLUMN_YM).sum()
    sumPdData[CONST_SUM_COLUMN] = sumPdData[CONST_SUM_COLUMN].apply(lambda x: round(x / 100000000, 2))
    options = {
        'title': {'text': '回购统计_月份'},
        'subtitle': {'text': ''},
        "xAxis": {
            "type": 'category',
            "crosshair": True
        },
        "yAxis": {
            # "min": 0,
            "title": {
                "text": '金额 (亿)'
            }
        },
    }
    totalHgMoney = []
    for key, value in sumPdData[CONST_SUM_COLUMN].to_dict().items():
        totalHgMoney.append([key, value])

    series[0]['data'] = totalHgMoney
    IPython.core.display.publish_display_data({'text/html': charts.plot(series, options=options, show='inline').data})


ag_hgtj_company('2018-04-01')
ag_hgtj_month('2015-07-01')
ag_hgtj_hangye('2018-04-01')