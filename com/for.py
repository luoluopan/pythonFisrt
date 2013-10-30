# coding=gbk
# __author__ = 'renfei'
for i in range(1,5):     # range 是内建函数  从 遍历出 从 第一个数到第二个数  默认步长为 1，也可以用第三个参数来设置步长 ，range 包含 第一个数 不包含第二个数 [1,5)
    if i == 2:
        continue
    print(i)
    if i == 3:
        break
else:
    print("执行 for循环完成后 最后执行 else") # else 一定会执行，除非break 出 for循环