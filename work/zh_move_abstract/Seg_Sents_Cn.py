#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2020/1/12 17:05

import re

def zng(paragraph):
    for sent in re.findall(u'[^！？。]+[！？。]?', paragraph, flags=re.U):
        yield sent


def is_dotInSentence(Sentence, index):
    # 句中逗点，比如：带小数点的数字、缩略词等
    char_b1 = Sentence[index - 1]
    char_a1 = Sentence[index + 1]
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
    text = text.replace('．','.').strip()
    seg_sents = []
    if '。' in text:
        for sen in list(zng(text)):
            sen = delete_tag(sen)
            seg_sents.append(sen)
    else:
        previous_index = 0
        # find all occurrences of “.” in this sentence
        indexs_of_dots = [index for index, x in enumerate(text) if x == '.']

        # 先去掉末尾点号
        for index in indexs_of_dots:
            if index == len(text) - 1:
                indexs_of_dots.remove(index)

        # 去掉句中点号
        for index in indexs_of_dots:
            if is_dotInSentence(text,index):
                indexs_of_dots.remove(index)

        if not indexs_of_dots:
            text = delete_tag(text)
            return [text]

        # 加入头尾index
        indexs_of_dots = [0] + indexs_of_dots + [len(text) - 1]

        # 按点号位置切分
        for i in range(len(indexs_of_dots)-1):
            if i > 0:
                sen_temp = text[indexs_of_dots[i]+1: indexs_of_dots[i + 1]] + '.'
            else:
                sen_temp = text[indexs_of_dots[i]:indexs_of_dots[i+1]] + '.'
            sen_temp = delete_tag(sen_temp)
            seg_sents.append(sen_temp)


    # print(seg_sents)
    return seg_sents



if __name__ == '__main__':
    while True:
        text = input()
        print(Seg_Sents_Cn(text))
        for sen in Seg_Sents_Cn(text):
            print(sen + "\n")