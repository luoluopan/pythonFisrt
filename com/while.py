# coding=gbk
__author__ = 'renfei'

number = 30
running = True

while running:
    guess = int(input("������µ�����"))
    if guess == number:
        print("��ϲ�㣬�¶��ˣ�")
        running = False             # ���� ����ѭ���� ����
    elif guess > number:
        print("������������е��̫���ˣ�")
    else:
        print("�����������̫С�ˣ��������˲£�")
else:
    print("ִ���� while ѭ���󣬻�ִ�� while ���׵� else����")    # while ���� else����������ִ����� whileѭ���� ִ�е� ��Ҳ����˵ ֻҪ while��else ����ô������i���Ǹ���ִ�У����� ���while��ѭ��
print("Done")

