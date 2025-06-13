import random

s = input("请输入红包金额和人数(以空格分隔)：")
v =s.split(" ")

# 红包金额
ww = v[0]
# 人数
nn = v[1]



www = eval(input('1. 普通红包\n2. 拼手气红包\n 请输入选择：'))
wew = random.randint(1,int(ww))



#普通红包部分
if www == 1:
    print('普通红包:')
    monemj = int(ww) / int(nn)
    f = 0
    for i in range(int(monemj)):
        f += 1
        print(f'第{f}名{monemj}元')



#拼手气红包部分
elif www == 2:
    print('拼手气红包:')




