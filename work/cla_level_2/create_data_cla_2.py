#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/12/12 17:45


from pySql import pySql
import json
import tqdm
import pandas as pd


def create_data(cla_dict,isuni,db_server):

    cla_2_train_label2id = {}
    cla_2_train_id2label = {}
    train_x = []
    train_y = []
    test_x = []
    test_y = []

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

        # # 判断该类别共有多少语料
        # num = len(abstracts)
        # if num < 130:
        #     continue
        # elif num < 1200:
        #     train_x += abstracts[:-30]
        #     test_x += abstracts[-30:]
        #     train_y = [i]*(num-30)
        #     test_y = [i]*30
        # elif num < 2200:
        #     train_x += abstracts[:-200]
        #     test_x += abstracts[-200:]
        #     train_y = [i] * (num - 200)
        #     test_y = [i] * 200
        # else:
        #     train_x += abstracts[:2000]
        #     test_x += abstracts[2000:2200]
        #     train_y = [i] * 2000
        #     test_y = [i] * 200
        #
        # print(len(train_x))
        # print(len(train_y))
        # print(len(test_x))
        # print(len(test_y))

        # exit()


    # cla_stats = sorted(cla_stats.items(), key=lambda x: x[1], reverse=True)
    # print(cla_stats)
    # with open(output_file, 'w', encoding='utf-8') as f:
    #     for key, value in cla_stats:
    #         f.write(key + '\t' + str(value) + '\n')

def is_chinese(char):
   if char >= '\u4e00' and char <= '\u9fa5':
        return True
   else:
        return False


if __name__ == '__main__':
    ## 读取数据库信息
    with open('db_info.json', 'r', encoding='utf-8') as f:
        db_info = json.load(f)
    db_info = db_info['cscd']
    db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd=db_info['pwd'], db=db_info['db'])

    with open('cla_cscd_label2text.json','r',encoding='utf-8') as f:
        cla_dict = json.load(f)
    create_data(cla_dict, 1, db_server)

    db_server.close()