# coding=gbk
__author__ = 'renfei'

change = 20
def func(change):
    print("���� change ��ֵΪ��",change)
    change = 2
    print("���� change ��ֵ �ı�Ϊ��",change)

def funcGlobal():
    global change
    print("���� change ��ֵΪ��",change)
    change = 10
    print("���� change ��ֵ Ϊ��",change)

#func(change)
funcGlobal()
print(change)
