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
    cla2num = {}

    i = 0
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\钍基\id2label.txt",'r',encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            [a,b,c,d,e] = line.split('\t')
            lable2id[b] = int(e)
            id2label[int(e)] = b
            num2id[int(d)] = int(e)

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\钍基\id2label.json", 'w', encoding='utf-8') as f:
        json.dump(id2label, f)
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\钍基\label2id.json", 'w', encoding='utf-8') as f:
        json.dump(lable2id, f)

        

    data = pd.read_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\钍基\data_new.xlsx")

    # # 入库数据
    # for i in range(len(data)):
    #     data.loc[i,"LabelID"] = num2id[data.iloc[i]["LabelID"]]
    # data.to_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\数据入库\data_tu.xlsx",sheet_name="文献数据", index=False)
    # exit()

    data["abstract"] = data["abstract"].str.replace("\n", '')
    data["abstract"] = data["abstract"].str.replace("\r", '')

    data = data[['LabelID','abstract']]
    data = data.dropna(axis=0,how='any')


    train_data = data.sample(frac=0.9, random_state=123)

    test_data = data[~data.index.isin(train_data.index)]

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\钍基\train.tsv", "w", encoding="utf-8") as f:
        for i in range(len(train_data)):
            abst = train_data.iloc[i]["abstract"].strip()
            if abst:
                f.write(str(num2id[train_data.iloc[i]["LabelID"]]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\钍基\test.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["abstract"].strip()
            if abst:
                f.write(str(num2id[test_data.iloc[i]["LabelID"]]) + "\t" + abst + "\n")
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\钍基\dev.tsv", "w", encoding="utf-8") as f:
        for i in range(len(test_data)):
            abst = test_data.iloc[i]["abstract"].strip()
            if abst:
                f.write(str(num2id[test_data.iloc[i]["LabelID"]]) + "\t" + abst + "\n")
    