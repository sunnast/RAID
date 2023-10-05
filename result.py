import genericpath
import tkinter as tk
from tkinter import font as tkfont

import raid0
from main import SampleApp
from raid0 import *
from raid1 import *
from raid5 import *
from raid10 import *
from raid50 import *
from start import *


class Result(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def result(self, n, s, lbl):
        txt = 'я работаю'
        self.lbl = lbl
        z = int(n.get()) + int(s.get())
        self.lbl.config(text=z)
