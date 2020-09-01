#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_data.py
@Time    :   2020/09/01 11:47:24
@Author  :   Leo Wood 
@Contact :   leowood@foxmail.com
@Desc    :   None
'''

import pandas as pd
import json


if __name__ == '__main__':
    lable2id = {}
    id2label = {}
    i = 0
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\上海药物所\id2label.txt",'r',encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            [a,b,c] = line.split('\t')
            lable2id[c + '-' + b] = int(a)
            id2label[int(a)] = c + '-' + b
        print(id2label)
        print(lable2id)
        # exit()

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\上海药物所\id2label.json", 'w', encoding='utf-8') as f:
        json.dump(id2label, f)
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\上海药物所\label2id.json", 'w', encoding='utf-8') as f:
        json.dump(lable2id, f)
    exit()

    
    data = pd.read_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\上海药物所\data.xlsx")
    print(data.head())

    data["abstract"] = data["abstract"].str.replace("\n", '')
    data["abstract"] = data["abstract"].str.replace("\r", '')



    train_data = data.sample(frac=0.9, random_state=123)

    test_data = data[~data.index.isin(train_data.index)]

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\上海药物所\train.tsv", "w", encoding="utf-8") as f:
        for i in range(len(train_data)):
            abst = train_data.iloc[i]["abstract"].strip()
            if abst:
                f.write(str(train_data.iloc[i]["LabelID"]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\上海药物所\test.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["abstract"].strip()
            if abst:
                f.write(str(test_data.iloc[i]["LabelID"]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\上海药物所\dev.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["abstract"].strip()
            if abst:
                f.write(str(test_data.iloc[i]["LabelID"]) + "\t" + abst + "\n")
    