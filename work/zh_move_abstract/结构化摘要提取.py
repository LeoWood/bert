# coding: utf-8

from tqdm import tqdm
from Seg_Sents_Cn import Seg_Sents_Cn
# 设置分句的标志符号；可以根据实际需要进行修改
cutlist = "。"
# cutlist.decode('utf-8')
move_list = ['目的','方法','结果','结论']

def split_move(move,line):
    geshi_flag = 1
    results = ''
    if move + ' :' in line:
        results = line.split(move + ' :')
    elif '[' + move + ']' in line:
        results = line.split('[' + move + ']')
    elif move + ' ' in line:
        results = line.split(move + ' ')
    elif move + ':' in line:
        results = line.split(move + ':')
    elif move + '：' in line:
        results = line.split(move + '：')
    else:
        geshi_flag = 0
        # print('-------格式不对-------')
        # print(line)
    return geshi_flag, results


def extract_sen(line, id):
    output_lines = []
    output_lines.append('###' + str(id))
    flag = 1
    if line.startswith('目的 ') or line.startswith('目的:'):
        line = line[3:]
    elif line.startswith('[目的]') or line.startswith('目的 :'):
        line = line[4:]
    else:
        flag = 0
    # print(line)
    if flag:
        geshi_flag, move_sens = split_move('方法', line)
        # print('move_sens:', move_sens)
        if not geshi_flag:
            return line
        purpose = Seg_Sents_Cn(move_sens[0])
        # print('purpose:', purpose)
        for sen in purpose:
            if sen:
                output_lines.append('目的\t'+sen)
        
        geshi_flag, move_sens = split_move('结果', move_sens[1])
        if not geshi_flag:
            return line
        methods = Seg_Sents_Cn(move_sens[0])
        for sen in methods:
            if sen:
                output_lines.append('方法\t'+sen)

        geshi_flag, move_sens = split_move('结论', move_sens[1])
        if not geshi_flag:
            return line
        results = Seg_Sents_Cn(move_sens[0])
        for sen in results:
            if sen:
                output_lines.append('结果\t'+sen)
        
        conclusions = Seg_Sents_Cn(move_sens[1])
        for sen in conclusions:
            if sen:
                output_lines.append('结论\t'+sen)

        # print(str(id), ' 抽取完毕-----')
        #         # print(output_lines)
        #         # exit()
    else:
        # print('------------------非结构化摘要------------------')
        # print(line)
        return line
    return output_lines
    

#
# # 检查某字符是否分句标志符号的函数；如果是，返回True，否则返回False
# def FindToken(cutlist, char):
#     if char in cutlist:
#         return True
#     else:
#         return False
#
# def is_number(char):
#     if char >= '\u0030' and char <= '\u0039':
#         return True
#     else:
#         return False

# # 进行分句的核心函数
# def Cut(cutlist, lines):
#     l = []  # 句子列表，用于存储单个分句成功后的整句内容，为函数的返回值
#     line = []  # 临时列表，用于存储捕获到分句标志符之前的每个字符，一旦发现分句符号后，就会将其内容全部赋给l，然后就会被清空
#     k = 0
#     for i in lines:  # 对函数参数2中的每一字符逐个进行检查 （本函数中，如果将if和else对换一下位置，会更好懂）
#         # print(i)
#         if FindToken(cutlist, i):  # 如果当前字符是分句符号
#             # print('位于符号列表', i)
#             if i == '.':
#                 if k < len(lines)-1 and is_number(lines[k-1]) and is_number(lines[k+1]):
#                     line.append(i)  # 将此字符放入临时列表中
#                     # print(line)
#                 else:
#                     line.append(i)  # 将此字符放入临时列表中
#                     # print('得到的分句列表',line)
#                     l.append(''.join(line).strip())  # 并把当前临时列表的内容加入到句子列表中
#                     line = []  # 将符号列表清空，以便下次分句使用
#             else:
#                 line.append(i)  # 将此字符放入临时列表中
#                 # print('得到的分句列表', line)
#                 l.append(''.join(line).strip())  # 并把当前临时列表的内容加入到句子列表中
#                 line = []  # 将符号列表清空，以便下次分句使用
#         else:  # 如果当前字符不是分句符号，则将该字符直接放入临时列表中
#             line.append(i)
#         k += 1
#     return l

if __name__ == "__main__":
    # a = '研究胃癌高发区陕北安塞县幽门螺杆菌(Hp)感染与.血清胃蛋白酶原I(PGI)、胃蛋白酶原II(PGII)、PGI/PGII(PGR)以及胃泌素-17(G-17)浓度的相关性.'
    # print(Cut(cutlist,a))
    # exit()
    with open(r"structured abstracts(origin).txt",'r', encoding='utf-8') as f:
        with open(r"structured_abstract.txt",'w', encoding='utf-8') as fw:
            with open(r"other_abs.txt",'w', encoding='utf-8') as ff:
                id = 0
                for line in tqdm(f.readlines()):
                    line = line.strip()
                    output_lines = extract_sen(line,id)
                    if isinstance(output_lines,list):
                        for r in output_lines:
                            fw.write(r+'\n')
                        fw.write('\n')
                    else:
                        ff.write(str(id) + '\t' + line + '\n')
                    id += 1
                # exit()






# file = open(r"D:\zhao\bert\input_new\input_2000new\test.tsv",'r', encoding='utf-8')
# outfile = open(r"D:\zhao\bert\input_new\input_2000new\testnew.tsv","w", encoding='utf-8')
# file = open(r"D:\zhao\allyuliao\R.txt",'r', encoding='utf-8')
# outfile = open(r"D:\zhao\allyuliao\pre_training_5w.txt","w", encoding='utf-8')
# i = 0
# for lines in file:
#     # print(lines)
#     l = Cut(list(cutlist), list(lines))
#     # exit()
#     for line in l:
#         if line.strip() != "":
#             li = line.strip().split()
#             for sentence in li:
#                 outfile.write(sentence)
#         outfile.write('\n')
#     # print('\n')
#     outfile.write('\n')
#     i += 1
#     if i % 1000 == 0:
#         print(i,' Done')
#                 # print(sentence)
#     if i == 49999:
#         exit()
