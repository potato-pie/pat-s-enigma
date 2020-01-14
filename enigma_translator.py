# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:17:11 2020

@author: pat
"""
import numpy as np

#turing's bombe

#decode
file = open("encrypted_message.txt","r")
op_string = file.read()
file.close()
#op_string = input("Encrypted message: ")
readed_password = np.loadtxt('real_tran_table.txt',delimiter=',')
readed_password = np.array(readed_password)
readed_password = readed_password.astype(np.int32)
back_search_table = np.zeros((95),dtype=np.int)
for i in range(95):
    back_search_table[readed_password[i]] = i
    
decode_op = ''
decode_array = np.fromstring(op_string, dtype=np.uint8)
for i in range(len(decode_array)):
    if(32 <= decode_array[i] <= 126):
        decode_op = decode_op + chr(back_search_table[decode_array[i] - 32] + 32)
    else:
        decode_op = decode_op + chr(decode_array[i])

print(decode_op)

with open('translate_result.txt','w+',encoding='utf-8') as file:
    file.write(decode_op)
file.close()