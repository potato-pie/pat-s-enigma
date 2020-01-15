# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:17:11 2020

@author: pat
"""
import numpy as np

def roll_the_roter(roter):
    for i in range(len(roter)):
        if(roter[i] == 94):
            roter[i] = 0
        else:
            roter[i] = roter[i] + 1

#decode
file = open("encrypted_message.txt","r")
op_string = file.read()
file.close()
#op_string = input("Encrypted message: ")
readed_password1 = np.loadtxt('roter1.txt',delimiter=',')
readed_password1 = np.array(readed_password1)
readed_password1 = readed_password1.astype(np.int32)

readed_password2 = np.loadtxt('roter2.txt',delimiter=',')
readed_password2 = np.array(readed_password2)
readed_password2 = readed_password2.astype(np.int32)

readed_password3 = np.loadtxt('roter3.txt',delimiter=',')
readed_password3 = np.array(readed_password3)
readed_password3 = readed_password3.astype(np.int32)

idx_list1 = np.argsort(readed_password1)
idx_list2 = np.argsort(readed_password2)
idx_list3 = np.argsort(readed_password3)

fr_caler = 0
se_caler = 0
thr_caler = 0

decode_op = ''
decode_array = np.fromstring(op_string, dtype=np.uint8)

for i in range(len(decode_array)):
    if(32 <= decode_array[i] <= 126):
        now_code = decode_array[i] - 32
        num_fr = idx_list3[now_code]
        num_se = idx_list2[num_fr]
        decode_op = decode_op + chr(idx_list1[num_se] + 32)
        fr_caler = fr_caler + 1
        roll_the_roter(readed_password1)
        idx_list1 = np.argsort(readed_password1)
        if(fr_caler == 95):
            fr_caler = 0
            se_caler = se_caler + 1
            roll_the_roter(readed_password2)
            idx_list2 = np.argsort(readed_password2)
        if(se_caler == 95):
            se_caler = 0
            thr_caler = thr_caler + 1
            roll_the_roter(readed_password3)
            idx_list3 = np.argsort(readed_password3)
        if(thr_caler == 95):
            thr_caler = 0
    else:
        decode_op = decode_op + chr(decode_array[i])

print(decode_op)

with open('translate_result.txt','w+',encoding='utf-8') as file:
    file.write(decode_op)
file.close()
