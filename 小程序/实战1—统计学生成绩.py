import smjs

list1 = ['小明','小张','小李','小三','小肚','张月']
list2 = []

enter1 = input('输入操作：\n'
               '添加学生成绩\n'
               '查看学生成绩及最高低分、平均分')


def add():
    global list1,list2
    while True:
        w = input('输入要添加成绩学生:')
        if w in list1:
            e = float(input('输入成绩:'))
            list2.append(e)
            print('添加成功')
            p = input('"look"查看学生成绩\n'
                      '"回车"继续添加')
            if p == 'look':
                look_up()
            elif p == '':
                add()

        else:
            print('该人存在，重新输入')
            continue




def look_up():
    lp = sum(list2) / len(list2)
    print(f'最高分为{max(list2)}')
    print(f'最低分为{min(list2)}')
    print(f'平均分为{lp}')
    smjs.exit()


if enter1 == '添加学生成绩':
     add()
elif enter1 == '查看学生成绩':
     look_up()
