# coding=gbk
__author__ = 'renfei'

def printMax(a,b=5):
    if a > b:
        print(a,"是最大的数字")
    else:
        print(b,"是最大的数字")



def sendMail(user):
    print(user,"祝你节日快乐")

sendMail("胖子")

printMax(1)
