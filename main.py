#!/usr/bin/env python3
"""
Author: Vasan Naddoni
"""
import tkinter as tk
import os, sys
# sys.path.insert(0, os.path.abspath('..'))
from first_page import FirstPage
from tkinter import PhotoImage
from styling import CustomLabel,CustomFrame
import time



class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

    
        self.geometry(str(int(screen_width))+"x"+str(int(screen_height))) 
        # self.geometry(str(int(screen_width/2))+"x"+str(int(screen_height/2))) 
        # self.start_up_app()
        # self.attributes('-fullscreen', True)
        
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in [FirstPage]:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FirstPage")
        self.mainloop()
        # th.join()


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''

        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    SampleApp()
    