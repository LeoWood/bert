#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/5/12 17:04

import pandas as pd
import pymssql
import random
import numpy as np


def stat_seq(file):
    seq_count = []
    with open(file,'r',encoding='utf-8') as f:
        sentences, tags = [],[]
        for line in f.readlines():
            line = line.strip()
            if not line:
                seq_len = len(sentences)
                seq_count.append(seq_len)
                sentences, tags = [], []
            elif not line.startswith("###"):
                ls = line.split('\t')
                tag, sen = ls[0], ls[1]
                sentences.append(sen)
                tags.append(tag)
    return seq_count


def get_data(file_from,file_to,class_dict):
    with open(file_to,'w',encoding='utf-8') as fw:
        with open(file_from, 'r', encoding='utf-8') as f:
            sentences, tags = [],[]
            for line in f.readlines():
                line = line.strip()
                if not line:
                    seq_len = len(sentences)
                    if seq_len != 0:
                        # print(sentences)
                        # print(tags)
                        # exit()
                        label_num = round(seq_len*3/11)
                        rs = sorted(random.sample(range(0,seq_len),label_num)) # 产生label_num个随机数，并排序

                        i = 0
                        for sen in sentences:
                            new_sens = {}
                            for j in range(seq_len):
                                new_sens[j] = '[...]. ' # 初始化一个全是[...].的数组
                            for k in range(label_num): # 选出来的label_num个位置用label替代
                                new_sens[rs[k]] = '[' + tags[rs[k]] + ']. '


                            new_sens[i] = sentences[i] + ' ' # 句子本身保留
                            masked_label_abs = ''
                            for j in range(seq_len):
                                masked_label_abs += new_sens[j]
                            fw.write(str(class_dict[tags[i]]) + '\t' + masked_label_abs + '\n')
                            i += 1
                    sentences, tags = [], []
                elif not line.startswith("###"):
                    ls = line.split('\t')
                    tag, sen = ls[0], ls[1]
                    sentences.append(sen)
                    tags.append(tag)


if __name__ == '__main__':
    # conn = pymssql.connect(server="159.226.125.115", user="sa", password="whlibwlb00)$$", database="SemanticRT")
    # sql = "SELECT[loc],[Truelabel],[ArticleID],[Sentence]FROM [SemanticRT].[dbo].[Sentences_NewLabel] where ArticleID<=10000 and ArticleID>0"
    # df = pd.read_sql(sql, conn)
    # seq_count = stat_seq('train_clean.txt')
    # print(seq_count)
    # print('mean: ',np.mean(seq_count))
    # print('median: ',np.median(seq_count))
    # print('max: ',max(seq_count))
    # print('min: ',min(seq_count))
    # exit()


    class_dict = {'OBJECTIVE':0, 'METHODS':1, 'RESULTS':2, 'CONCLUSIONS':3,'BACKGROUND':4}


    #
    ## create train data
    data_path = '../../data/data_refind/'
    train_path = data_path + 'data_mask_label/seq_length_nums'

    get_data(data_path + 'new_train.txt',train_path + 'train_temp.tsv',class_dict)

    df_train = pd.read_csv(train_path + 'train_temp.tsv',sep='\t',names=['label','Sentence'])
    # print(max([len(sen.split(' ')) for sen in df_train['Sentence']]))
    # print(len(df_train))

    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv(train_path + 'train.tsv',sep='\t',header=False,index=False)




    # exit()
    # df_train = pd.read_csv('test_temp.tsv', sep='\t', names=['label', 'Sentence'])
    # # print(max([len(sen.split(' ')) for sen in df_train['Sentence']]))
    # print(len(df_train))
    # # print(len(df_train.loc[df_train['label']==1]))
    # df_train = df_train.sample(frac=1).reset_index(drop=True)
    # df_train.to_csv('test.tsv', sep='\t', header=False, index=False)
    #
    # df_train = pd.read_csv('dev_temp.tsv', sep='\t', names=['label', 'Sentence'])
    # # print(max([len(sen.split(' ')) for sen in df_train['Sentence']]))
    # print(len(df_train))
    # # print(len(df_train.loc[df_train['label']==1]))
    # df_train = df_train.sample(frac=1).reset_index(drop=True)
    # df_train.to_csv('dev.tsv', sep='\t', header=False, index=False)


