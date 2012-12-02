
from tkinter import *
import pymysql

class selectDepartment:
    def __init__ (self):
        self.root = Tk()
        self.root.title('Select Department')
        
        self.var1 = StringVar()
        self.var1.set("Computer Science")

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        
        label1 = Label(self.root, text = "Term:        Fall 2012")
        label1.grid(row = 0, column = 1, sticky = W)
        label2 = Label(self.root, text = "Department")
        label2.grid(row = 1, column = 1, sticky = W)


        listbox = OptionMenu(self.root,self.var1, "Aerospace Engineering", "Biology", "Biomedical Engineering", "Computer Science", "Electrical and Computer Engineering")
        listbox.grid(row = 1, column = 1, sticky = E)

        button1 = Button(self.root, text = "Back", width = 10)
        button1.grid(row = 2, column = 0)
        button2 = Button(self.root, text = "Next", width = 10, command = self.print_statement)
        button2.grid(row = 2, column = 2)

    def print_statement(self):
        print(self.var1.get())
        print("Hello World")

if __name__=='__main__':
    app = selectDepartment()

