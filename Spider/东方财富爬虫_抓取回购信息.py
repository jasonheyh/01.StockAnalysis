#-*- coding:utf-8 -*-

import requests
import json
#分级A的数据接口
r = requests.get(url='https://www.jisilu.cn/data/sfnew/funda_list/')
print(r.json())
print(r.json()['rows'])
print(r.json()['rows'][1]['cell']['next_recalc_dt'])
datas=r.json()['rows']   #打印解码后的返回数据
#把数据完全打印出来查看结构体

#print(json.dumps(datas, indent=3, ensure_ascii=False))

#打出所有的分级A代码，如果是A基金得到利率
for _data in datas:
    print(_data['cell']['funda_id'])
    print(_data['cell']['coupon_descr_s'])

#分级B 'https://www.jisilu.cn/data/sfnew/fundb_list/'
#母基 'https://www.jisilu.cn/data/sfnew/fundm_list/'