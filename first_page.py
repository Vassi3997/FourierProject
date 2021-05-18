from math import pi, radians
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
        self.cv.configure(scrollregion=(-480,-480,540,540))
        self.t1 = 0
        self.seq = 0

        self.rings = 2
        self.time_increment = 0.9
        self.screen_update_time = 32
        self.content_deletion_delay = 7 

        self.center_secondary_circle = None
        self.wave = []
        self.iteration = 0
        self.create_circle(0,0,5,self.cv,fill="black")
        self.revolvingCircle(self.t1)

    def create_circle(self,x, y, radius, canvasName,fill=""):
        return canvasName.create_oval(x - radius, y - radius, x + radius, y + radius,fill=fill)


    def draw_wave(self,wave):

        for i in range(1,len(wave)):
            self.pattern = self.cv.create_line(600+i,wave[i-1],600+i,wave[i],fill="black",width="3")
            self.after(self.screen_update_time+self.content_deletion_delay,self.cv.delete,self.pattern)


    def revolvingCircle(self,t1):
        x = 0
        y = 0
        self.create_circle(0,0,self.radius*(4/( math.pi)),self.cv)

        if self.center_secondary_circle is not None:
            self.cv.delete(self.line)
            self.cv.delete(self.center_secondary_circle)
            self.cv.delete(self.main_circle)

        for i in range(self.rings):
            prevX = x
            prevY = y
            n = 2*i + 1
            
            if self.center_secondary_circle is not None:
                self.cv.delete(self.traveling_line)
                self.after(self.screen_update_time+self.content_deletion_delay,self.cv.delete,self.line)
                self.after(self.screen_update_time+self.content_deletion_delay,self.cv.delete,self.main_circle)
                self.after(self.screen_update_time+self.content_deletion_delay,self.cv.delete,self.center_secondary_circle)

            t1 -= self.time_increment
            
            self.new_radius = self.radius*(4/(n* math.pi))

            x += self.new_radius*math.cos(n*math.radians(t1))
            y += self.new_radius*math.sin(n*math.radians(t1))


            self.main_circle = self.create_circle(prevX,prevY,self.new_radius,self.cv)

            self.center_secondary_circle=self.create_circle(x,y,5,self.cv,fill="black")

            self.line = self.cv.create_line(x,y,prevX,prevY,width="3")

            self.traveling_line = self.cv.create_line(x,y,600,y,fill="red",width="3")

        self.wave.insert(0,y)

        if len(self.wave)>=2:
            self.draw_wave(self.wave)

        if len(self.wave)>700:
            self.wave.pop()

        self.after(self.screen_update_time,self.revolvingCircle,t1)