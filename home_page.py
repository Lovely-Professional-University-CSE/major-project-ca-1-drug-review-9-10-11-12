# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:34:27 2019

@author: Asus
"""

from tkinter import *
import os
home_page = Toplevel()
home_page.title("HOME")
home_page.wm_attributes("-fullscreen", "true")
home_page.config(bg="black")

home_page.iconbitmap("Cjdowner-Cryptocurrency-ICON.ico")
sentiment1 = PhotoImage(file = 'sentiment.png')

take_UI = PhotoImage(file = 'start_image.png')

Label(home_page, text= 'Drug Review Dataset',fg='red',compound=BOTTOM,font=('helv36', 40, 'bold'),image = sentiment1).pack(anchor=CENTER, padx = 400, pady = 20)

def exit_window():
	home_page.destroy()
exit_image = PhotoImage(file = 'Exit_Image.png')
Button(home_page, image=exit_image, cursor="hand2", command = exit_window).pack(anchor=SW, padx=10, pady=0)

def Predict_Input():
	home_page.destroy()
	os.system('app.py')
B1=Button(home_page,  image = take_UI, font="halston 20 italic", cursor="hand2", command = Predict_Input)
B1.pack(anchor=E, padx=200,pady=20)
B1.config(width = 600, height = 900)
home_page.mainloop()