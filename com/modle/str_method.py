# coding=gbk
__author__ = 'renfei'

name = "Swaroop"

if name.startswith("Swa"):
    print("name���� swa ��ͷ��")

if "a" in name:
    print("name ���� ��a��")

if name.find("war") != -1:
    print("name ���� war")

user = " lilei,hanmeimei"
print(user.strip())
print(user.lstrip())

print(user.index("i"))
print(user.title())