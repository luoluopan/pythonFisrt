# coding=gbk
__author__ = 'renfei'

ab = {"��վ":"www.mapbar.com","���":"mapx.mapbar.com","����":"wireless.mapbar.com"}

print("��վ����ַ�� %s" % ab["��վ"])
ab["�Ƶ�"]="hotel.mapbar.com"
del ab["��վ"]
for name,url in ab.items():
    print("%s �� ��ַ �� %s" % (name,url))

if "����" in ab:
    print("���ߵ���ַ�ǣ�%s" % ab["����"])

