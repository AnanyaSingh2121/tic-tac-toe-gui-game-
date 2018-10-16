from tkinter import*
import tkinter.messagebox

win=Tk()
win.title("TIC-TAC-TOE")
click=True

def board(button):
    global click
    if button['text']==" " and click==True:
        button['text']="X"
        click=False

    elif button['text']==" " and click==False:
         button['text']="O"
         click=True
    if(button1['text']=="X" and button2['text']=="X" and button3['text']=="X" or  
       button4['text']=="X" and button5['text']=="X" and button6['text']=="X" or
       button7['text']=="X" and button8['text']=="X" and button9['text']=="X" or
       button1['text']=="X" and button4['text']=="X" and button7['text']=="X" or
       button2['text']=="X" and button5['text']=="X" and button8['text']=="X" or
       button3['text']=="X" and button6['text']=="X" and button9['text']=="X" or
       button1['text']=="X" and button5['text']=="X" and button9['text']=="X" or
       button3['text']=="X" and button5['text']=="X" and button7['text']=="X"):
           tkinter.messagebox.showinfo("Winner X","you won")
    if(button1['text']=="O" and button2['text']=="O" and button3['text']=="O" or  
       button4['text']=="O" and button5['text']=="O" and button6['text']=="O" or
       button7['text']=="O" and button8['text']=="O" and button9['text']=="O" or
       button1['text']=="O" and button4['text']=="O" and button7['text']=="O" or
       button2['text']=="O" and button5['text']=="O" and button8['text']=="O" or
       button3['text']=="O" and button6['text']=="O" and button9['text']=="O" or
       button1['text']=="O" and button5['text']=="O" and button9['text']=="O" or
       button3['text']=="O" and button5['text']=="O" and button7['text']=="O"):
           tkinter.messagebox.showinfo("Winner O","you won")           
    '''else:
        tkinter.messagebox.showinfo("Draw") '''
     
  

button=StringVar()

button1=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button1))
button1.grid(row=1,column=0,sticky=S+N+W+E)

button2=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button2))
button2.grid(row=1,column=1,sticky=S+N+W+E)

button3=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button3))
button3.grid(row=1,column=2,sticky=S+N+W+E)

button4=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button4))
button4.grid(row=2,column=0,sticky=S+N+W+E)

button5=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button5))
button5.grid(row=2,column=1,sticky=S+N+W+E)

button6=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button6))
button6.grid(row=2,column=2,sticky=S+N+W+E)

button7=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button7))
button7.grid(row=3,column=0,sticky=S+N+W+E)

button8=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button8))
button8.grid(row=3,column=1,sticky=S+N+W+E)

button9=Button(win,text=" ",font=('ariel 28 bold'),height=4,width=8,
               command=lambda:board(button9))
button9.grid(row=3,column=2,sticky=S+N+W+E)




win.mainloop()




