from tkinter import *

root = Tk()
root.title('Notepad')
def file1():
    print('Create your New Project')
def New1():
    print('Create New file')
def open1():
    print("Open Your file")
def save1():
    print("Save Your File")
def  print1():
    print("Print data present in your file")

menu = Menu(root)

m1 = Menu(menu)
m1.add_command(label='NewProject', command=file1)
m1.add_command(label='New', command=New1)
m1.add_command(label='Open', command=open1)
m1.add_separator()
m1.add_command(label='Save', command=save1)
m1.add_command(label='Print', command=print1)
root.config(menu=menu)

menu.add_cascade(label='File', menu=m1)
menu.add_cascade(label='Exit')

menu.config()




root.mainloop()