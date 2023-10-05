import tkinter as tk
from tkinter import font as tkfont
import result

flag = ''


class RAID1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        flag = 'raid1'

        label = tk.Label(self, text='RAID-1', font=controller.title_font)
        label.place(x=268, y=10)

        lbl = tk.Label(self, text='Рассчет общего объема', font=('Share Tech Mono', 14, 'italic'))
        lbl.place(x=50, y=50)

        lbl_s = tk.Label(self, text='S = ')
        lbl_s.place(x=70, y=110)
        lbl_z = tk.Label(self, text='Σ = ')
        lbl_z.place(x=70, y=170)

        entry_s = tk.Entry(self, width=10)
        entry_s.place(x=100, y=110)

        btn_res = tk.Button(self, text='Рассчитать', width=14)
        btn_res.place(x=70, y=143)

        lbl_res = tk.Label(self, text='')
        lbl_res.place(x=100, y=170)

        lbl = tk.Label(self, text='Рассчет объема одного диска', font=('Share Tech Mono', 14, 'italic'))
        lbl.place(x=350, y=50)

        lbl_s = tk.Label(self, text='Σ = ')
        lbl_s.place(x=390, y=110)
        lbl_z = tk.Label(self, text='S = ')
        lbl_z.place(x=390, y=170)

        entry_s = tk.Entry(self, width=10)
        entry_s.place(x=420, y=110)

        btn_res = tk.Button(self, text='Рассчитать', width=14)
        btn_res.place(x=390, y=143)

        lbl_res = tk.Label(self, text='')
        lbl_res.place(x=420, y=170)

        button = tk.Button(self, text='Назад', width=10, command=lambda: controller.show_frame('StartPage'))
        button.place(x=255, y=350)
