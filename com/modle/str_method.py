# coding=gbk
__author__ = 'renfei'

name = "Swaroop"

if name.startswith("Swa"):
    print("name是以 swa 开头的")

if "a" in name:
    print("name 包含 ‘a’")

if name.find("war") != -1:
    print("name 包含 war")

user = " lilei,hanmeimei"
print(user.strip())
print(user.lstrip())

print(user.index("i"))
print(user.title())