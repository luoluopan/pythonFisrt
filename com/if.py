# coding=gbk
__author__ = 'renfei'

number = 30
userNumber = int(input("input you number"))
if number == userNumber:
    print("输入的数字等于原来的数字")
elif userNumber > number:
    print("输入的数字大于原来的数字")
else:
    print("输入的数字小于原来的数字")
print("Done")
