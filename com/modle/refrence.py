__author__ = 'renfei'
shopList=["apple","mango","banana","tudou"]
myList=shopList
del shopList[0:1]
print(myList)
print(shopList)

myList=shopList[:]
del shopList[0]
print(myList)
print(shopList)
