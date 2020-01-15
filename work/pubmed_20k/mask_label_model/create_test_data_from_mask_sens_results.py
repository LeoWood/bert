#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/1/15 15:03


import pandas as pd
import numpy as np

def get_nums(file_from):
    nums = []
    with open(file_from, 'r', encoding='utf-8') as f:
        sentences, tags = [],[]
        for line in f.readlines():
            line = line.strip()
            if not line:
                seq_len = len(sentences)
                if seq_len != 0:
                    nums.append(len(sentences))
                sentences, tags = [], []
            elif not line.startswith("###"):
                ls = line.split('\t')
                tag, sen = ls[0], ls[1]
                sentences.append(sen)
                tags.append(tag)
    return nums

if __name__ == '__main__':
    ## 读取masked sentece model的结果
    df = pd.read_csv('/home/leo/lh/Projects/bert/outputs/Move_mask_sens_refind/test_results.csv')
    print(len(df))
    ## 读取测试集
    df_test = pd.read_csv('/home/leo/lh/Projects/bert/data/data_refind/test.tsv', sep='\t', names=['label', 'Sentence'])
    print(len(df_test))
    # print(df_test.iloc[286030])
    # with open('abs_len.txt','r',encoding='utf-8') as f:
    #     nums = [int(line.strip()) for line in f.readlines()]
    ## 读取测试集原格式
    nums = get_nums('/home/leo/lh/Projects/bert/data/data_refind/test_refind.txt')
    print(len(nums))
    print(sum(nums))
    # exit()
    cla = {'0': 'Purpose', '1': 'Methods', '2': 'Results', '3': 'Conclusions', '4': 'Background'}
    i = 0
    with open('/home/leo/lh/Projects/bert/data/data_refind/data_mask_label/3_labels/test.tsv', 'w', encoding='utf-8') as fw:
        for num in nums:
            print(i,i+num)
            # 读取当前摘要预测得分
            results_temp = np.array(df[i:i+num]).tolist()
            max_list = []
            label_dict = {}
            k = 0
            for a in results_temp:
                m = max(a)
                max_list.append(m)
                label_dict[k] = cla[str(a.index(max(a)))]
                k += 1
            sor_max_list = sorted(max_list, reverse=True)
            rs = []
            ls = []
            for x in range(round(num*3/11)):
                i_i = max_list.index(sor_max_list[x])
                rs.append(i_i)
                ls.append(label_dict[i_i])


            # 读取原始句子和标签
            tags = []
            sentences = []
            for j in range(i,i+num):
                sentences.append(df_test.iloc[j]['Sentence'])
                tags.append(df_test.iloc[j]['label'])

            # 开始写入
            k = 0
            for sen in sentences:
                new_sens = {}
                for j in range(num):
                    new_sens[j] = '[...]. '  # 初始化一                # new_sens[rs[0]] = '[' + ls[0] + ']. '  # 选出来的两个位置用label替代
                # new_sens[rs[1]] = '[' + ls[1] + ']. '
                # new_sens[rs[2]] = '[' + ls[2] + ']. '个全是[...].的数组

                # for x in range(round(num * 3 / 11)):
                for x in range(3):
                    new_sens[rs[x]] = '[' + ls[x] + ']. '


                new_sens[k] = sentences[k] + ' '  # 句子本身保留
                masked_label_abs = ''
                for j in range(num):
                    masked_label_abs += new_sens[j]
                # print(masked_label_abs)
                fw.write(str(tags[k]) + '\t' + masked_label_abs + '\n')
                k += 1

            # print(results_temp)
            i += num
            # exit()


    print(nums)