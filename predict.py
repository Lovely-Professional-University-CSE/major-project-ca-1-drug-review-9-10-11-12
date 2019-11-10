from tkinter import *
from preprocess import *
import os

def sentiment():
    mtext=t1.get()
    x=prepro(mtext)
    vect=vector(x)
    pred=loaded_clf.predict(vect)
    entry2=Label(root,text=pred[0])
    entry2.config(font=('helvetica', 10))
    canvas1.create_window(200, 210, window=entry2)

root= Tk()
#root.wm_attributes("-fullscreen", "true")
root.config(bg="black")
root.title("Predict the Sentiment")
t1=StringVar()
canvas1 = Canvas(root, width = 400, height = 300,  relief = 'raised',bg = 'black')
canvas1.pack()

label1 =Label(root, text='Predict Or Comment The Sentiment')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 =Label(root, text='Type Your Review:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)
 
entry1 =Entry (root) 
canvas1.create_window(200, 140, window=entry1)
    
B2 = Button(root,text='Get the Sentiment',bg='brown', fg='white', font=('helvetica', 9, 'bold'),command=sentiment)
canvas1.create_window(200, 180, window=B2)
root.mainloop()