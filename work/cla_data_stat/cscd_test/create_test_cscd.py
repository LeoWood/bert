#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/12/21 16:34

import json
import os
import pandas as pd


if __name__ == '__main__':
    with open('../cla_cscd_filter_1/cla_cscd_label2text_filter.json','r',encoding='utf-8') as f:
        cla_dict = json.load(f)

    with open('cscd_label2id.json','r',encoding='utf-8') as f:
        cscd_label2id = json.load(f)

    with open('cscd_id2label.json','r',encoding='utf-8') as f:
        cscd_id2label = json.load(f)

    with open('test.tsv', 'w', encoding='utf-8') as fw:
        for label, text in cla_dict.items():
            print(label + text)
            # file_name =
            df = pd.read_csv('refind'+ '\\' +  label+text +'.csv')
            id = cscd_label2id[label + ' ' + text]
            for i in range(50):
                fw.write(str(id) + '\t' + df.iloc[i]['abstract'] + '\n')

