#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/10/6 10:05

from pySql import pySql
import json
from tqdm import tqdm


if __name__ == '__main__':
    ## 读取数据库信息
    with open('db_info.json', 'r', encoding='utf-8') as f:
        db_info = json.load(f)
    db_info = db_info['cscd']
    db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd=db_info['pwd'], db=db_info['db'])

    sql = "SELECT abstract FROM [CSCD].[dbo].[article_info] where abstract like '目的%'"

    df = db_server.read_sql(sql)
    with open('structured abstracts(origin).txt','w',encoding='utf-8') as f:
        for i in range(len(df)):
            f.write(df.iloc[i]['abstract'] + '\n')

    db_server.close()