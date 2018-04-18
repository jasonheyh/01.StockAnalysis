import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('./stock.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''



sql = '''create table aghg (
        证券代码 VARCHAR(10),
        证券名称 VARCHAR(10),
        公告日期 DATE,
        回购进度 VARCHAR(20),
        币种 VARCHAR(10),
        股份类型 VARCHAR(2),
        数量 FLOAT ,
        金额 FLOAT ,
        比例 FLOAT ,
        价格上限 FLOAT ,
        价格下限 FLOAT ,
        用途 TEXT,
        最新价 FLOAT ,
        PE FLOAT ,
        是否破净 VARCHAR(5))'''

# create table stock_%s" % fileName[0:6] + "(日期 date, 股票代码 VARCHAR(10),     名称 VARCHAR(10),\
#                        收盘价 float,    最高价    float, 最低价 float, 开盘价 float, 前收盘 float, 涨跌额    float, \
#                        涨跌幅 float, 换手率 float, 成交量 bigint, 成交金额 bigint, 总市值 bigint, 流通市值 bigint)

cursor.execute(sql)

# '''使用游标关闭数据库的链接'''
cursor.close()
