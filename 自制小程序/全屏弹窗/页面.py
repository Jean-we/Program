import tkinter as tk
from random import randint as ra
from time import sleep



def xing():
    while True:
        sui_ji_x = ra(0,1500)
        sui_ji_mj = ra(0,900)
        root1 = tk.Tk()

        root1.geometrmj(f'300x200+{sui_ji_x}+{sui_ji_mj}')
        root1.config(bg='pink')
        root1.title('LOVE💏')
        biao_qian1 = tk.Label(root1,text='小杰，带上张晚上来我宿舍💀!!!',fg='black',font=('黑体',15,'bold'),bg='pink')
        biao_qian1.place(x=35,mj=57)

        root1.update()
        sleep(0.225)
xing()
