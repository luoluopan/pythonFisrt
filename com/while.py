# coding=gbk
__author__ = 'renfei'

number = 30
running = True

while running:
    guess = int(input("输入你猜的数字"))
    if guess == number:
        print("恭喜你，猜对了！")
        running = False             # 设置 跳出循环的 条件
    elif guess > number:
        print("你输入的数字有点儿太大了！")
    else:
        print("你输入的数字太小了，再往大了猜！")
else:
    print("执行完 while 循环后，会执行 while 配套的 else条件")    # while 带的 else条件，是在执行完成 while循环后 执行的 ，也就是说 只要 while有else ，那么它将以i的那个会执行，除非 你的while死循环
print("Done")

