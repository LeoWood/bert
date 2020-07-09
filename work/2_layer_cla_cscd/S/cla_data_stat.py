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
        if '*' in label:
            label_self = label.split('*')[0]
            label_not = label.split('*')[1].split(',')
            sql = "SELECT count(*) AS 'count' FROM article_info where classification like '" + label_self + "%' "
            for l in label_not:
                sql += "and classification not like '" + l + "%' "
            sql += "and isUniCla=1 and language='chi'"
            print(sql)
        else:
            sql = "SELECT count(*) AS 'count' FROM article_info where classification like '{cla_str}%' and isUniCla={isuni} and language='chi'".format(cla_str=label,isuni=isuni)

        df = db_server.read_sql(sql)
        cla_stats[label + ' ' + text] = df.iloc[0]['count']
        i += 1
        # print(label, ' Done')

    # cla_stats = sorted(cla_stats.items(), key=lambda x: x[1], reverse=True)
    # print(cla_stats)
    count = 0

    with open(output_file, 'w', encoding='utf-8') as f:
        for key, value in cla_stats.items():
            f.write(key + '\t' + str(value) + '\n')
            count += value
            print(key + '\t' + str(value))
        print(count)
        f.write(str(count))


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

    stat_str = "modified"
    ## 构架映射表
    cla_label2text = {}

    with open(stat_str + '_category.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                if '\t' in line:
                    line = line.split('\t')[0]
                try:
                    cla_label2text[line.split(' ')[0]] = line.split(' ')[1]
                except:
                    print(line)
                    exit()

    with open(stat_str + '_label2text.json', 'w', encoding='utf-8') as f:
        json.dump(cla_label2text, f)


    stat(stat_str + '_label2text.json',1,stat_str + '_stat.txt',db_server)


    db_server.close()

