import datetime
time = datetime.datetime.now()
hour = time.hour
minute = time.minute
n1 = float(input('输入峰时电度数：'))
n2 = float(input('输入谷时电度数:'))
v1 = 0.538 * (n1 + n2)
print(f'当前时间{hour}时{minute}分')
print(f'按传统用电标准算，电费{v1}元')
p = n1 * 0.568
l = n2 * 0.288
if 22 > hour > 8:
    if 50 > minute > 20:
      print(f'峰时电费为{p}元')
elif 8 > hour > 22:
    print(f'谷时电费为{l}元')
dwad = (p + l) - v1

print(f'一年时间，节省了{dwad}元')