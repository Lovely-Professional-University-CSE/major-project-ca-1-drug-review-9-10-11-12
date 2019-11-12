from tkinter import *
from PIL import ImageTk,Image
import os
def Return_H():
	top.destroy()
	os.system('home_page.py')

def open_window():
   top.destroy()
   os.system('predict.py')
def Plots():
  
  top.destroy()
  os.system('visualize.py')

def exit_window():
	top.destroy()
    
def show_accuracy():
  top.destroy()
  os.system('accuracy.py')
top=Tk()
#top.geometry("600x300+120+120")

top.config(bg ="black")
top.wm_title("ABOUT")
top.wm_attributes("-fullscreen", "true")

take_UI1 = PhotoImage(file ='Input_Image.png')
B1=Button(top, image = take_UI1, cursor="hand2", command = open_window)
B1.pack(anchor=N, padx=500,pady=20,fill='both')
B1.config(width = 150, height = 150)

bar_plots = PhotoImage(file = 'bar_graph.png')
B2=Button(top,image =bar_plots,text= 'Plots',compound=LEFT,font=('helv36', 60, 'bold'),command=Plots)
B2.pack(anchor=SE,padx=300,pady=20,fill='both')
B2.config(width = 300, height = 300)

acc=PhotoImage(file='features_accuracy.png')
B3=Button(top,image=acc,text='Accuracy',cursor='hand2',command=show_accuracy)
B3.pack(anchor=S, padx=500,pady=20,fill='both')
B3.config(width = 150, height = 150)

home_R = PhotoImage(file = 'home.png')
mbutton=Button(top,image=home_R, font=('helv36', 20, 'bold'),fg = 'white',bg='black', cursor="hand2", command = Return_H)
mbutton.pack(anchor=SW, padx =500, pady = 20,fill='both')
mbutton.config(width = 300, height = 120)



    
exit1 = PhotoImage(file = 'Exit_Image.png')
mbutton1=Button(top,image =exit1,command=exit_window)
mbutton1.pack(anchor=SE,padx=500,pady=20,fill='both')
mbutton1.config(width = 300, height = 120)

top.mainloop()
