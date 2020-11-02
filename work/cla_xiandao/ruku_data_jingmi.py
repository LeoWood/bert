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
    labeltail2id = {}
    i = 0
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\精密测量\id2label.txt",'r',encoding="utf-8") as f:
        for line in f.readlines():
            line = line.strip()
            [a,b,c] = line.split('\t')
            lable2id[b + '-' + a] = int(c)
            id2label[int(c)] = b + '-' + a
            labeltail2id[a] = int(c)
        print(id2label)
        print(lable2id)
        print(labeltail2id)
        # exit()

    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\精密测量\id2label.json", 'w', encoding='utf-8') as f:
        json.dump(id2label, f)
    with open(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\精密测量\label2id.json", 'w', encoding='utf-8') as f:
        json.dump(lable2id, f)


    
    data = pd.read_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\精密测量\data.xlsx")
    print(data.head())

    data["abstract"] = data["abstract"].str.replace("\n", '')
    data["abstract"] = data["abstract"].str.replace("\r", '')
    for i in range(len(data)):
        data.loc[i,"LabelID"] = labeltail2id[data.iloc[i]["LabelID"].strip()]
    data.to_excel(r"D:\UCAS\Phd\Projects\201804监测平台\先导专项-分类\数据入库\data_jingmi.xlsx",sheet_name="文献数据", index=False)

    exit()
    