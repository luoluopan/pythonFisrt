# coding=gbk
# __author__ = 'renfei'
for i in range(1,5):     # range ���ڽ�����  �� ������ �� ��һ�������ڶ�����  Ĭ�ϲ���Ϊ 1��Ҳ�����õ��������������ò��� ��range ���� ��һ���� �������ڶ����� [1,5)
    if i == 2:
        continue
    print(i)
    if i == 3:
        break
else:
    print("ִ�� forѭ����ɺ� ���ִ�� else") # else һ����ִ�У�����break �� forѭ��