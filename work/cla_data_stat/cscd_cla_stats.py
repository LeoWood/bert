#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/11/15 16:25


from pySql import pySql
import json
import tqdm


def stat(label2text,isuni,output_file,db_server):
    with open(label2text,'r',encoding='utf-8') as f:
        cla_dict = json.load(f)
    cla_stats = {}
    i = 0
    for label,text in cla_dict.items():
        cla_str = label
        sql = "SELECT count(*) AS 'count' FROM article_info where classification like '{cla_str}%' and isUniCla={isuni} and language='chi'".format(
            cla_str=cla_str,isuni=isuni)
        df = db_server.read_sql(sql)
        cla_stats[label + ' ' + text] = df.iloc[0]['count']
        i += 1
        print(i, ' Done')

    cla_stats = sorted(cla_stats.items(), key=lambda x: x[1], reverse=True)
    print(cla_stats)

    with open(output_file, 'w', encoding='utf-8') as f:
        for key, value in cla_stats:
            f.write(key + '\t' + str(value) + '\n')

def is_chinese(char):
   if char >= '\u4e00' and char <= '\u9fa5':
        return True
   else:
        return False

if __name__ == '__main__':
    ## 读取数据库信息
    with open('db_info.json','r',encoding='utf-8') as f:
        db_info = json.load(f)
    db_info = db_info['cscd']
    db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd = db_info['pwd'], db = db_info['db'])


    # stat('med_cla_eng/label2text.json',1,'med_cla_eng/stats_cscd_med_eng.txt',db_server)
    stat(r'cla_agriculture/label2text.json',1,'cla_agriculture/stats_agri.txt',db_server)


    db_server.close()

