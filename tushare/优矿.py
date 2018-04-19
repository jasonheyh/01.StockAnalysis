#!/usr/bin/python
# coding: UTF-8

import seaborn
from matplotlib import pylab
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
from CAL.PyCAL import *    # CAL.PyCAL中包含font
from datetime import timedelta,datetime
import time
import scipy.stats as st
cal=Calendar('China.SSE')


def buylist(input_account_date, universe0):
    calDate = Date.fromDateTime(input_account_date)
    xgstart = cal.advanceDate(calDate, '-180B', BizDayConvention.Preceding)
    xgend = cal.advanceDate(calDate, '-0B', BizDayConvention.Preceding)
    buylistall = []
    bylist = []
    # time_all=['-100B','-110B','-120B','-130B','-140B','-150B']
    for i in universe0:
        try:
            df = DataAPI.MktEquwAdjAfGet(secID=i, beginDate=xgstart, endDate=xgend,
                                         field=u"secID,closePrice,turnoverVol", pandas="1")
            dfprice = df.closePrice.tolist()
            dfvol = df.turnoverVol.tolist()
            if dfprice[-1] > max(dfprice[:-1]) and 1.618 > dfprice[-1] / min(
                    dfprice) > 1.2:  # and dfprice[-6]<max(dfprice[:-5]) and sum(dfvol[-4:])/4>sum(dfvol[-8:-4])/4 and 1.6>dfprice[-1]/min(dfprice)>1.2:
                buylistall.append(i)
        except:
            pass
    if len(buylistall) > 3:
        stock_info = DataAPI.MktStockFactorsOneDayGet(tradeDate=input_account_date, secID=buylistall,
                                                      field=u"secID,tradeDate,pe,ROE", pandas="1")
        stock_info['EP'] = 1.0 / stock_info.PE
        stock_info['EPrank'] = stock_info.EP.rank()
        stock_info['ROErank'] = stock_info.ROE.rank()
        stock_info['allrank'] = stock_info.EPrank + stock_info.ROErank
        stock_px = stock_info.sort('allrank', ascending=False)
        bylist = stock_px[:3].secID.tolist()
    else:
        bylist = buylistall
    return bylist


start = '2012-01-01'  # 回测起始时间
end = '2017-05-12'  # 回测结束时间
benchmark = 'HS300'  # 策略参考标准 '000016.ZICN'
universe = StockScreener(Factor.PE.value_range(10, 60))  # DynamicUniverse('A')  # 证券池，支持股票和基金
capital_base = 1000000  # 起始资金
freq = 'd'  # 策略类型，'d'表示日间策略使用日线回测，'m'表示日内策略使用分钟线回测
refresh_rate = Weekly(1)  # 调仓频率，表示执行handle_data的时间间隔，若freq = 'd'时间间隔的单位为交易日，若freq = 'm'时间间隔为分钟
commission = Commission(buycost=0.0003, sellcost=0.0013)


# list(set(StockScreener( Factor.OperatingRevenueGrowRate.value_range(0.3,None) )).union(set(StockScreener( Factor.PE.value_range(10,50) ))))
def initialize(account):  # 初始化虚拟账户状态
    account.value_counter = {}
    pass


def handle_data(account):  # 每个交易日的买入卖出指令
    # print account.current_date
    '''
    for stk in account.security_position.keys():  # 记录持仓的天数
        if account.day_counter.has_key(stk):
            account.day_counter[stk] += 1
        else:
            account.day_counter[stk] = 1
    '''
    # print len(account.security_position.keys()),len(account.day_counter.keys()),account.current_date
    # hc
    hcbuylist = buylist(account.current_date, account.universe)
    # hcbuylist=Rzmr(hc1buylist,account.current_date)
    # print account.current_date,hcbuylist
    if '000024.XSHE' in hcbuylist:
        hcbuylist.remove('000024.XSHE')
    # 记录最大
    for v in account.value_counter.keys():
        if v not in account.security_position.keys():
            account.value_counter.pop(v)

    for u in account.security_position.keys():
        if u not in account.value_counter.keys():
            account.value_counter[u] = [account.security_position[u] * account.security_cost[u]]
        else:
            account.value_counter[u].append(account.security_position[u] * account.reference_price[u])

    for k in account.security_position.keys():
        if account.security_position[k] * account.reference_price[k] / max(account.value_counter[k]) - 1 < -0.07 or \
                                account.reference_price[k] / account.security_cost[k] > 1.25:
            order_pct_to(k, 0)

    nwbuylist = list(set(hcbuylist) - set(account.security_position.keys()))
    # if len(account.security_position)>5:
    # nwbuylist=[]
    if len(nwbuylist) > 0:
        percent = min(1.0 / len(nwbuylist), 0.2)
        for stkj in nwbuylist:
            order_pct(stkj, percent)
    #
    print nwbuylist, account.current_date
    return
