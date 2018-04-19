import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('../stock.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''



sql = '''create table hkhg (
        股票代码 VARCHAR(10),
        股票名称 VARCHAR(10),
        回购数量 NUMERIC,
        最高回购价 FLOAT,
        最低回购价 FLOAT,
        回购平均价 FLOAT,
        回购总额 NUMERIC,
        日期 DATE)'''

# create table stock_%s" % fileName[0:6] + "(日期 date, 股票代码 VARCHAR(10),     名称 VARCHAR(10),\
#                        收盘价 float,    最高价    float, 最低价 float, 开盘价 float, 前收盘 float, 涨跌额    float, \
#                        涨跌幅 float, 换手率 float, 成交量 bigint, 成交金额 bigint, 总市值 bigint, 流通市值 bigint)

cursor.execute(sql)

# '''使用游标关闭数据库的链接'''
cursor.close()
