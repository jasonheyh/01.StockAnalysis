import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('./stock.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''



sql = '''create table ggzc (
        日期 DATE ,
        市场代码 VARCHAR(10),
        名称 VARCHAR(10),
        名称缩写 VARCHAR(8),
        变动金额 LONG ,
        成交均价 FLOAT ,
        变动比例 FLOAT,
        变动人 VARCHAR(10),
        董监高人员姓名 TEXT,
        持股种类 VARCHAR(10),
        变动股数 LONG ,
        变动后持股数 LONG ,
        变动人与董监高的关系 VARCHAR(20),
        变动原因 TEXT,
        职务 VARCHAR(20),
        代码 VARCHAR(10))'''

# create table stock_%s" % fileName[0:6] + "(日期 date, 股票代码 VARCHAR(10),     名称 VARCHAR(10),\
#                        收盘价 float,    最高价    float, 最低价 float, 开盘价 float, 前收盘 float, 涨跌额    float, \
#                        涨跌幅 float, 换手率 float, 成交量 bigint, 成交金额 bigint, 总市值 bigint, 流通市值 bigint)

cursor.execute(sql)

# '''使用游标关闭数据库的链接'''
cursor.close()
