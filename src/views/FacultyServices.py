
from tkinter import *
import pymysql

class FacultyServices:
    def __init__ (self):
        self.root = Tk()
        self.root.title('Faculty Services')

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):

        button1 = Button(self.root, text = "Assign Grades", width = 25, command = self.print_statement)
        button1.grid(row = 0, column = 0)
        button1 = Button(self.root, text = "Update Personal Information", width = 25, command = self.print_statement)
        button1.grid(row = 1, column = 0)
        button1 = Button(self.root, text = "Assign Tutors", width = 25, command = self.print_statement)
        button1.grid(row = 2, column = 0)
        button1 = Button(self.root, text = "View Student Performance", width = 25, command = self.print_statement)
        button1.grid(row = 3, column = 0)
        
    def print_statement(self):
        print("I love you!")

if __name__=='__main__':
    app = facultyServices()

