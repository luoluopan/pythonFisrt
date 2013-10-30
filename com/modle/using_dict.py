# coding=gbk
__author__ = 'renfei'

ab = {"主站":"www.mapbar.com","企服":"mapx.mapbar.com","无线":"wireless.mapbar.com"}

print("主站的网址是 %s" % ab["主站"])
ab["酒店"]="hotel.mapbar.com"
del ab["主站"]
for name,url in ab.items():
    print("%s 的 网址 是 %s" % (name,url))

if "无线" in ab:
    print("无线的网址是：%s" % ab["无线"])

