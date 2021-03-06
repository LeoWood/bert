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
    num2id = {}

    i = 0
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\印太\id2label.txt",'r',encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            [a,b,c] = line.split('\t')

            lable2id[a] = int(c)
            id2label[int(c)] = a
            num2id[int(b)] = int(c)

        print(id2label)
        print(lable2id)
        print(num2id)

        # exit()

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\印太\id2label.json", 'w', encoding='utf-8') as f:
        json.dump(id2label, f)
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\印太\label2id.json", 'w', encoding='utf-8') as f:
        json.dump(lable2id, f)


    
    data = pd.read_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\印太\data.xls")
    print(data.head())

    data["文献摘要"] = data["文献摘要"].str.replace("\n", '')
    data["文献摘要"] = data["文献摘要"].str.replace("\r", '')
    data = data[['文献数据分类','文献摘要']]
    data = data.dropna(axis=0,how='any')


    train_data = data.sample(frac=0.9, random_state=123)

    test_data = data[~data.index.isin(train_data.index)]

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\印太\train.tsv", "w", encoding="utf-8") as f:
        for i in range(len(train_data)):
            abst = train_data.iloc[i]["文献摘要"].strip()
            if abst:
                f.write(str(num2id[train_data.iloc[i]["文献数据分类"]]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\印太\test.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["文献摘要"].strip()
            if abst:
                f.write(str(num2id[test_data.iloc[i]["文献数据分类"]]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\印太\dev.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["文献摘要"].strip()
            if abst:
                f.write(str(num2id[test_data.iloc[i]["文献数据分类"]]) + "\t" + abst + "\n")
    