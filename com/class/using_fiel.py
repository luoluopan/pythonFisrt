# coding=gbk
__author__ = 'renfei'

pome = '''\
 	Programming is fun
	When the work is done
	if you wanna make your work also fun:
	????????use Python!
 '''

#f = open("pome.txt","w")   # open �� 3.0 ��ǰ�汾��fileһ�� �� һ���ļ� w�Ǵ�ģʽ д a��׷�� r��  ͨ�� help��open�� �鿴
#f.write(pome)              # ���ļ� pome.txt д��һ�仰 pome
#f.close()                  # �ر� ��

f2 = open("pome.txt","r")
while True:
    line = f2.readline()
    if len(line) == 0:
        break
    print(line)
f2.close()
