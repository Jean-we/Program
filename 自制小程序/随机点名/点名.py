import random
import tkinter as tk
from random import randint
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import Frame
from random import choices

from PIL import ImageTk, Image 


#创建画布1
root1 =  tk.Tk()
#尺寸
root1.geometry('450x350+730+350')
#标题
root1.title('24 internet💀')
#ikun/照片区域
kun = r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/ikun.jpeg'
img = Image.open(kun)
photo1 = ImageTk.PhotoImage(img.resize( (100,200) ))
top1 = tk.Label(root1,image=photo1)
#Red_bug/照片区域
red_bug = r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/Red_bug.jpeg'
img2 = Image.open(red_bug)
photo2 =ImageTk.PhotoImage(img2.resize( (108,104) ))
top2 = tk.Label(root1,image=photo2)
#标题
title = tk.Label(root1,text='点名程序',font=('SimHei',20,'bold') )




#画布权重/行
root1.rowconfigure(0,weight=6)
root1.rowconfigure(1,weight=6)
root1.rowconfigure(2,weight=6)
root1.rowconfigure(3,weight=6)
root1.rowconfigure(4,weight=6)
#画布权重/列
root1.columnconfigure(0,weight=6)
root1.columnconfigure(1,weight=6)
root1.columnconfigure(2,weight=6)
root1.columnconfigure(3,weight=6)
root1.columnconfigure(4,weight=6)



#名单文件
with open(r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/名单.txt','r',encoding='utf-8') as o:
    b = o.read()



#创建容器，显示在root上
ron_qi1 = Frame(root1)
#运行点名显示位置
ron_qi1.place(x=300,y=250)
#运行点名按钮
a1 = tk.Button(ron_qi1,text='点击运行')
a1.grid()


#创建容器，显示在root上
ron_qi2 = Frame(root1)
#查看显示位置
ron_qi2.place(x=310,y=60)
#查看按钮
a2 = tk.Button(ron_qi2,text='查看')
a2.grid()


#添加容器部分
rin_qi3 = tk.Frame(root1)
rin_qi3.place(x=310,y=110)
#添加按钮
a3 =tk.Button(rin_qi3,text='添加')
a3.grid()


#删除部分
ron_qi4 = tk.Frame(root1)
ron_qi4.place(x=310,y=180)
#删除按钮
a4 = tk.Button(ron_qi4,text='删除')
a4.grid()




#运行点名
def vote(e):
    with open(r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/名单.txt','r',encoding='utf-8') as h:
        lpo = h.read()
        #mki是列表
        mki = lpo.split()
        #权重
        if len(mki) > 32:
            quan_zhong = [3.428, 3.428, 3.428, 1, 3.428, 3.428, 3.428, 2.028, 3.428, 3.428, 3.428, 3.428, 3.428, 3.428,
                          3.428, 3.428, 3.428, 1, 3.428, 3.428, 3.428, 1, 3.428, 1, 3.428, 3.428, 3.428, 3.428, 3.428,
                          3.428, 3.428, 3.428]
            zeng_jia = int(len(mki)) - int(32)
            for i in range(zeng_jia):
                quan_zhong.append(3.428)


        elif len(mki) == 32:
            quan_zhong = [3.428,3.428,3.428,2,3.428,3.428,3.428,2.028,3.428,3.428,3.428,3.428,3.428,3.428,
                      3.428,3.428,3.428,2,3.428,3.428,3.428,2,3.428,1,3.428,3.428,3.428,3.428,3.428,
                      3.428,3.428,3.428]
        new_list1 = random.choices(mki,weights=quan_zhong)
    # 点击后弹出窗口
    messagebox.showinfo(title='结果',message=f'{new_list1[0]}')




#查看
def view(e):
    with open(r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/名单.txt', 'r', encoding='utf-8') as v:
        f = v.read()
    messagebox.showinfo(title='全部人员',message=f'{f}')




#添加
def add(e):
    new_name = simpledialog.askstring(title='添加', prompt='输入添加姓名:')
    if new_name == None:
        messagebox.showinfo(title='重输', message='重新输入')
    else:
            with open(r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/名单.txt','a',encoding='utf-8') as pl:
                pl.write(' ')
                pl.write(new_name)
                pl.flush()
                pl.close()
            messagebox.showinfo(title='添加',message=f'{new_name}添加成功')


#删除
def remove(e):
    remove_name = simpledialog.askstring(title='删除',prompt='输入删除姓名')
    if remove_name == None:
        messagebox.showinfo(title='重输',message='重新输入')
    else:
        with open(r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/名单.txt','r',encoding='utf-8') as m:
            lo = m.read()
        if remove_name not in lo:
            messagebox.showinfo(message=f'{remove_name}不存在，无法删除')
        else:
            with open(r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/名单.txt','r',encoding='utf-8') as w:
                quan_bu = w.read()
                #此时jie_guo就是列表
                jie_guo = quan_bu.split()
                jie_guo.remove(remove_name)
            with open(r'/Users/jeans/Desktop/python项目实战/自制小程序/随机点名/名单.txt','w',encoding='utf-8') as r:
                for l in jie_guo:
                    r.write(l)
                    r.write(' ')
                r.flush()
                r.close()
            messagebox.showinfo(message=f'{remove_name}删除成功')



shi_jain = ['<Button-1>']


#绑定事件/运行点名
a1.bind('<Button-1>',vote)


#绑定事件/查看
a2.bind('<Button-1>',view)


#绑定事件/添加
a3.bind('<Button-1>',add)

#绑定事件/删除
a4.bind('<Button-1>',remove)



#ikun/图片显示
top1.place(x=0,y=50)
#red_bus/图片显示
top2.place(x=210,y=80)





#一直显示
root1.mainloop()