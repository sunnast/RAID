import tkinter as tk
from tkinter import font as tkfont

xplacer = 210
yplacer = 90


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Выберите вид массива", font=controller.title_font)
        label.place(x=xplacer, y=yplacer)

        btn_raid0 = tk.Button(self, text="RAID-0", width=19,
                              command=lambda: (controller.show_frame("RAID0"), controller.set_raid(0)))
        btn_raid1 = tk.Button(self, text="RAID-1", width=19, bg='blue',
                              command=lambda: controller.show_frame("RAID1"))
        btn_raid5 = tk.Button(self, text="RAID-5", width=19,
                              command=lambda: controller.show_frame("RAID5"))
        btn_raid10 = tk.Button(self, text="RAID-1+0", width=19,
                               command=lambda: controller.show_frame("RAID10"))
        btn_raid50 = tk.Button(self, text="RAID-5+0", width=19,
                               command=lambda: controller.show_frame("RAID50"))
        btn_raid0.place(x=xplacer, y=yplacer + 30)
        btn_raid1.place(x=xplacer, y=yplacer + 60)
        btn_raid5.place(x=xplacer, y=yplacer + 90)
        btn_raid10.place(x=xplacer, y=yplacer + 120)
        btn_raid50.place(x=xplacer, y=yplacer + 150)
