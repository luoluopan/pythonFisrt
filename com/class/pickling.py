# coding=gbk
__author__ = 'renfei'

import pickle as p

shopListFile = "shopList.data"

shopList = ["ƻ��","�㽶","����"]

#f = open(shopListFile,"wb")
#p.dump(shopList,f)
#f.close()


f = open(shopListFile,"rb")
storeList = p.load(f)
print(storeList)
