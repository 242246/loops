# coding: utf8
"""
Write a program that prompts user to enter some text and prints the number
of CAPITAL LETTERS on the screen. E.g:

Enter text: Data Science is SUPER!
7

"""
sentence = str(input())

num = 0
letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for i in sentence:
    if i in letters:
        num += 1

print(num)


