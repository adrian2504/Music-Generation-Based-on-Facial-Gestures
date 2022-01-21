from  tkinter import ttk,tix
from tkinter import *
from code import *
def screen():
    root=Tk()#blank widow
    root.title("BAND MUSIC PLAYER")
    root.geometry('500x500')
    style = ttk.Style()
    style.map("C.TButton",
        foreground=[('pressed', 'red'), ('active', 'blue')],
        background=[('pressed', '!disabled', 'black'), ('active', 'white')]
        )
    #entities on the window and placing them
    label2=ttk.Label(root,text="Play Band Section",font=("Arial Bold", 10)).place(x=50,y=260)
    label3=ttk.Label(root,text="Actions: One Eye Open,Both Eyes Closed,Head on right,Head on Left,Head on Top",font=("Arial Bold", 8)).place(x=50,y=280)
    buttonPlay=ttk.Button(root, text="Play Band",style='C.TButton',command=Band).place(x=150,y=350)
    
    root.mainloop()#window constantly display

#main Execution
screen()
