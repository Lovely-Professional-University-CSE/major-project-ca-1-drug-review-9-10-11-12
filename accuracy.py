from tkinter import *
import os
from preprocess import *
import os
def back():
    accuracy_window.destroy()
    os.system('gui.py')
accuracy_window=Tk()
box=PhotoImage(file='images\\confusion.png')
l1=Label(accuracy_window,image=box)
l1.grid(row=1,column=1)
l2=Label(accuracy_window,text=loaded_acc,font=('helv36', 30, 'bold'))
l2.grid(row=3,column=1)
l3=Label(accuracy_window,text='Accuracy of the model',font=('helv36', 20, 'bold'))
l3.grid(row=2,column=1)
b1=Button(accuracy_window,text='Back',command=back)
b1.grid(row=4, column=1)
accuracy_window.mainloop()