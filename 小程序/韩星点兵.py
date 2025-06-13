print("韩星点兵求人数")
w = int(input("请输入韩星的人数："))
while True:
    if w % 3  == 2 and w % 5 == 4 and w % 7 == 6:
        print("韩星点兵的人数为：", w)
        break
    else:
        s = w +1
        break
print("当前韩星点兵的人数为：", s)