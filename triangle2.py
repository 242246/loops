# coding: utf8
"""
Write a program that will ask the user for an integer (the size of the triangle)
and then print an isosceles triangle composed of `*` characters of the given
size. E.g:

Enter the size of the triangle: 3
  *
 ***
*****

"""
size = int(input('enter the size of the triangle'))

for i in range (1,size+1):
    print(' ' * (size - i) + '*'*(2*i-1))

