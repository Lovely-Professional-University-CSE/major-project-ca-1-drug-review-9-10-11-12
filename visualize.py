from tkinter import *
from PIL import ImageTk,Image
import os
def back():
    visualize_window.destroy()
    os.system('GUI.py')
visualize_window=Tk()
visualize_window.config
box=PhotoImage(file='images\\boxplot.png')
l1=Label(visualize_window,image=box)
l1.grid(row=1,column=1)
ratings=PhotoImage(file='images\\ratings_chart.png')
l2=Label(visualize_window,image=ratings)
l2.grid(row=1,column=2)
word=PhotoImage(file='images\\review_word.png')
l3=Label(visualize_window,image=word)
l3.grid(row=2,column=1)
bar=PhotoImage(file='images\\barplot.png')
l4=Label(visualize_window,image=bar)
l4.grid(row=2,column=2)
b1=Button(visualize_window,text='home',command=back)
b1.grid(row=2,column=3)
visualize_window.mainloop()