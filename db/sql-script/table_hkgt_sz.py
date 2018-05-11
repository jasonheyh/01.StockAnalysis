import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('../stock.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''



sql = '''create table hkgt_sz (
        日期 DATE,
        当日资金流入 FLOAT,
        当日余额	 FLOAT,
        历史资金累计流入 FLOAT,
        当日成交净买额 FLOAT,
        买入成交额 FLOAT,
        卖出成交额 FLOAT
        )'''

cursor.execute(sql)

cursor.close()
