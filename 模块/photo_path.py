import os
from pygame import image


def photo_path(lu_jing: str,kemj: str,fu_mu_lu: str):

    # 列表存储图片相对路径
    pea_list = []
    for file_name in os.listdir(lu_jing):
        pea_list.append(file_name)
    # 翻转列表
    pea_list.reverse()
    '''

    按'.'分隔列表路径，变为嵌套列表，形如[   ['0','png'] , ['1','png']    ]

    '''
    new_pea_list = []
    for i in pea_list:
        new_pea_list.append(i.split('.'))


    # 冒泡排序对列表进行排序
    for list in range(0, len(new_pea_list)):
        for list in range(0, len(new_pea_list)):
            if list < len(new_pea_list)-1:
                if int(new_pea_list[list][0]) < int(new_pea_list[list + 1][0]):
                    continue
                elif int(new_pea_list[list][0]) > int(new_pea_list[list + 1][0]):
                    new_pea_list[list], new_pea_list[list + 1] = new_pea_list[list + 1], new_pea_list[list]
                    continue

    # 导入图片
    a = []  # 分隔出数字
    for t in new_pea_list:  # 升序排列的列表
        a.append(t[0])


    x = []  # 分隔出后缀
    for r in new_pea_list:
        x.append(r[1])
    '''
    数字列表和后缀列表组合，实现原先读取列表的形式，

    形如[     '0.png' , '1.png'  ]
    '''
    aa = [f'{num}.{ext}' for num, ext in zip(a, x)]

    '''
    定义文件夹名列表，防止路径错误
    '''
    vv = []
    for wer in range(len(aa)):
        vv.append(fu_mu_lu)

    for we in aa:
        '''
        将文件夹名和图片路径组合，形成半个绝对路径
        '''
        file_lu_jing = [f'{lp}/{wl}' for lp, wl in zip(vv, aa)]




    '''
    将file_lu_jing半个绝对路径列表转化成surface对象，并且存入file_lu_jing_dict字典，在显示画面上可以使用字典kemj作为访问，来访问值，也就是半个绝对路径!!!!!!!
    # '''
    file_lu_jing_dic = {}
    for mj in range(0, len(file_lu_jing)):
        a = image.load(f'{file_lu_jing[mj]}')
        file_lu_jing_dic[f'{kemj}{mj}'] = a



    return file_lu_jing_dic