import  random
# 平局次数
draw = 0
# 黑方犯规次数
blackno = 0
# 红方犯规次数
redno = 0
# 对局次数
w = 0
# 红方获胜次数
red = 0
# 黑方获胜次数
black = 0
e = input('输入开始即可开始比赛')
for i in range(30):
        if e == '开始':
            op = random.randint(1,6)
            if op == 6:
                print('平局')
                draw = 1
            elif op == 1:
                print('红方一分')
                red =+ 1
            elif op == 2:
                print('黑方一分')
                black +=1
            elif op == 3:
                print('红方犯规')
                redno += 1
            elif op == 4:
                print('黑方犯规')
                blackno +=1




p = input('"查看"可以查看比赛前情况')
if p == '查看':
  print(f'红队获胜{red}分\n'
      f'红队违规{redno}次\n'
      f'黑队获胜{black}分\n'
      f'黑队违规{blackno}次\n'
      f'平局{draw}次')