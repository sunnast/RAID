import tkinter as tk
from tkinter import font as tkfont
from result import Result


class RAID0(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        r = Result(self, controller)

        label = tk.Label(self, text='RAID-0', font=controller.title_font)
        label.place(x=268, y=10)

        lbl = tk.Label(self, text='Рассчет общего объема', font=('Share Tech Mono', 14, 'italic'))
        lbl.place(x=50, y=50)

        lbl_n = tk.Label(self, text='N = ')
        lbl_n.place(x=70, y=80)
        lbl_s = tk.Label(self, text='S = ')
        lbl_s.place(x=70, y=110)
        lbl_z = tk.Label(self, text='Σ = ')
        lbl_z.place(x=70, y=170)

        entry_n = tk.Entry(self, width=10)
        entry_n.place(x=100, y=80)
        entry_s = tk.Entry(self, width=10)
        entry_s.place(x=100, y=110)

        # n = controller.set_raid_n(entry_n)
        # s = controller.set_raid_s(entry_s)
        # z = int(n) * int(s)

        lbl_res1 = tk.Label(self, text='!!!!')
        lbl_res1.place(x=100, y=170)

        btn_res1 = tk.Button(self, text='Рассчитать', width=14,
                             command=(lambda: r.result(entry_n, entry_s, lbl_res1)))
        btn_res1.place(x=70, y=143)

        lbl = tk.Label(self, text='Рассчет объема одного диска', font=('Share Tech Mono', 14, 'italic'))
        lbl.place(x=350, y=50)

        lbl_n = tk.Label(self, text='N = ')
        lbl_n.place(x=390, y=80)
        lbl_s = tk.Label(self, text='Σ = ')
        lbl_s.place(x=390, y=110)
        lbl_z = tk.Label(self, text='S = ')
        lbl_z.place(x=390, y=170)

        entry_n = tk.Entry(self, width=10)
        entry_n.place(x=420, y=80)
        entry_z = tk.Entry(self, width=10)
        entry_z.place(x=420, y=110)

        btn_res2 = tk.Button(self, text='Рассчитать', width=14)
        btn_res2.place(x=390, y=143)

        lbl_res2 = tk.Label(self, text='')
        lbl_res2.place(x=420, y=170)

        button = tk.Button(self, text='Назад', width=10, command=lambda: controller.show_frame('StartPage'))
        button.place(x=255, y=350)

        # def result():
        #     n = controller.set
        #
