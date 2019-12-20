#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/12/12 17:45


from pySql import pySql
import json
import tqdm
import pandas as pd


def create_data_old(cla_dict,isuni,db_server):

    cscd_label2id = {}
    cscd_id_label = {}

    i = 0
    for label,text in cla_dict.items():
        cla_str = label
        sql = "SELECT top 2000 title,abstract FROM article_info where classification like '{cla_str}%' and isUniCla={isuni}".format(
            cla_str=cla_str,isuni=isuni)
        df = db_server.read_sql(sql)
        abstracts = []
        for j in range(len(df)):
            flag = 0
            title = str(df.iloc[j]['title'])
            for s in title:
                if not is_chinese(s):
                    flag += 1
            ## 判断是否为中文摘要
            if flag == len(title):
                print(title)
                # exit()
                continue
            else:
                abstracts.append(df.iloc[j]['abstract'].strip().replace('\r','').replace('\n',''))
        with open('train_temp.tsv','a',encoding='utf-8') as f:
            for abst in abstracts:
                f.write(str(i) + '\t' + abst + '\n')
        cscd_id_label[i] = label + ' ' + text
        cscd_label2id[label + ' ' + text] = i
        i += 1

    with open('cscd_id_label.json','w',encoding='utf-8') as f:
        json.dump(cscd_id_label,f)
    with open('cscd_label2id.json', 'w', encoding='utf-8') as f:
        json.dump(cscd_label2id, f)

    df_train = pd.read_csv('train_temp.tsv', sep='\t', names=['label', 'Sentence'])

    print(len(df_train))
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv('train.tsv', sep='\t', header=False, index=False)


def create_data_1000(cla_dict,db_server):

    cscd_label2id = {}
    cscd_id_label = {}

    i = 0
    for label,text in cla_dict.items():
        sql = "SELECT top 1000 id,title,abstract FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi' and id not in (select id from cla_test_100) order by id".format(cla_str=label)
        df = db_server.read_sql(sql)
        df.to_csv('train_1000/' + label + text + '.csv', encoding='utf_8_sig')
        abstracts = []
        for j in range(len(df)):
            abstracts.append(df.iloc[j]['abstract'].strip().replace('\r','').replace('\n',''))
        with open('train_1000/train_temp.tsv','a',encoding='utf-8') as f:
            for abst in abstracts:
                f.write(str(i) + '\t' + abst + '\n')
        cscd_id_label[i] = label + ' ' + text
        cscd_label2id[label + ' ' + text] = i
        i += 1
        print(label, ' Done')

    with open('train_1000/cscd_id_label.json','w',encoding='utf-8') as f:
        json.dump(cscd_id_label,f)
    with open('train_1000/cscd_label2id.json', 'w', encoding='utf-8') as f:
        json.dump(cscd_label2id, f)

    df_train = pd.read_csv('train_1000/train_temp.tsv', sep='\t', names=['label', 'Sentence'])

    print(len(df_train))
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv('train_1000/train.tsv', sep='\t', header=False, index=False)

def create_data_2000(cla_dict,db_server):

    cscd_label2id = {}
    cscd_id_label = {}

    i = 0
    for label,text in cla_dict.items():
        sql = "SELECT top 2000 id,title,abstract FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi' and id not in (select id from cla_test_100) order by id".format(cla_str=label)
        df = db_server.read_sql(sql)
        df.to_csv('train_2000/' + label + text + '.csv', encoding='utf_8_sig')
        abstracts = []
        for j in range(len(df)):
            abstracts.append(df.iloc[j]['abstract'].strip().replace('\r','').replace('\n',''))
        with open('train_2000/train_temp.tsv','a',encoding='utf-8') as f:
            for abst in abstracts:
                f.write(str(i) + '\t' + abst + '\n')
        cscd_id_label[i] = label + ' ' + text
        cscd_label2id[label + ' ' + text] = i
        i += 1
        print(len(df))
        print(label, ' Done')

    with open('train_2000/cscd_id_label.json','w',encoding='utf-8') as f:
        json.dump(cscd_id_label,f)
    with open('train_2000/cscd_label2id.json', 'w', encoding='utf-8') as f:
        json.dump(cscd_label2id, f)

    df_train = pd.read_csv('train_2000/train_temp.tsv', sep='\t', names=['label', 'Sentence'])

    print(len(df_train))
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv('train_2000/train.tsv', sep='\t', header=False, index=False)

def create_data_3000(cla_dict,db_server):

    cscd_label2id = {}
    cscd_id_label = {}

    i = 0
    for label,text in cla_dict.items():
        sql = "SELECT top 3000 id,title,abstract FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi' and id not in (select id from cla_test_100) order by id".format(cla_str=label)
        df = db_server.read_sql(sql)
        df.to_csv('train_3000/' + label + text + '.csv', encoding='utf_8_sig')
        abstracts = []
        for j in range(len(df)):
            abstracts.append(df.iloc[j]['abstract'].strip().replace('\r','').replace('\n',''))
        with open('train_3000/train_temp.tsv','a',encoding='utf-8') as f:
            for abst in abstracts:
                f.write(str(i) + '\t' + abst + '\n')
        cscd_id_label[i] = label + ' ' + text
        cscd_label2id[label + ' ' + text] = i
        i += 1
        print(len(df))
        print(label, ' Done')

    with open('train_3000/cscd_id_label.json','w',encoding='utf-8') as f:
        json.dump(cscd_id_label,f)
    with open('train_3000/cscd_label2id.json', 'w', encoding='utf-8') as f:
        json.dump(cscd_label2id, f)

    df_train = pd.read_csv('train_3000/train_temp.tsv', sep='\t', names=['label', 'Sentence'])

    print(len(df_train))
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv('train_3000/train.tsv', sep='\t', header=False, index=False)

def create_data_level(cla_dict,db_server):
    cscd_label2id = {}
    cscd_id_label = {}

    i = 0
    for label, text in cla_dict.items():
        sql = "SELECT id,title,abstract FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi' and id not in (select id from cla_test_100) order by id".format(
            cla_str=label)
        df = db_server.read_sql(sql)

        num = len(df)

        if num >= 10000:
            df = df[:10000]
        elif num >= 5000:
            df = df[:5000]
        elif num >= 2000:
            df = df[:2000]

        df.to_csv('train_level/' + label + text + '.csv', encoding='utf_8_sig')
        abstracts = []
        for j in range(len(df)):
            abstracts.append(df.iloc[j]['abstract'].strip().replace('\r', '').replace('\n', ''))
        with open('train_level/train_temp.tsv', 'a', encoding='utf-8') as f:
            for abst in abstracts:
                f.write(str(i) + '\t' + abst + '\n')
        cscd_id_label[i] = label + ' ' + text
        cscd_label2id[label + ' ' + text] = i
        i += 1
        print(label, ' Done')

    with open('train_level/cscd_id_label.json', 'w', encoding='utf-8') as f:
        json.dump(cscd_id_label, f)
    with open('train_level/cscd_label2id.json', 'w', encoding='utf-8') as f:
        json.dump(cscd_label2id, f)

    df_train = pd.read_csv('train_level/train_temp.tsv', sep='\t', names=['label', 'Sentence'])

    print(len(df_train))
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv('train_level/train.tsv', sep='\t', header=False, index=False)


def is_chinese(char):
   if char >= '\u4e00' and char <= '\u9fa5':
        return True
   else:
        return False

def insert_into_test(db_server,cla_dict):
    for label,text in cla_dict.items():
        ### 写入数据库
        # sql = "insert into cla_test_100 SELECT top 100 * FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi'".format(
        #     cla_str=label)
        # db_server.write_sql(sql)
        sql = "SELECT top 100 id,paper_id,title,abstract,keyword FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi'".format(
            cla_str=label)
        df = db_server.read_sql(sql)
        df.to_csv('test/' + label + text + '.csv',encoding='utf_8_sig')
        print(label, ' Done.')



if __name__ == '__main__':
    # df_train = pd.read_csv('train_temp.tsv', sep='\t', names=['label', 'Sentence'])
    #
    # print(len(df_train))
    # exit()

    ## 读取数据库信息
    with open('db_info.json', 'r', encoding='utf-8') as f:
        db_info = json.load(f)
    db_info = db_info['cscd']
    db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd=db_info['pwd'], db=db_info['db'])

    with open('cla_cscd_filter_1/cla_cscd_label2text_filter.json','r',encoding='utf-8') as f:
        cla_dict = json.load(f)
    # create_data(cla_dict, 1, db_server)

    # insert_into_test(db_server,cla_dict)

    create_data_3000(cla_dict,db_server)

    db_server.close()