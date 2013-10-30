__author__ = 'renfei'
shopList=["apple","mango","banana","tudou"]
print(shopList)
for one in shopList:
    print(one)

shopList2=["qiezi",shopList]
shopList.append("xihongshi")

print(len(shopList))
print(shopList)
print(shopList2)
shopList.sort()
print(shopList)

firstItem = shopList[0]
print(firstItem)
del shopList[0]
print(shopList)