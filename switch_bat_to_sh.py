# -*- encoding:utf-8 -*-
import re
import os
import sys
os.chdir(sys.path[0])

def switch(bat_f,sh_f):
    with open(bat_f,'r',encoding='utf-8') as f:
        commond = f.read()

    commond = commond.replace('set ','export ')
    commond = commond.replace('^','\\')
    vars = re.findall('%.[^%]*%',commond)
    switch_vars = [v.replace('%','$')[:-1] for v in vars]
    for var,switch_var in zip(vars,switch_vars):
        commond = commond.replace(var,switch_var)
    print(commond)
    with open(sh_f,'w',encoding='utf-8') as f:
        f.write(commond)

if __name__ == '__main__':
    switch('Cla_yu.bat','Cla_yu.sh')

