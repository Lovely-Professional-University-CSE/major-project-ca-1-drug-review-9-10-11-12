
from tkinter import *
import sys
import os

about_us = Tk()
about_us.title("About Us")
about_us.wm_attributes("-fullscreen", "true")
about_us.config(bg="cyan")

Label(about_us, text="Module Used", font="halston 20 italic underline", bg="cyan").pack(padx = 20, pady = 10)

about_us_Frame = Frame(about_us, bg="cyan")
about_us_Frame.pack(anchor = N)

image1 = PhotoImage(file="seaborn.png")
image2 = PhotoImage(file="tkinter.png")
image3 = PhotoImage(file="numpy.png")
image4 = PhotoImage(file="pandas.png")
image5 = PhotoImage(file="matplotlib.png")
image6 = PhotoImage(file="spyder.png")

Label(about_us_Frame, image=image1,text= 'Seaborn',compound=LEFT,font=('helv36', 20, 'bold')).grid(row = 0, column = 0)
Label(about_us_Frame, image=image2,text= 'Tkinter',compound=LEFT,font=('helv36', 20, 'bold')).grid(row = 0, column = 1)
Label(about_us_Frame, image=image3,text= 'Numpy',compound=LEFT,font=('helv36', 20, 'bold')).grid(row = 0, column = 2)
Label(about_us_Frame, image=image4,text= 'Pandas',compound=LEFT,font=('helv36', 20, 'bold')).grid(row = 1, column = 2,padx=100, pady=5)
Label(about_us_Frame, image=image5,text= 'matplotlib',compound=LEFT,font=('helv36', 20, 'bold')).grid(row = 1, column = 0, padx=10, pady=5)
Label(about_us_Frame, image=image6,text= 'Spyder',compound=LEFT,font=('helv36', 20, 'bold')).grid(row = 1, column = 1, padx=10, pady=5)

def home_page():
    about_us.destroy()
    os.system("home_page.py")
home_button = PhotoImage(file="home.png")
Button(about_us_Frame, image=home_button, cursor="hand2", command=home_page).grid(row = 2, column = 0, columnspan = 1, pady=10)

about_us.mainloop()
