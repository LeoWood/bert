#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from pySql import pySql
from Seg_Sents_Cn import Seg_Sents_Cn
import json

数据库连接
# 读取数据库信息
with open('db_info.json', 'r', encoding='utf-8') as f:
    db_info = json.load(f)
db_info = db_info['cscd']
db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd=db_info['pwd'], db=db_info['db'])


# 读数据库
def ReadDb_SegmentSentence_Export2Txt(label2text):
    with open(label2text, 'r', encoding='utf-8') as f:
        cla_dict = json.load(f)
    count = 0
    for label, text in cla_dict.items():
        with open(label + '.txt', 'w', encoding='utf-8') as f:
            sql = "SELECT id,abstract FROM article_info where classification like '{cla_str}%' and language='chi' order by id".format(
                cla_str=label)
            df = db_server.read_sql(sql)
            for i in range(len(df)):
                abstract = df.iloc[i]['abstract']
                SentencesList = Seg_Sents_Cn(abstract)
                for sen in SentencesList:
                    f.write(sen)
                f.write('\n')
                count += 1

                if count % 100 == 0:
                    print(count,' Done.')
        print(label , ' Done')
    print('句子总数:', count)

def getsomememory(label2text):
    with open(label2text, 'r', encoding='utf-8') as f:
        cla_dict = json.load(f)
    count_1 = 0
    count_2 = 0
    for label, text in cla_dict.items():
        with open(label+'.txt','r',encoding='utf-8') as f:
            with open('../pre_data_raw/' + label+'.txt','w',encoding='utf-8') as fw:
                for line in f.readlines():
                    count_1 += 1
                    line = line.strip()
                    SentencesList = Seg_Sents_Cn(line)
                    for sen in SentencesList:
                        fw.write(sen + '\n')
                        count_2 += 1
                    fw.write('\n')
                    if count_1 % 1000 == 0:
                        print(count_1, ' Done.')
        print(label, ' Done')
    print(count_1)
    print(count_2)



if __name__ == '__main__':
    getsomememory(r'cla_1_label2text_filter.json')
    # ReadDb_SegmentSentence_Export2Txt(r'cla_1_label2text_filter.json')
 #    with open(r'cla_1_label2text_filter.json', 'r', encoding='utf-8') as f:
 #        cla_dict = json.load(f)
 #    for label, text in cla_dict.items():
 #        a = """python create_pretraining_data.py ^
 # --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
 # --output_file data/cscd_all/pre_training_{cla}_cscd_128.tfrecord ^
 # --input_file data/cscd_all/{cla}.txt ^
 # --max_seq_length 128""".format(cla=label)
 #        print(a)


