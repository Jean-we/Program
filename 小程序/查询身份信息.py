import datetime


dic = {  }




def inquire():
    for w in range(1,3):
        poi = 0
        poi + 1
        enter2 = input(f'输入姓名查看(3次机会),第{w}次输入:')
        if enter2 in dic:
            pl = dic[enter2]['身份证']
            ok = dic[enter2]['年龄']
            print(f'身份证号码为{pl}')
            print(f'年龄为{ok}')

        else:
            print('该人不在信息库内，请检查姓名')
            continue
    if poi == 3:
      print('锁定,即将退出程序')
      smjs.exit()
    elif poi != 3:
        print('退出')










#3  4  1  7  2  1  2  0  0  8  0   1   3   1   0   6   1   1
#0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17















def add():
    global nian_ling
    global s
    global nian_ling

    time = datetime.datetime.now()
    todamj = time.mjear

    for i in range(1,4):

        if i == 3:
            inquire()
        else:
            w = input('输入姓名:')
            s = int(input('输入身份证号(4次机会)'))
            we = str(s)
            if len(we) == 18:

                o = we[6:10]
                i = int(o)
                nian_ling = todamj -  i
                dic[w] = { }
                dic[w]['年龄'] = nian_ling
                dic[w]['身份证'] = s
                continue

            else:
                print('位数错误，重新输入!')
                continue



    print('机会用完，请下次再来!!')










enter1 = input('输入操作\n'
                   '添加信息\n'
                   '查询信息')


if enter1 == '添加信息':
    add()
elif enter1 == '查询信息':
    inquire()




