#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/1/12 17:05

import re

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
        return False

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
                           ' 讨论', ' 简介', ' 背景', ' 目的', ' 方法', ' 结果', ' 结论','目的 ', '方法 ', '结果 ', '结论 ')
    delete_first2_chars = ('简介', '背景', '目的', '方法', '结果','结论')
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
    if eachSentence.startswith(delete_first2_chars) and not eachSentence.startswith('结果表明'):
        eachSentence = eachSentence[2:]
    return eachSentence

def Seg_Sents_Cn(text):
    seg_sents = []
    if '。' in text:
        for sen in list(zng(text)):
            sen = delete_tag(sen)
            seg_sents.append(sen)
    else:
        previous_index = 0
        # find all occurrences of “.” in this sentence
        indexs_of_dots = [index for index, x in enumerate(text) if x == '.']

        for index in indexs_of_dots:
            if index == len(text) - 1:  ## 位于最后
                sen = text[previous_index:]
                sen = delete_tag(sen)
                seg_sents.append(sen)
            elif is_dotInSentence(text, index): ## 句中的句点
                continue
            else:
                sen = text[previous_index:index + 1]
                sen = delete_tag(sen)
                seg_sents.append(sen)
                previous_index = index + 1

    print(seg_sents)
    return seg_sents




if __name__ == '__main__':
    while True:
        text = input()
        Seg_Sents_Cn(text)