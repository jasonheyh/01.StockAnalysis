import sqlite3

# '''创建一个数据库，文件名'''
conn = sqlite3.connect('../stock.db')
# '''创建游标'''
cursor = conn.cursor()

# '''执行语句'''



sql = '''create table yjyz (
        股票代码 VARCHAR(10),
        股票名称 VARCHAR(10),
        日期 DATE,
        预告类型 VARCHAR(10),
        业绩变动幅度_From_per FLOAT,
        业绩变动幅度_To_per FLOAT,
        市净率 FLOAT,
        市盈率 FLOAT,
        业绩变动 VARCHAR,
        每股收益_最新估算_元 VARCHAR,
        每股收益_上年同期_元 VARCHAR,
        流通股本_万股 FLOAT
        )'''

cursor.execute(sql)

cursor.close()
