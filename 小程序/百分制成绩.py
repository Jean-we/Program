a = float(input('输入成绩：'))

if a > 100 or a < 0:
    print('输入错误')
elif 100 > a > 90:
    print('成等级为A')
elif 89 > a > 80:
    print('成绩等级为B')
elif 79 > a > 70:
    print('成绩等级为C')
elif 69 > a > 60:
    print('成绩等级为D')
elif a < 60 :
    print('成绩等级为E')