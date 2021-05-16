"""
Author: Vasan Naddoni
copyright @ Occipital Technologies Pvt Ltd
"""

import tkinter as tk

class CustomFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self,bg = "#232323")

class CustomButton(tk.Button):
    def __init__(self,*args,**kwargs):
        super(CustomButton,self).__init__(*args, **kwargs)
        self.configure(font = ('Calibri', '28'),fg = "#FFFAFA",bg = "#535558",relief="raised",activebackground = "#535558")

class CustomLabel(tk.Label):
    def __init__(self,*args,**kwargs):
        super(CustomLabel,self).__init__(*args, **kwargs)
        self.configure(font = ('Calibri', '28'),bg = "#232323",fg = "#FFFAFA")

class CustomEntry(tk.Entry):
    def __init__(self,*args,**kwargs):
        super(CustomEntry,self).__init__(*args, **kwargs)
        self.configure(font = ('Calibri', '28'), bg="#EAEAEA")

class CustomPannedWindow(tk.PanedWindow):
    def __init__(self,*args,**kwargs):
        super(CustomPannedWindow,self).__init__(*args,**kwargs)
        self.configure(bg =  "#878A8E")

class CustomOptionMenu(tk.OptionMenu):
    def __init__(self,*args,**kwargs):
        super(CustomOptionMenu,self).__init__(*args,**kwargs)
        self.configure(font = ('Calibri', '28'),bg =  "#f7f7f7")

class CustomScale(tk.Scale):
    def __init__(self,*args,**kwargs):
        super(CustomScale,self).__init__(*args,**kwargs)
        self.configure(orient='horizontal',resolution=5,sliderrelief="raised",width = 40,sliderlength = 95,borderwidth = 0)
