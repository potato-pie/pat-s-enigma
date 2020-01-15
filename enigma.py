# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:28:43 2020

@author: pat
"""
import numpy as np
from random import shuffle
import warnings
warnings.filterwarnings("ignore")

def roll_the_roter(roter):
    for i in range(len(roter)):
        if(roter[i] == 94):
            roter[i] = 0
        else:
            roter[i] = roter[i] + 1



ifreset = int(input("Reset the code? (type 0 for not reset, otherwise reset): "))

if(ifreset != 0):
    print("Reset the code...")
    
    mt_password1 = [i for i in range(95)]
    mt_password1 = np.array(mt_password1)
    shuffle(mt_password1)
    
    mt_password2 = [i for i in range(95)]
    mt_password2 = np.array(mt_password2)
    shuffle(mt_password2)
    
    mt_password3 = [i for i in range(95)]
    mt_password3 = np.array(mt_password3)
    shuffle(mt_password3)
    
    """
    real_tran_table = np.zeros((95),dtype=np.int)
    for i in range(95):
        num_fr = mt_password1[i]
        num_se = mt_password2[num_fr]
        num_thr = mt_password3[num_se]
        real_tran_table[i] = mt_password[num_thr];
    """
    
    np.savetxt("roter1.txt", mt_password1,fmt='%d',delimiter=',')
    np.savetxt("roter2.txt", mt_password2,fmt='%d',delimiter=',')
    np.savetxt("roter3.txt", mt_password3,fmt='%d',delimiter=',')
else:
    print("Use the original code")
    
    mt_password1 = np.loadtxt('roter1.txt',delimiter=',')
    mt_password1 = np.array(mt_password1)
    mt_password1 = mt_password1.astype(np.int32)
    
    mt_password2 = np.loadtxt('roter2.txt',delimiter=',')
    mt_password2 = np.array(mt_password2)
    mt_password2 = mt_password2.astype(np.int32)
    
    mt_password3 = np.loadtxt('roter3.txt',delimiter=',')
    mt_password3 = np.array(mt_password3)
    mt_password3 = mt_password3.astype(np.int32)
    
file = open("input_article.txt","r")
string_input = file.read()
file.close()
#string_input = input("Type put a sentence: ")
ascii_code = np.fromstring(string_input, dtype=np.uint8)
op_array = np.zeros((len(ascii_code)),dtype=np.int)

fr_caler = 0
se_caler = 0
thr_caler = 0

for i in range(len(ascii_code)):
    if(32 <= ascii_code[i] <= 126):
        now_code = ascii_code[i] - 32
        num_fr = mt_password1[now_code]
        num_se = mt_password2[num_fr]
        op_array[i] = mt_password3[num_se] + 32
        fr_caler = fr_caler + 1
        roll_the_roter(mt_password1)
        if(fr_caler == 95):
            fr_caler = 0
            se_caler = se_caler + 1
            roll_the_roter(mt_password2)
        if(se_caler == 95):
            se_caler = 0
            thr_caler = thr_caler + 1
            roll_the_roter(mt_password3)
        if(thr_caler == 95):
            thr_caler = 0
    else:
        op_array[i] = ascii_code[i]
        
op_string = ''
for i in range(len(op_array)):
    op_string = op_string + chr(op_array[i])

print(op_string)

with open('encrypted_message.txt','w+') as file:
    file.write(op_string)
file.close()