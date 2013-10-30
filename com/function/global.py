# coding=gbk
__author__ = 'renfei'

change = 20
def func(change):
    print("变量 change 的值为：",change)
    change = 2
    print("变量 change 的值 改变为：",change)

def funcGlobal():
    global change
    print("变量 change 的值为：",change)
    change = 10
    print("变量 change 的值 为：",change)

#func(change)
funcGlobal()
print(change)
