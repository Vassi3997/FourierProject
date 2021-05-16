from math import radians
import tkinter as tk
from styling import CustomFrame    
import math

class FirstPage(CustomFrame):
    def __init__(self,parent,controller):
        CustomFrame.__init__(self, parent)

        self.controller = controller

        self.radius = 200
        self.cv = tk.Canvas(self)
        self.cv.pack()
        self.cv.place(relheight=0.98, relwidth=0.98, relx=0.01, rely=0.01)
        self.t1 = 0
        self.old_small_circle = None
        self.wave = []
        self.iteration = 0
        self.create_circle(480,540,self.radius,self.cv)
        self.create_circle(480,540,5,self.cv,fill="black")
        self.revolvingCircle(self.t1)

    def create_circle(self,x, y, radius, canvasName,fill=""): 
        x0 = x - radius
        y0 = y - radius
        x1 = x + radius
        y1 = y + radius
        return canvasName.create_oval(x0, y0, x1, y1,fill=fill)

    def delete_elements(self,element):
        self.cv.delete(element)

    def revolvingCircle(self,t1):
        if self.old_small_circle is not None:
            self.cv.delete(self.old_small_circle)
            self.cv.delete(self.line)
            self.cv.delete(self.traveling_line)
        t1 -= 1.5
        
        x = self.radius*math.cos(math.radians(t1))
        y = self.radius*math.sin(math.radians(t1))

        self.line = self.cv.create_line(480,540,x+480,y+540)

        self.traveling_line = self.cv.create_line(x+480,y+540,960,y+540)
        self.wave = [y+540] + self.wave

        for i in range(len(self.wave)):
            self.pattern = self.create_circle(960+i,self.wave[i],3,self.cv,fill="black")
            self.after(100,self.delete_elements,self.pattern)

        self.old_small_circle=self.create_circle(x+480,y+540,5,self.cv,fill="black")

        self.cv.delete(self.pattern)

        # if math.cos(math.radians(t1)) == 0.9999996192282494: #0.999999 :
            # print("cycle")
        if len(self.wave) > 540:
            self.wave.pop(-1)

        self.after(100,self.revolvingCircle,t1)