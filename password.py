# coding: utf8
"""
Write a program that prompts the user to enter a password, and then prints
exactly one of the following messages: ‘The password is secure.’ or
‘The password is insecure!’. A secure password must meet the following
conditions:

* have at least one lowercase letter,
* have at least one capital letter,
* have at least one digit.

Examples:

Enter the password: Katar7yna
The password is secure.
Enter the password: catastrophe01
The password is insecure!

"""
password = input()

cap = "QWERTYUIOPASDFGHJKLZXCVBNM"
num ="1234567890"
low = 'qwertyuiopasdfghjklzxcvbnm'
c_num = 0
n_num = 0
l_num =0

result = str('')

for i in password:
    if i in cap:
        c_num += 1
    elif i in num:
        n_num += 1
    elif i in low: 
        l_num +=1

if c_num == 0 or n_num == 0 or l_num == 0:
    result = 'The password is insecure!'
else:
    result = 'The password is secure.'

print(result)