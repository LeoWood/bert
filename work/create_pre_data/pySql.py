#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/11/15 16:25


import pymssql
import pandas as pd


class pySql:
    def __init__(self, ip, user, pwd, db):
        self.ip = ip
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = pymssql.connect(server=ip, user=user, password=pwd, database=db)

    def read_sql(self, sql):
        df = pd.read_sql(sql, self.conn)
        return df

    def write_sql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    import jieba
    import time
    t1 = time.time()
    jieba.load_userdict('Med_Keywords.txt')
    print([word for word in jieba.cut('hello world')])
    print('加载词典:', time.time()-t1)
    while True:
        text = input()
        print([word for word in jieba.cut(text)])
    exit()

    import json

    # 数据库连接
    ## 读取数据库信息
    with open('db_info.json', 'r', encoding='utf-8') as f:
        db_info = json.load(f)
    db_info = db_info['cscd']
    db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd=db_info['pwd'], db=db_info['db'])

    sql = " SELECT distinct obj2.keyword FROM [CSCD].[dbo].[article_info] obj1,[CSCD].[dbo].[article_keywords] obj2 where obj1.paper_id=obj2.paper_id and obj1.classification like 'R%'"
    df = db_server.read_sql(sql)
    from tqdm import tqdm
    with open('Med_Keywords.txt','w',encoding='utf-8') as f:
        for i in tqdm(range(len(df))):
            f.write(df.iloc[i]['keyword'] + '\n')

