import tkinter as tk
from tkinter import font as tkfont

from raid0 import *
from raid1 import *
from raid5 import *
from raid10 import *
from raid50 import *
from start import *


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Share Tech Mono', size=14, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        w = container.winfo_screenwidth()
        h = container.winfo_screenheight()
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 300  # смещение от середины
        h = h - 200
        self.geometry(f'600x400+{w}+{h}')
        self.resizable(width=False, height=False)

        self.frames = {}
        for F in (StartPage, RAID0, RAID1, RAID5, RAID10, RAID50):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def set_raid(self, value):
        self.raid = value

    def set_raid_n(self, n):
        self.n = n

    def set_raid_s(self, s):
        self.s = s

    # def set_res_win(self, param):
    #     self.lbl_res = param

    # def result(self, n, s, lbl):
    #     self.n = n
    #     self.s = s
    #     self.lbl = lbl
    #     z = self.n * self.s
    #     self.lbl.config(z)


    # def result(self, flag_marker, n, s):
    #
    #     if flag_marker == 'raid0':
    #
    #         self = int(n) * int(s)
    #         lbl_res2 = tk.Label(self, text='')
    #         lbl_res2.place(x=420, y=170)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
