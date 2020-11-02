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
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\西南山地\id2label.txt",'r',encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            [a,b,c,d] = line.split('\t')

            lable2id[b] = int(d)
            id2label[int(d)] = b
            num2id[a] = int(d)

        print(id2label)
        print(lable2id)
        print(num2id)

        # exit()

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\西南山地\id2label.json", 'w', encoding='utf-8') as f:
        json.dump(id2label, f)
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\西南山地\label2id.json", 'w', encoding='utf-8') as f:
        json.dump(lable2id, f)


    
    data = pd.read_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\西南山地\data.xlsx")
    print(data.head())

    data["文献摘要"] = data["文献摘要"].str.replace("\n", '')
    data["文献摘要"] = data["文献摘要"].str.replace("\r", '')

    # # 入库数据
    # for i in range(len(data)):
    #     data.loc[i,"文献数据分类"] = num2id[data.iloc[i]["文献数据分类"].upper()]
    # data.to_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\数据入库\data_shandi.xlsx",sheet_name="文献数据", index=False)
    # exit()


    data = data[['文献数据分类','文献摘要']]
    data = data.dropna(axis=0,how='any')


    train_data = data.sample(frac=0.9, random_state=123)

    test_data = data[~data.index.isin(train_data.index)]

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\西南山地\train.tsv", "w", encoding="utf-8") as f:
        for i in range(len(train_data)):
            abst = train_data.iloc[i]["文献摘要"].strip()
            if abst:
                f.write(str(num2id[train_data.iloc[i]["文献数据分类"].upper()]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\西南山地\test.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["文献摘要"].strip()
            if abst:
                f.write(str(num2id[test_data.iloc[i]["文献数据分类"].upper()]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\西南山地\dev.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["文献摘要"].strip()
            if abst:
                f.write(str(num2id[test_data.iloc[i]["文献数据分类"].upper()]) + "\t" + abst + "\n")
    