#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/12/12 17:45


from pySql import pySql
import json
import tqdm
import pandas as pd
import os
import sys
os.chdir(sys.path[0])


def create_data(cla_dict,db_server,path):

    cscd_label2id = {}
    cscd_id_label = {}

    i = 0
    for label,text in cla_dict.items():
        if '*' in label:
            label_self = label.split('*')[0]
            label_not = label.split('*')[1].split(',')
            sql = "SELECT id,title,abstract,en_abstract FROM article_info where classification like '" + label_self + "%' "
            for l in label_not:
                sql += "and classification not like '" + l + "%' "
            sql += "and isUniCla=1 and language='chi'"
            print(sql)
            label = label_self
        else:
            sql = "SELECT id,title,abstract,en_abstract FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi'".format(cla_str=label)

        # if '*' in label:
        #     label = label.split('*')[0]
        #
        # sql = "SELECT id,title,abstract,en_abstract FROM article_info where classification like '{cla_str}%' and isUniCla=1 and language='chi' order by id".format(cla_str=label)
        df = db_server.read_sql(sql)
        df.to_csv(os.path.join('data_csv_temp', label + ' ' + text + '.csv'), encoding='utf_8_sig')

        df_train = df[:int(len(df)*0.9)]
        df_test = df[int(len(df)*0.9):]

        abstracts = []
        for j in range(len(df_train)):
            abst = df_train.iloc[j]['abstract'].strip().replace('\r', '').replace('\n', '')
            if abst != '':
                abstracts.append(abst)
        with open(os.path.join(path, 'train_temp.tsv'),'a',encoding='utf-8') as f:
            for abst in abstracts:
                f.write(str(i) + '\t' + abst + '\n')

        abstracts = []
        for j in range(len(df_test)):
            abst = df_test.iloc[j]['abstract'].strip().replace('\r', '').replace('\n', '')
            if abst != '':
                abstracts.append(abst)
        with open(os.path.join(path, 'test.tsv'), 'a', encoding='utf-8') as f:
            for abst in abstracts:
                f.write(str(i) + '\t' + abst + '\n')

        cscd_id_label[i] = label + ' ' + text
        cscd_label2id[label + ' ' + text] = i
        i += 1
        print(len(df))
        print(label, ' Done')

    with open(os.path.join(path, 'id2label.json'),'w',encoding='utf-8') as f:
        json.dump(cscd_id_label,f)
    with open(os.path.join(path, 'label2id.json'), 'w', encoding='utf-8') as f:
        json.dump(cscd_label2id, f)

    df_train = pd.read_csv(os.path.join(path, 'train_temp.tsv'), sep='\t', names=['label', 'Sentence'])

    print(len(df_train))

    df_test = pd.read_csv(os.path.join(path, 'test.tsv'), sep='\t', names=['label', 'Sentence'])
    df_test[:100].to_csv(os.path.join(path, 'data_example.csv'),index=False)

    print(len(df_test))

    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv(os.path.join(path, 'train.tsv'), sep='\t', header=False, index=False)





if __name__ == '__main__':
    # df_train = pd.read_csv('cla_agriculture/test.tsv', sep='\t', names=['label', 'Sentence'])
    #
    # print(len(df_train))
    # exit()

    ## 读取数据库信息
    with open('db_info.json', 'r', encoding='utf-8') as f:
        db_info = json.load(f)
    db_info = db_info['cscd']
    db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd=db_info['pwd'], db=db_info['db'])

    with open(r'temp_label2text.json','r',encoding='utf-8') as f:
        cla_dict = json.load(f)
    # create_data(cla_dict, 1, db_server)

    # insert_into_test(db_server,cla_dict)

    create_data(cla_dict,db_server,'data_bert_temp')

    db_server.close()