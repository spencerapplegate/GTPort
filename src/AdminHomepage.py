#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *

class AdminHomepage:

    def __init__(self):
        self.root = Tk()
        self.root.title('Home Page')

        self.selection = IntVar()

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        radioFrame = Frame(self.root)
        radioFrame.pack(padx=15)
        
        self.adminReportButton = Radiobutton(self.root, text="View Administrative Report", variable=self.selection, value=1)
        self.adminReportButton.pack(anchor=W)
        
        self.addCourseButton = Radiobutton(self.root, text="Add New Course", variable=self.selection, value=2)
        self.addCourseButton.pack(anchor=W)

        buttonFrame = Frame(self.root)
        buttonFrame.pack(fill=X)

        nextButton = Button(buttonFrame, text="Next", command=self.print_this)
        nextButton.pack(side=RIGHT)

        logoutButton = Button(buttonFrame, text="Logout", command=self.print_this())
        logoutButton.pack(side=RIGHT)

    # This method is just a place holder to print out the username and password
    # values gathered from the textfields. This will not be used in the actual
    # application
    def print_this(self):
        print("Hello World")

if __name__=="__main__":
    app = AdminHomepage()
