#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_data.py
@Time    :   2020/08/18 11:10:18
@Author  :   Leo Wood
@Contact :   leowood@foxmail.com
@Desc    :   None
'''

import json
import pandas as pd
import os
import sys
os.chdir(sys.path[0])

if __name__ == '__main__':
    df = pd.read_excel("训练数据.xlsx")
    df["分类"] = df["分类"].str.replace("\n", '')
    df["分类"] = df["分类"].str.replace("\r", '')

    df["dc:description"] = df["dc:description"].str.replace("\n", '')
    df["dc:description"] = df["dc:description"].str.replace("\r", '')


    lable2id = {}
    id2label = {}
    i = 0
    for label in set(df["分类"].tolist()):
        lable2id[label] = i
        id2label[i] = label
        i += 1

    with open('id2label.json', 'w', encoding='utf-8') as f:
        json.dump(lable2id, f)
    with open('label2id.json', 'w', encoding='utf-8') as f:
        json.dump(id2label, f)

    train_data = df.sample(frac=0.9, random_state=123)

    test_data = df[~df.index.isin(train_data.index)]

    # print(set(test_data["分类"].tolist()))

    with open("train.tsv", "w", encoding="utf-8") as f:
        for i in range(len(train_data)):
            # print(train_data.iloc[i])
            # print(lable2id[train_data.iloc[i]["分类"]])
            # print(train_data.iloc[i]["dc:description"])
            # exit()
            f.write(str(lable2id[train_data.iloc[i]["分类"]]) + "\t" + train_data.iloc[i]["dc:description"] + "\n")


    with open("test.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            f.write(str(lable2id[test_data.iloc[i]["分类"]]) + "\t" + test_data.iloc[i]["dc:description"] + "\n")
    with open("dev.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            f.write(str(lable2id[test_data.iloc[i]["分类"]]) + "\t" + test_data.iloc[i]["dc:description"] + "\n")
    print(df.head())
