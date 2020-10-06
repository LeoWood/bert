#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/5/12 17:04

import pandas as pd
import pymssql
import os
import sys
os.chdir(sys.path[0])

def get_data(file_from,file_to,class_dict):
    count = 0
    with open(file_to,'w',encoding='utf-8') as fw:
        with open(file_from, 'r', encoding='utf-8') as f:
            sentences, tags = [],[]
            for line in f.readlines():
                line = line.strip()
                if not line:
                    if len(sentences) != 0:
                        # print(sentences)
                        # print(tags)
                        # exit()
                        count += 1
                        i = 0
                        for sen in sentences:
                            num = len(sentences)
                            masked_abs = ''
                            mask = ' AAA ' + 'AAA ' * (num-2) + 'AAA. '
                            if i == 0:
                                masked_abs = mask + ' '.join(sentences[1:])
                            elif i == len(sentences) - 1:
                                masked_abs = ' '.join(sentences[:-1]) + mask
                            else:
                                masked_abs = ' '.join(sentences[:i]) + mask + ' '.join(sentences[i + 1:])
                            # print(masked_abs)
                            # fw.write(str(class_dict[tags[i]]) + '\t' + masked_abs + '\n')
                            fw.write(str(class_dict[tags[i]]) + '\t' + sen + '\n')
                            i += 1
                        if count == 100000:
                            return
                    sentences, tags = [], []
                elif not line.startswith("###"):
                    ls = line.split('\t')
                    tag, sen = ls[0], ls[1]
                    sentences.append(sen)
                    tags.append(tag)

def get_data_sens(file_from,file_to,class_dict):
    count = 0
    with open(file_to,'w',encoding='utf-8') as fw:
        with open(file_from, 'r', encoding='utf-8') as f:
            sentences, tags = [],[]
            for line in f.readlines():
                line = line.strip()
                if not line:
                    if len(sentences) != 0:
                        # print(sentences)
                        # print(tags)
                        # exit()
                        count += 1
                        i = 0
                        for sen in sentences:
                            # num = len(sentences)
                            # masked_abs = ''
                            # mask = ' AAA ' + 'AAA ' * (num-2) + 'AAA. '
                            # if i == 0:
                            #     masked_abs = mask + ' '.join(sentences[1:])
                            # elif i == len(sentences) - 1:
                            #     masked_abs = ' '.join(sentences[:-1]) + mask
                            # else:
                            #     masked_abs = ' '.join(sentences[:i]) + mask + ' '.join(sentences[i + 1:])
                            # print(masked_abs)
                            # fw.write(str(class_dict[tags[i]]) + '\t' + masked_abs + '\n')
                            fw.write(str(class_dict[tags[i]]) + '\t' + sen + '\n')
                            i += 1
                        # if count == 100000:
                        #     return
                    sentences, tags = [], []
                elif not line.startswith("###"):
                    ls = line.split('\t')
                    try:
                        tag, sen = ls[0], ls[1]
                    except:
                        print(line)
                        exit()
                    sentences.append(sen)
                    tags.append(tag)




if __name__ == '__main__':
    # conn = pymssql.connect(server="159.226.125.115", user="sa", password="whlibwlb00)$$", database="SemanticRT")
    # sql = "SELECT[loc],[Truelabel],[ArticleID],[Sentence]FROM [SemanticRT].[dbo].[Sentences_NewLabel] where ArticleID<=10000 and ArticleID>0"
    # df = pd.read_sql(sql, conn)
    # df_train = pd.read_csv('train/train.tsv', sep='\t', names=['label', 'Sentence'])
    # print(max([len(sen) for sen in df_train['Sentence']]))
    # exit()

    class_dict = {'目的':0, '方法':1, '结果':2, '结论':3}

    id2label = {'0':'目的',"1":"方法","2":"结果","3":"结论"}
    import json
    with open('id2label.json','w',encoding='utf-8') as f:
        json.dump(id2label,f)

    with open('label2id.json', 'w', encoding='utf-8') as f:
        json.dump(class_dict, f)
    exit()


    get_data_sens('structured_abstract.txt','data_all.tsv',class_dict)

    df = pd.read_csv('data_all.tsv',sep='\t',names=['label','Sentence'])

    df_train = df[:int(len(df)*0.99)]
    df_test = df[int(len(df)*0.99):]


    # print(max([len(sen.split(' ')) for sen in df_train['Sentence']]))
    print(len(df_train))
    # print(len(df_train.loc[df_train['label']==1]))
    df_train = df_train.sample(frac=1).reset_index(drop=True)
    df_train.to_csv('train.tsv',sep='\t',header=False,index=False)
    print(len(df_train))

    df_test = df_test.sample(frac=1).reset_index(drop=True)
    df_test.to_csv('test.tsv',sep='\t',header=False,index=False)
    print(len(df_test))


    exit()

    # df_train = pd.read_csv('test_temp.tsv', sep='\t', names=['label', 'Sentence'])
    # # print(max([len(sen.split(' ')) for sen in df_train['Sentence']]))
    # print(len(df_train))
    # # print(len(df_train.loc[df_train['label']==1]))
    # df_train = df_train.sample(frac=1).reset_index(drop=True)
    # df_train.to_csv('test.tsv', sep='\t', header=False, index=False)


