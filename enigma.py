# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 09:28:43 2020

@author: pat
"""
import numpy as np
from random import shuffle
import warnings
warnings.filterwarnings("ignore")

ifreset = int(input("Reset the code? (type 0 for not reset, otherwise reset): "))

if(ifreset != 0):
    print("Reset the code...")
    mt_password = [i for i in range(95)]
    mt_password = np.array(mt_password)
    shuffle(mt_password)
    real_tran_table = np.zeros((95),dtype=np.int)
    
    for i in range(95):
        num_fr = mt_password[i]
        num_se = mt_password[num_fr]
        num_thr = mt_password[num_se]
        real_tran_table[i] = mt_password[num_thr];
    
    np.savetxt("real_tran_table.txt", real_tran_table,fmt='%d',delimiter=',')
else:
    print("Use the original code")
    real_tran_table = np.loadtxt('real_tran_table.txt',delimiter=',')
    real_tran_table = np.array(real_tran_table)
    real_tran_table = real_tran_table.astype(np.int32)
    
file = open("input_article.txt","r")
string_input = file.read()
file.close()
#string_input = input("Type put a sentence: ")
ascii_code = np.fromstring(string_input, dtype=np.uint8)
op_array = np.zeros((len(ascii_code)),dtype=np.int)

for i in range(len(ascii_code)):
    if(32 <= ascii_code[i] <= 126):
        now_code = ascii_code[i] - 32
        op_array[i] = real_tran_table[now_code] + 32
    else:
        op_array[i] = ascii_code[i]
        
op_string = ''
for i in range(len(op_array)):
    op_string = op_string + chr(op_array[i])

print(op_string)

with open('encrypted_message.txt','w+') as file:
    file.write(op_string)
file.close()