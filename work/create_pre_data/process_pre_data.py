#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

from pySql import pySql
import json

# 数据库连接
## 读取数据库信息
with open('db_info.json', 'r', encoding='utf-8') as f:
    db_info = json.load(f)
db_info = db_info['cscd']
db_server = pySql(ip=db_info['ip'], user=db_info['user'], pwd=db_info['pwd'], db=db_info['db'])

# 求和
SumUpSentencesNum = 0

def zng(paragraph):
    for sent in re.findall(u'[^！？。]+[！？。]?', paragraph, flags=re.U):
        yield sent


def is_dotInSentence(SentenceList, index):
    # 句中逗点，比如：带小数点的数字、缩略词等
    char_b1 = SentenceList[index - 1]
    char_a1 = SentenceList[index + 1]
    if ('0' <= char_b1 <= '9' or 'a' <= char_b1 <= 'z' or 'A' <= char_b1 <= 'Z') and ('0' <= char_a1 <= '9' or 'a' <= char_a1 <= 'z' or 'A' <= char_a1 <= 'Z' or char_a1 == '%' or char_a1 == ' ' or char_a1 == ')' or char_a1 == '）'):
        return True
    else:
        False


def delete_tag(eachSentence):
    delete_first7_chars = (' 背景与目的:', ' 背景与目的：')
    delete_first6_chars = ('背景与目的:', '背景与目的：', ' 背景与目的')
    delete_first5_chars = ('背景与目的',
                           ' 【讨论】', ' 【简介】', ' 【背景】', ' 【目的】', ' 【方法】', ' 【结果】', ' 【结论】',
                           ' [讨论]', ' [简介]', ' [背景]', ' [目的]', ' [方法]', ' [结果]', ' [结论]')
    delete_first4_chars = ('【讨论】', '【简介】', '【背景】', '【目的】', '【方法】', '【结果】', '【结论】',
                           '[讨论]', '[简介]', '[背景]', '[目的]', '[方法]', '[结果]', '[结论]',
                           ' 讨论：', ' 简介：', ' 背景：', ' 目的：', ' 方法：', ' 结果：', ' 结论：',
                           ' 讨论:', ' 简介:', ' 背景:', ' 目的:', ' 方法:', ' 结果:', ' 结论:',
                           ' 讨论·', ' 简介·', ' 背景·', ' 目的·', ' 方法·', ' 结果·', ' 结论·')
    delete_first3_chars = ('讨论：', '简介：', '背景：', '目的：', '方法：', '结果：', '结论：',
                           '讨论:', '简介:', '背景:', '目的:', '方法:', '结果:', '结论:',
                           '讨论·', '简介·', '背景·', '目的·', '方法·', '结果·', '结论·',
                           ' 讨论', ' 简介', ' 背景', ' 目的', ' 方法', ' 结果', ' 结论')
    # delete_first2_chars = ('讨论', '简介', '背景', '目的', '方法', '结果', '结论')
    if eachSentence.startswith(delete_first7_chars):
        eachSentence = eachSentence[7:]
    if eachSentence.startswith(delete_first6_chars):
        eachSentence = eachSentence[6:]
    if eachSentence.startswith(delete_first5_chars):
        eachSentence = eachSentence[5:]
    if eachSentence.startswith(delete_first4_chars):
        eachSentence = eachSentence[4:]
    if eachSentence.startswith(delete_first3_chars):
        eachSentence = eachSentence[3:]
    # if eachSentence.startswith(delete_first2_chars):
    #     eachSentence = eachSentence[2:]
    return eachSentence

# 读数据库，读一行，分一句
def ReadDb_SegmentSentence_Export2Txt(label2text):
    with open(label2text, 'r', encoding='utf-8') as f:
        cla_dict = json.load(f)
    for label, text in cla_dict.items():
    # for label, text in [('A','a')]:
        global SumUpSentencesNum
        previous_index = 0

        with open(label + '.txt', 'w', encoding='utf-8') as f:
            sql = "SELECT id,abstract FROM article_info where classification like '{cla_str}%' and language='chi' order by id".format(
                cla_str=label)
            df = db_server.read_sql(sql)

            for i in range(len(df)):
                paragraph = df.iloc[i]['abstract']
                SentencesList = list(zng(paragraph))
                dotSentence = []
                for eachSentence in SentencesList:
                    # 如果有".", 说明文中可能混用了英文分句符号，需要检查上下文。
                    if "." in eachSentence:
                        # is there "." in the tail of this sentence, yes!
                        if eachSentence[-1] == '.':
                            pass
                        # is there "." in the tail of this sentence, no!
                        elif eachSentence[-1] != '.':
                            eachSentence += '.'

                        # find all occurrences of “.” in this sentence
                        indexs_of_dots = [index for index, x in enumerate(eachSentence) if x == '.']

                        for i in indexs_of_dots:
                            index = i
                            # 句末？
                            if index == len(eachSentence)-1:
                                dotSentence.append(eachSentence[previous_index:-1])
                                break
                            # 句中逗点
                            elif is_dotInSentence(eachSentence, index):
                                continue
                            # 分句逗点
                            else:
                                dotSentence.append(eachSentence[previous_index:index + 1])
                                previous_index = index + 1

                        for sen in dotSentence:
                            sen = delete_tag(sen)
                            SumUpSentencesNum += 1
                            # print(sen, '第{}句'.format(SumUpSentencesNum))
                            f.write(sen + '\n')

                    # 如果没有".", 说明使用的是标准的中文符号，正常处理即可。
                    else:
                        sen = delete_tag(eachSentence)
                        SumUpSentencesNum += 1
                        # print(sen, '第{}句'.format(SumUpSentencesNum))
                        f.write(sen + '\n')
                previous_index = 0
                f.write('\n')
                if SumUpSentencesNum % 1000 == 0:
                    print(SumUpSentencesNum,' Done.')
        print(label , ' Done')
    print('句子总数:', SumUpSentencesNum)


if __name__ == '__main__':
    ReadDb_SegmentSentence_Export2Txt(r'cla_1_label2text_filter.json')

