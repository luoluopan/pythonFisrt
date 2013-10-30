# coding=gbk
__author__ = 'renfei'

pome = '''\
 	Programming is fun
	When the work is done
	if you wanna make your work also fun:
	????????use Python!
 '''

#f = open("pome.txt","w")   # open 跟 3.0 以前版本的file一样 打开 一个文件 w是打开模式 写 a是追加 r读  通过 help（open） 查看
#f.write(pome)              # 往文件 pome.txt 写入一句话 pome
#f.close()                  # 关闭 流

f2 = open("pome.txt","r")
while True:
    line = f2.readline()
    if len(line) == 0:
        break
    print(line)
f2.close()
