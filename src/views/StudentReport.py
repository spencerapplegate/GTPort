# Figure 18 Average Grade by Instructors

from tkinter import *
import pymysql
from tkinter.messagebox import showwarning

class StudentReport:
    def __init__(self, driver, un):
        self.Driver = driver
        self.un = un

        self.root = Tk()
        self.root.title("Student Report")

        self.dept = StringVar()
        self.dept.set("--")

        self.makeWindow()
        self.root.mainloop()

    def makeWindow(self):
        self.label = Label(self.root, text="Department: ")
        self.label.grid(row=0, column=0)
        
        self.deptList = ["--", "Aerospace Engineering","Biology", "Biomedical Engineering", "Computer Science","Electrical & Computer Engineering"]
        self.options = OptionMenu(self.root, self.dept, *self.deptList, command=self.populate)
        self.options.grid(row=0, column=1, columnspan=3)
        
        self.label1 = Label(self.root, text = "Instructor")
        self.label1.grid(row=1, column=0, sticky=W)

        self.label2 = Label(self.root, text = 'Course Code')
        self.label2.grid(row=1, column=1, sticky=EW)

        self.label3 = Label(self.root, text = 'Course Name')
        self.label3.grid(row=1, column=2, sticky=EW)

        self.label4 = Label(self.root, text = 'Average Grade')
        self.label4.grid(row=1, column=3, sticky=E)

        self.link1 = Button(self.root, text = 'Go To Homepage', command=self.returnHome)
        self.link1.grid(row=3, column=1, columnspan=2, sticky=E)

        self.bodyFrame = Frame(self.root)
        self.bodyFrame.grid(row=2,columnspan=4,sticky=EW)

    def populate(self, dept):
        if self.dept.get() != "--":
            db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36",
                             db='cs4400_Group36')
            c = db.cursor()
            query = "SELECT C.courseCode, C.courseTitle, I.name FROM coursesOffered C, department D, courseSection S, teaches T, instructor I WHERE C.deptID = D.deptID AND C.courseCode = S.courseCode AND S.sectionCRN = T.sectionCRN AND T.instructorUsername = I.username AND D.name = %s GROUP BY C.courseTitle"
            c.execute(query, dept)
            items = c.fetchall()
            itemList = []
            for i in items:
                y = []
                for x in i:
                    y += [x]
                y += [0,0,0,0,0]
                itemList += [y]
            for i in itemList:
                queryA = "SELECT grade FROM registers R, courseSection C WHERE R.sectionCRN = C.sectionCRN AND C.courseTitle = %s"
                c.execute(queryA, i[1])
                a = c.fetchall()
                for b in a:
                    if b[0] == "A":
                        i[3] += 1
                    elif b[0] == "B":
                        i[4] += 1
                    elif b[0] == "C":
                        i[5] += 1
                    elif b[0] == "D":
                        i[6] += 1
                    elif b[0] == "F":
                        i[7] += 1
            for x in itemList:
                if (x[3]+x[4]+x[5]+x[6]+x[7]) == 0:
                    gpa = 0
                else:
                    gpa = ((x[3]*4)+(x[4]*3)+(x[5]*2)+(x[6]*1)+(x[7]*0))/(x[3]+x[4]+x[5]+x[6]+x[7])
                x += [float(round(gpa,2))]
            goodList = []
            for y in itemList:
                goodList += [[y[0],y[1],y[2], y[8]]]
            c.close()
            db.close()
            # Something about this grid remove/forget doesnt
            # work correctly! But the content is correct!
            self.bodyFrame.grid_remove()
            for num in range(len(goodList)):
                Lname = Label(self.bodyFrame, text=goodList[num][2])
                Lname.grid(row=num,column=0)
                Lcode = Label(self.bodyFrame, text=goodList[num][0])
                Lcode.grid(row=num,column=1)
                Ltitle = Label(self.bodyFrame, text=goodList[num][1])
                Ltitle.grid(row=num, column=2)
                Lgpa = Label(self.bodyFrame, text=str(goodList[num][3]))
                Lgpa.grid(row=num, column=3)
            self.bodyFrame.grid(row=2,columnspan=4,sticky=EW)
        else:
            showwarning("ERROR", "Please select a valid department.")

    def returnHome(self):
        self.root.destroy()
        self.Driver.launch_homepage([1,0,0],self.un)

if __name__=="__main__":
    app = StudentReport()
