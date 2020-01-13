#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/1/13 17:18


import pandas as pd
import os

def get_data(file_from,file_to,class_dict):
    with open(file_to,'w',encoding='utf-8') as fw:
        with open(file_from, 'r', encoding='utf-8') as f:
            sentences, tags = [],[]
            for line in f.readlines():
                line = line.strip()
                if not line:
                    if len(sentences) != 0:
                        i = 0
                        for sen in sentences:
                            fw.write(str(class_dict[tags[i]]) + '\t' + sen + '\n')
                            i += 1
                    sentences, tags = [], []
                elif not line.startswith("###"):
                    ls = line.split('\t')
                    tag, sen = ls[0], ls[1]
                    sentences.append(sen)
                    tags.append(tag)

if __name__ == '__main__':
    class_dict = {'OBJECTIVE': 0, 'METHODS': 1, 'RESULTS': 2, 'CONCLUSIONS': 3, 'BACKGROUND': 4}

    data_path = '../../data/data_refind/'
    ## create train data
    train_path = data_path
    if not os.path.exists(train_path):
        os.mkdir(train_path)

    get_data(data_path + 'new_train.txt', train_path + 'train_temp.tsv', class_dict)

    df_train = pd.read_csv(train_path + 'train_temp.tsv', sep='\t', names=['label', 'Sentence'])
    print(len(df_train))
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv(train_path + 'train.tsv', sep='\t', header=False, index=False)

    ## create test data
    test_path = data_path
    if not os.path.exists(test_path):
        os.mkdir(test_path)
    get_data(data_path + 'test_refind.txt', test_path + 'test.tsv', class_dict)







