#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/12/12 11:10
import json

def is_chinese(char):
   if char >= '\u4e00' and char <= '\u9fa5':
        return True
   else:
        return False

if __name__ == '__main__':
    cla_1 = {0: 'A 马克思主义、列宁主义、毛泽东思想、邓小平理论', 1: 'B 哲学、宗教', 2: 'C 社会科学总论', 3: 'D 政治、法律', 4: 'E 军事', 5: 'F 经济',
             6: 'G 文化、科学、教育、体育', 7: 'H 语言、文字', 8: 'I 文学', 9: 'J 艺术', 10: 'K 历史、地理', 11: 'N 自然科学总论', 12: 'O 数理科学和化学',
             13: 'P 天文学、地球科学', 14: 'Q 生物科学', 15: 'R 医药卫生', 16: 'S 农业科学', 17: 'U 交通运输', 18: 'V 航空、航天', 19: 'X 环境科学、安全科学',
             20: 'TB 一般工业技术', 21: 'TD 矿业工程', 22: 'TE 石油、天然气工业', 23: 'TF 冶金工程', 24: 'TG 金属学与金属工艺', 25: 'TH 机械、仪表工业',
             26: 'TJ 武器工业', 27: 'TK 能源与动力工程', 28: 'TL 原子能技术', 29: 'TM 电工技术', 30: 'TN 无线电电子学、电信技术', 31: 'TP 自动化技术、计算机技术',
             32: 'TQ 化学工业', 33: 'TS 轻工业、手工业', 34: 'TU 建筑科学', 35: 'TV 水利工程'}

    cla_2_r = {0: 'R1 预防医学、卫生学', 1: 'R2 中国医学', 2: 'R3 基础医学', 3: 'R4 临床医学', 4: 'R5 内科学', 5: 'R6 外科学', 6: 'R71 妇产科学',
               7: 'R72 儿科学', 8: 'R73 肿瘤学', 9: 'R74 神经病学与精神病学', 10: 'R75 皮肤病学与性病学', 11: 'R76 耳鼻咽喉科学', 12: 'R77 眼科学',
               13: 'R78 口腔科学', 14: 'R8 特种医学', 15: 'R9 药学'}

    cla_3_r = {0: 'R11卫生基础科学', 1: 'R12环境卫生、环境医学', 2: 'R13劳动卫生', 3: 'R14放射卫生', 4: 'R15营养卫生、食品卫生', 5: 'R16个人卫生',
               6: 'R169计划生育与卫生', 7: 'R17妇幼卫生', 8: 'R179儿童、少年卫生', 9: 'R18流行病学与防疫', 10: 'R19保健组织与事业（卫生事业管理）',
               11: 'R2-0中国医学理论', 12: 'R21中医预防、卫生学', 13: 'R22中医基础理论', 14: 'R24中医临床学', 15: 'R25中医内科', 16: 'R26中医外科',
               17: 'R271中医妇产科', 18: 'R272中医儿科', 19: 'R273中医肿瘤科', 20: 'R274中医骨伤科', 21: 'R275中医皮科', 22: 'R276中医五官科',
               23: 'R277中医其他学科', 24: 'R28中药学', 25: 'R289方剂学', 26: 'R29中国少数民族医学', 27: 'R31医用一般医学', 28: 'R32人体形态学',
               29: 'R33人体生理学', 30: '[R34]人体生物化学、分子生物学', 31: 'R36病理学', 32: 'R37医学微生物学（病原细菌学、病原微生物学）', 33: 'R38医学寄生虫学',
               34: 'R392医学免疫学', 35: 'R394医学遗传学', 36: 'R395医学心理学、病理心理学', 37: 'R44诊断学', 38: 'R45治疗学', 39: 'R47护理学',
               40: 'R48临终关怀学', 41: 'R49康复医学', 42: 'R51传染病', 43: 'R52结核病', 44: 'R53寄生虫病', 45: 'R54心脏、血管（循环系）疾病',
               46: 'R55血液及淋巴系疾病', 47: 'R56呼吸系及胸部疾病', 48: 'R57消化系及腹部疾病', 49: 'R58内分泌腺疾病及代谢病', 50: 'R59全身性疾病',
               51: 'R61外科手术学', 52: 'R62整形外科学（修复外科学）', 53: 'R63外科感染', 54: 'R64创伤外科学', 55: 'R65外科学各论',
               56: 'R68骨科学（运动系疾病、矫形外科学）', 57: 'R69泌尿科学（泌尿生殖系疾病）', 58: 'R711妇科学', 59: 'R713妇科手术', 60: 'R714产科学',
               61: 'R715临床优生学', 62: 'R719产科手术', 63: 'R720.5儿科治疗学', 64: 'R722新生儿、早产儿疾病', 65: 'R723婴儿的营养障碍',
               66: 'R725小儿内科学', 67: 'R726小儿外科学', 68: 'R730一般性问题', 69: 'R733造血器及淋巴系肿瘤', 70: 'R734呼吸系肿瘤',
               71: 'R735消化系肿瘤', 72: 'R736内分泌腺肿瘤', 73: 'R737泌尿生殖器肿瘤', 74: 'R738运动系肿瘤', 75: 'R739.4神经系肿瘤',
               76: 'R739.5皮肤肿瘤', 77: 'R739.6耳鼻咽喉肿瘤', 78: 'R739.8口腔、颌面部肿瘤', 79: 'R741神经病学', 80: 'R749精神病学',
               81: 'R751皮肤病学', 82: 'R759性病学', 83: 'R764耳科学、耳疾病', 84: 'R765鼻科学、鼻疾病', 85: 'R766咽科学、咽疾病',
               86: 'R767喉科学、喉疾病', 87: 'R772眼纤维膜疾病', 88: 'R774视网膜及视神经疾病', 89: 'R775眼压与青光眼', 90: 'R776晶状体与玻璃体疾病',
               91: 'R777眼附属器官疾病', 92: 'R778眼屈光学', 93: 'R779.6眼外科手术学', 94: 'R780.1口腔疾病的预防与卫生', 95: 'R780.2口腔病理学',
               96: 'R781口腔内科学', 97: 'R782口腔颌面部外科学', 98: 'R783口腔矫形学', 99: 'R788儿童口腔疾病', 100: 'R81放射医学', 101: 'R82军事医学',
               102: 'R85航空航天医学', 103: 'R91药物基础科学', 104: 'R917药物分析', 105: 'R92药典、药方集（处方集）、药物鉴定', 106: 'R93生药学（天然药物学）',
               107: 'R94药剂学', 108: 'R95药事组织', 109: 'R96药理学', 110: 'R97药品', 111: 'R99毒物学（毒理学）'}

    cla_2_r = {0: 'R1 预防医学、卫生学', 1: 'R2 中国医学', 2: 'R3 基础医学', 3: 'R4 临床医学', 4: 'R5 内科学', 5: 'R6 外科学', 6: 'R71 妇产科学',
               7: 'R72 儿科学', 8: 'R73 肿瘤学', 9: 'R74 神经病学与精神病学', 10: 'R75 皮肤病学与性病学', 11: 'R76 耳鼻咽喉科学', 12: 'R77 眼科学',
               13: 'R78 口腔科学', 14: 'R8 特种医学', 15: 'R9 药学'}

    new_dict = {}
    for key,value in cla_2_r.items():
        new_dict[str(key)] = value

    with open('id2label.json','w',encoding='utf-8') as f:
        json.dump(new_dict,f)
    exit()

    # cla_1_label2text = {}
    # with open('cla_1_label2text.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         # print(value.split())
    #         cla_1_label2text[value.split()[0]] = value.split()[1]
    #     json.dump(cla_1_label2text,f)
    #
    # cla_1_label2id = {}
    # with open('cla_1_label2id.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_1_label2id[value.split()[0]] = key
    #     json.dump(cla_1_label2id, f)
    #
    # cla_1_id2label = {}
    # with open('cla_1_id2label.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_1_id2label[key] = value.split()[0]
    #     json.dump(cla_1_id2label, f)
    #
    # cla_2_r_label2text = {}
    # with open('cla_2_r_label2text.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_2_r_label2text[value.split()[0]] = value.split()[1]
    #     json.dump(cla_2_r_label2text, f)
    #
    # cla_2_r_label2id = {}
    # with open('cla_2_r_label2id.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_2_r_label2id[value.split()[0]] = key
    #     json.dump(cla_2_r_label2id, f)
    #
    # cla_2_r_id2label = {}
    # with open('cla_2_r_id2label.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_2_r_id2label[key] = value.split()[0]
    #     json.dump(cla_2_r_id2label, f)
    #

    label2text = {}
    for key, value in cla_3_r.items():
        i = 0
        for s in value:
            if is_chinese(s):
                cla_3_r[key] = value[:i] + ' ' + value[i:]
                label2text[value[:i] ] = value[i:]
                break
            i += 1

    print(cla_3_r)
    print(label2text)
    with open('med_cla_eng/id2label.json','w',encoding='utf-8') as f:
        json.dump(cla_3_r,f)
    with open('med_cla_eng/label2text.json','w',encoding='utf-8') as f:
        json.dump(label2text,f)
    exit()



    #
    # cla_3_r_label2text = {}
    # with open('cla_3_r_label2text.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_3_r_label2text[value.split()[0]] = value.split()[1]
    #     json.dump(cla_3_r_label2text, f)
    #
    # cla_3_r_label2id = {}
    # with open('cla_3_r_label2id.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_3_r_label2id[value.split()[0]] = key
    #     json.dump(cla_3_r_label2id, f)
    #
    # cla_3_r_id2label = {}
    # with open('cla_3_r_id2label.json', 'w', encoding='utf-8') as f:
    #     for key, value in cla_1.items():
    #         cla_3_r_id2label[key] = value.split()[0]
    #     json.dump(cla_3_r_id2label, f)

    ## 全部二级类

    # cla_2_label2text = {}
    #
    # with open('cla_data_stat.txt','r',encoding='utf-8') as f:
    #     for line in f.readlines():
    #         line = line. strip()
    #         if line:
    #             cla_2_label2text[line.split()[0]] = line.split()[1]
    #
    # with open('cla_2_label2text.json', 'w', encoding='utf-8') as f:
    #     json.dump(cla_2_label2text,f)

    # cla_cscd_label2text = {}
    #
    # with open('cla_cscd.txt', 'r', encoding='utf-8') as f:
    #     for line in f.readlines():
    #         line = line.strip()
    #         if line:
    #             cla_cscd_label2text[line.split()[0]] = line.split()[1]
    #
    # with open('cla_cscd_label2text.json', 'w', encoding='utf-8') as f:
    #     json.dump(cla_cscd_label2text, f)

    cla_cscd_label2text = {}

    with open('physics_cla/cla_cscd_phy_2.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                cla_cscd_label2text[line.split()[0]] = line.split()[1]

    with open('physics_cla/cla_cscd_phy_2_label2text.json', 'w', encoding='utf-8') as f:
        json.dump(cla_cscd_label2text, f)




