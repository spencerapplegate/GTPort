#!/usr/bin/python3.2
'''
Created on Nov 12, 2012

@author: spencer
'''
from tkinter import *
from tkinter.messagebox import showwarning
from tkinter.messagebox import showinfo
import pymysql

# This is a class called Login. We will be able to use this class to create
# several instances of this view. Therefore we could have several users
# accessing our application at once (prob not necessary for this project)
# but it will help with code flow as well
class StudentPI:

    # This is the constructor of the login view. Here I create the Tk object,
    # username and password variables (specific to each instance of Login). I also
    # construct the view and run it through the computer's clock cycles (makeWindow
    # and mainloop)
    def __init__(self, un, driver):
        self.Driver = driver
        self.username = un
        self.root = Tk()
        self.root.title('Personal Information')

        self.name = StringVar()
        self.dob = StringVar()
        self.gender = StringVar(value="Male")
        self.address = StringVar()
        self.permAddress = StringVar()
        self.contactNumber = StringVar()
        self.email = StringVar()
        self.tutorWilling = IntVar(value=1)
        self.tutorCourses = []
        self.currentTutorCourse = StringVar(self.root)
        self.tutorCoursesSelected = []
        self.major = StringVar(value="Aerospace Engineering")
        self.degree = StringVar(value="BS")
        self.previousEduSchool = []
        self.previousEduMajor = []
        self.previousEduDegree = []
        self.previousEduGradYear = []
        self.previousEduGPA = []

        self.populate()

        self.makeWindow()
        self.root.mainloop()

    # This method is used to construct the actual view. Names of variables
    # should be intuitive. Three frames are used to control the layout of the
    # view using Tk's 'pack' method.
    def makeWindow(self):

        nameFrame = Frame(self.root)
        nameFrame.pack(padx=10)

        nameLabel = Label(nameFrame, text="Name ")
        nameLabel.pack(side=LEFT)

        nameEntry = Entry(nameFrame, textvariable = self.name)
        nameEntry.pack(side=LEFT, padx=10)

        dobFrame = Frame(self.root)
        dobFrame.pack(padx=10)

        dobLabel = Label(dobFrame, text="Date of Birth ")
        dobLabel.pack(side=LEFT)

        dobEntry = Entry(dobFrame, textvariable = self.dob)
        dobEntry.pack(side=LEFT, padx=10)

        genderFrame = Frame(self.root)
        genderFrame.pack(padx=15)

        genderLabel = Label(genderFrame, text="Gender ")
        genderLabel.pack(side=LEFT)

        genderOptionMenu = OptionMenu(genderFrame, self.gender, "Male", "Female")
        genderOptionMenu.pack(side=LEFT)

        addressFrame = Frame(self.root)
        addressFrame.pack(padx=10)

        addressLabel = Label(addressFrame, text="Address ")
        addressLabel.pack(side=LEFT)

        addressEntry = Entry(addressFrame, textvariable = self.address)
        addressEntry.pack(side=LEFT, padx=10)

        permAddressFrame = Frame(self.root)
        permAddressFrame.pack(padx=10)

        permAddressLabel = Label(permAddressFrame, text="Permanent Address ")
        permAddressLabel.pack(side=LEFT)

        permAddressEntry = Entry(permAddressFrame, textvariable = self.permAddress)
        permAddressEntry.pack(side=LEFT, padx=10)

        contactFrame = Frame(self.root)
        contactFrame.pack(padx=10)

        contactLabel = Label(contactFrame, text="Contact ")
        contactLabel.pack(side=LEFT)

        contactEntry = Entry(contactFrame, textvariable = self.contactNumber)
        contactEntry.pack(side=LEFT, padx=10)

        emailFrame = Frame(self.root)
        emailFrame.pack(padx=10)

        emailLabel = Label(emailFrame, text="Email Address ")
        emailLabel.pack(side=LEFT)

        emailEntry = Entry(emailFrame, textvariable = self.email)
        emailEntry.pack(side=LEFT, padx=10)

        tutorWillingFrame = Frame(self.root)
        tutorWillingFrame.pack(padx=10)

        tutorWillingLabel = Label(tutorWillingFrame, text="Willing to tutor? ")
        tutorWillingLabel.pack(side=LEFT)

        yesRadioButton = Radiobutton(tutorWillingFrame, text="Yes",
                variable=self.tutorWilling,value=0, command=self.radio_yes)
        yesRadioButton.pack(side=LEFT)

        noRadioButton = Radiobutton(tutorWillingFrame, text="No",
                variable=self.tutorWilling,value=1, command=self.radio_no)
        noRadioButton.pack(side=LEFT)

        self.tutorCoursesFrame = Frame(self.root)
        self.tutorCoursesFrame.pack(padx=15, fill=X)

        tutorCoursesLabel = Label(self.tutorCoursesFrame, text="If Yes, select the courses you would like to tutor for ")
        tutorCoursesLabel.grid(row=0,column=0)

        self.tutorCoursesOptionMenu = OptionMenu(self.tutorCoursesFrame,
                self.currentTutorCourse, *self.tutorCourses)
        self.tutorCoursesOptionMenu.grid(row=0,column=1)

        addCourseButton = Button(self.tutorCoursesFrame, text="+",
                command=self.addToSelected)
        addCourseButton.grid(row=0,column=2)

        self.tutorCoursesText = Text(self.tutorCoursesFrame, height=1, width=50, background="white")
        self.tutorCoursesText.grid(row=0,column=3)

        removeCoursesButton = Button(self.tutorCoursesFrame, text="Delete",
                command=self.removeFromSelected)
        removeCoursesButton.grid(row=0,column=4)

        majorFrame = Frame(self.root)
        majorFrame.pack(padx=15)

        majorLabel = Label(majorFrame, text="Major ")
        majorLabel.pack(side=LEFT)

        majorOptionMenu = OptionMenu(majorFrame, self.major, "Aerospace Engineering",
                                            "Biology", "Biomedical Engineering", "Computer Science",
                                            "Electrical & Computer Engineering")
        majorOptionMenu.pack(side=LEFT)

        degreeLabel = Label(majorFrame, text="Degree ")
        degreeLabel.pack(side=LEFT)

        degreeOptionMenu = OptionMenu(majorFrame, self.degree, "BS", "MS", "Ph.D")
        degreeOptionMenu.pack(side=LEFT)

        previousEduLabelFrame = Frame(self.root)
        previousEduLabelFrame.pack(padx=15)

        previousEduLabel = Label(previousEduLabelFrame, text="Previous Education ")
        previousEduLabel.pack()

        self.previousEduFrame = Frame(self.root, borderwidth=1)
        self.previousEduFrame.pack()

        self.populatePreviousEdu(0)

        self.buttonFrame = Frame(self.root)
        self.buttonFrame.pack(fill=X)

        self.submitButton = Button(self.buttonFrame, text="Submit",
                command=self.submit)
        self.submitButton.pack(side=RIGHT)

        self.addEduButton = Button(self.buttonFrame, text="Add Education",
                command=self.addEdu)
        self.addEduButton.pack(side=LEFT)


    def populate(self):
        self.db = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36", db='cs4400_Group36')
        c = self.db.cursor()
        SQL = "SELECT * FROM student WHERE username = %s"
        c.execute(SQL, self.username)
        items = c.fetchall()
        self.name.set(items[0][5])
        self.dob.set(items[0][7])
        if items[0][9] == 'M':
            self.gender.set("Male")
        else:
            self.gender.set("Female")
        self.major.set(items[0][2])
        self.degree.set(items[0][3])
        self.address.set(items[0][4])
        self.permAddress.set(items[0][8])
        self.contactNumber.set(items[0][10])
        self.email.set(items[0][6])

        #self.tutorCourses = self.getTutorCourse()
        self.tutorCourses.append("--")
        self.currentTutorCourse.set(self.tutorCourses[0])
        self.getPreviousEdu()

        c.close()
        self.db.close()

    def getTutorCourse(self):
        courses = []
        self.db2 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36", db='cs4400_Group36')
        c = self.db2.cursor()
        SQL = "SELECT courseCode FROM registers R, courseSection CS WHERE R.studentUsername = %s AND (R.grade = 'A' OR R.grade = 'B') AND R.sectionCRN = CS.sectionCRN"
        c.execute(SQL, self.username)
        items = c.fetchall()
        courses.append("--")
        for i in items:
            courses.append(i[0])
        c.close()
        self.db2.close()
        return courses

    def getPreviousEdu(self):
        self.db3 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj" , user ="cs4400_Group36", db='cs4400_Group36')
        c = self.db3.cursor()
        SQL = "SELECT * FROM eduHistory WHERE studentUsername = %s"
        c.execute(SQL, self.username)
        items = c.fetchall()
        for i in items:
            tmp = StringVar(value=i[1])
            self.previousEduSchool.append(tmp)
            tmp = IntVar(value=i[2])
            self.previousEduGradYear.append(tmp)
            tmp = StringVar(value=i[3])
            self.previousEduDegree.append(tmp)
            tmp = StringVar(value=i[4])
            self.previousEduMajor.append(tmp)
            tmp = DoubleVar(value=i[5])
            self.previousEduGPA.append(tmp)
        tmp = StringVar(value="")
        self.previousEduSchool.append(tmp)
        tmp = IntVar(value=0)
        self.previousEduGradYear.append(tmp)
        tmp = StringVar(value="")
        self.previousEduDegree.append(tmp)
        tmp = StringVar(value="")
        self.previousEduMajor.append(tmp)
        tmp = DoubleVar(value=0.0)
        self.previousEduGPA.append(tmp)
        c.close()
        self.db3.close()

    def addToSelected(self):
        if self.currentTutorCourse.get() == "--":
            return
        else:
            self.tutorCoursesSelected.append(self.currentTutorCourse.get())
        self.tutorCoursesText.delete("1.0", END)
        string = ""
        for i in range(len(self.tutorCoursesSelected)):
            string += self.tutorCoursesSelected[i]
            if i != (len(self.tutorCoursesSelected)-1):
                string += ", "
        self.tutorCoursesText.insert(INSERT, string)

    def populatePreviousEdu(self,flag):
        size = len(self.previousEduGradYear) - 1
        if size == 0:
            previousEduSchoolNameLabel = Label(self.previousEduFrame, text="Name of Institution Attended ")
            previousEduSchoolNameLabel.grid(row=0, column=0)

            previousEduSchoolNameEntry = Entry(self.previousEduFrame,
                    textvariable = self.previousEduSchool[0])
            previousEduSchoolNameEntry.grid(row=0, column=1)

            previousEduMajorLabel = Label(self.previousEduFrame, text="Major ")
            previousEduMajorLabel.grid(row=1, column=0)

            previousEduMajorEntry = Entry(self.previousEduFrame, textvariable =
                    self.previousEduMajor[0])
            previousEduMajorEntry.grid(row=1, column=1)

            previousEduDegreeLabel = Label(self.previousEduFrame, text="Degree ")
            previousEduDegreeLabel.grid(row=2, column=0)

            previousEduDegreeEntry = Entry(self.previousEduFrame, textvariable
                    = self.previousEduDegree[0])
            previousEduDegreeEntry.grid(row=2, column=1)

            previousEduGradYearLabel = Label(self.previousEduFrame, text="Year of graduation ")
            previousEduGradYearLabel.grid(row=3, column=0)

            previousEduGradYearEntry = Entry(self.previousEduFrame,
                    textvariable = self.previousEduGradYear[0])
            previousEduGradYearEntry.grid(row=3, column=1)

            previousEduGPALabel = Label(self.previousEduFrame, text="GPA ")
            previousEduGPALabel.grid(row=4, column=0)

            previousEduGPAEntry = Entry(self.previousEduFrame, textvariable =
                    self.previousEduGPA[0])
            previousEduGPAEntry.grid(row=4, column=1)
        elif size == 1:
            # first set
            previousEduSchoolNameLabel = Label(self.previousEduFrame, text="Name of Institution Attended ")
            previousEduSchoolNameLabel.grid(row=0, column=0)

            previousEduSchoolNameEntry = Entry(self.previousEduFrame,
                    textvariable = self.previousEduSchool[0])
            previousEduSchoolNameEntry.grid(row=0, column=1)

            previousEduMajorLabel = Label(self.previousEduFrame, text="Major ")
            previousEduMajorLabel.grid(row=1, column=0)

            previousEduMajorEntry = Entry(self.previousEduFrame, textvariable =
                    self.previousEduMajor[0])
            previousEduMajorEntry.grid(row=1, column=1)

            previousEduDegreeLabel = Label(self.previousEduFrame, text="Degree ")
            previousEduDegreeLabel.grid(row=2, column=0)

            previousEduDegreeEntry = Entry(self.previousEduFrame, textvariable
                    = self.previousEduDegree[0])
            previousEduDegreeEntry.grid(row=2, column=1)

            previousEduGradYearLabel = Label(self.previousEduFrame, text="Year of graduation ")
            previousEduGradYearLabel.grid(row=3, column=0)

            previousEduGradYearEntry = Entry(self.previousEduFrame,
                    textvariable = self.previousEduGradYear[0])
            previousEduGradYearEntry.grid(row=3, column=1)

            previousEduGPALabel = Label(self.previousEduFrame, text="GPA ")
            previousEduGPALabel.grid(row=4, column=0)

            previousEduGPAEntry = Entry(self.previousEduFrame, textvariable =
                    self.previousEduGPA[0])
            previousEduGPAEntry.grid(row=4, column=1)

            #second set
            previousEduSchoolNameLabel1 = Label(self.previousEduFrame, text="Name of Institution Attended ")
            previousEduSchoolNameLabel1.grid(row=5, column=0)

            previousEduSchoolNameEntry1 = Entry(self.previousEduFrame,
                    textvariable = self.previousEduSchool[1])
            previousEduSchoolNameEntry1.grid(row=5, column=1)

            previousEduMajorLabel1 = Label(self.previousEduFrame, text="Major ")
            previousEduMajorLabel1.grid(row=6, column=0)

            previousEduMajorEntry1 = Entry(self.previousEduFrame, textvariable
                    = self.previousEduMajor[1])
            previousEduMajorEntry1.grid(row=6, column=1)

            previousEduDegreeLabel1 = Label(self.previousEduFrame, text="Degree ")
            previousEduDegreeLabel1.grid(row=7, column=0)

            previousEduDegreeEntry1 = Entry(self.previousEduFrame, textvariable
                    = self.previousEduDegree[1])
            previousEduDegreeEntry1.grid(row=7, column=1)

            previousEduGradYearLabel1 = Label(self.previousEduFrame, text="Year of graduation ")
            previousEduGradYearLabel1.grid(row=8, column=0)

            previousEduGradYearEntry1 = Entry(self.previousEduFrame,
                    textvariable = self.previousEduGradYear[1])
            previousEduGradYearEntry1.grid(row=8, column=1)

            previousEduGPALabel1 = Label(self.previousEduFrame, text="GPA ")
            previousEduGPALabel1.grid(row=9, column=0)

            previousEduGPAEntry1 = Entry(self.previousEduFrame, textvariable =
                    self.previousEduGPA[1])
            previousEduGPAEntry1.grid(row=9, column=1)
        elif size >= 2:
            # first set
            previousEduSchoolNameLabel = Label(self.previousEduFrame, text="Name of Institution Attended ")
            previousEduSchoolNameLabel.grid(row=0, column=0)

            previousEduSchoolNameEntry = Entry(self.previousEduFrame,
                    textvariable = self.previousEduSchool[0])
            previousEduSchoolNameEntry.grid(row=0, column=1)

            previousEduMajorLabel = Label(self.previousEduFrame, text="Major ")
            previousEduMajorLabel.grid(row=1, column=0)

            previousEduMajorEntry = Entry(self.previousEduFrame, textvariable =
                    self.previousEduMajor[0])
            previousEduMajorEntry.grid(row=1, column=1)

            previousEduDegreeLabel = Label(self.previousEduFrame, text="Degree ")
            previousEduDegreeLabel.grid(row=2, column=0)

            previousEduDegreeEntry = Entry(self.previousEduFrame, textvariable
                    = self.previousEduDegree[0])
            previousEduDegreeEntry.grid(row=2, column=1)

            previousEduGradYearLabel = Label(self.previousEduFrame, text="Year of graduation ")
            previousEduGradYearLabel.grid(row=3, column=0)

            previousEduGradYearEntry = Entry(self.previousEduFrame,
                    textvariable = self.previousEduGradYear[0])
            previousEduGradYearEntry.grid(row=3, column=1)

            previousEduGPALabel = Label(self.previousEduFrame, text="GPA ")
            previousEduGPALabel.grid(row=4, column=0)

            previousEduGPAEntry = Entry(self.previousEduFrame, textvariable =
                    self.previousEduGPA[0])
            previousEduGPAEntry.grid(row=4, column=1)

            #second set
            previousEduSchoolNameLabel1 = Label(self.previousEduFrame, text="Name of Institution Attended ")
            previousEduSchoolNameLabel1.grid(row=5, column=0)

            previousEduSchoolNameEntry1 = Entry(self.previousEduFrame,
                    textvariable = self.previousEduSchool[1])
            previousEduSchoolNameEntry1.grid(row=5, column=1)

            previousEduMajorLabel1 = Label(self.previousEduFrame, text="Major ")
            previousEduMajorLabel1.grid(row=6, column=0)

            previousEduMajorEntry1 = Entry(self.previousEduFrame, textvariable
                    = self.previousEduMajor[1])
            previousEduMajorEntry1.grid(row=6, column=1)

            previousEduDegreeLabel1 = Label(self.previousEduFrame, text="Degree ")
            previousEduDegreeLabel1.grid(row=7, column=0)

            previousEduDegreeEntry1 = Entry(self.previousEduFrame, textvariable
                    = self.previousEduDegree[1])
            previousEduDegreeEntry1.grid(row=7, column=1)

            previousEduGradYearLabel1 = Label(self.previousEduFrame, text="Year of graduation ")
            previousEduGradYearLabel1.grid(row=8, column=0)

            previousEduGradYearEntry1 = Entry(self.previousEduFrame,
                    textvariable = self.previousEduGradYear[1])
            previousEduGradYearEntry1.grid(row=8, column=1)

            previousEduGPALabel1 = Label(self.previousEduFrame, text="GPA ")
            previousEduGPALabel1.grid(row=9, column=0)

            previousEduGPAEntry1 = Entry(self.previousEduFrame, textvariable =
                    self.previousEduGPA[1])
            previousEduGPAEntry1.grid(row=9, column=1)

            # third set
            previousEduSchoolNameLabel2 = Label(self.previousEduFrame, text="Name of Institution Attended ")
            previousEduSchoolNameLabel2.grid(row=10, column=0)

            previousEduSchoolNameEntry2 = Entry(self.previousEduFrame,
                    textvariable = self.previousEduSchool[2])
            previousEduSchoolNameEntry2.grid(row=10, column=1)

            previousEduMajorLabel2 = Label(self.previousEduFrame, text="Major ")
            previousEduMajorLabel2.grid(row=11, column=0)

            previousEduMajorEntry2 = Entry(self.previousEduFrame, textvariable
                    = self.previousEduMajor[2])
            previousEduMajorEntry2.grid(row=11, column=1)

            previousEduDegreeLabel2 = Label(self.previousEduFrame, text="Degree ")
            previousEduDegreeLabel2.grid(row=12, column=0)

            previousEduDegreeEntry2 = Entry(self.previousEduFrame, textvariable
                    = self.previousEduDegree[2])
            previousEduDegreeEntry2.grid(row=12, column=1)

            previousEduGradYearLabel2 = Label(self.previousEduFrame, text="Year of graduation ")
            previousEduGradYearLabel2.grid(row=13, column=0)

            previousEduGradYearEntry2 = Entry(self.previousEduFrame,
                    textvariable = self.previousEduGradYear[2])
            previousEduGradYearEntry2.grid(row=13, column=1)

            previousEduGPALabel2 = Label(self.previousEduFrame, text="GPA ")
            previousEduGPALabel2.grid(row=14, column=0)

            previousEduGPAEntry2 = Entry(self.previousEduFrame, textvariable =
                    self.previousEduGPA[2])
            previousEduGPAEntry2.grid(row=14, column=1)

    def addEdu(self):
        if len(self.previousEduGradYear) > 2:
            return

        self.previousEduFrame.pack_forget()
        self.buttonFrame.pack_forget()

        tmp = StringVar(value="")
        self.previousEduSchool.append(tmp)
        tmp = IntVar(value="")
        self.previousEduGradYear.append(tmp)
        tmp = StringVar(value="")
        self.previousEduDegree.append(tmp)
        tmp = StringVar(value="")
        self.previousEduMajor.append(tmp)
        tmp = DoubleVar(value="")
        self.previousEduGPA.append(tmp)

        self.previousEduFrame.pack()
        self.buttonFrame.pack(fill=X)
        self.populatePreviousEdu(1)

    def submit(self):
        db4 = pymysql.connect(host = "academic-mysql.cc.gatech.edu" , passwd = "a1Rlxylj", user = "cs4400_Group36", db='cs4400_Group36')
        c = db4.cursor()
        try:
            #put personal info update here
            if self.name.get() == "" or self.dob.get() == "" or self.gender.get() == "" or self.address.get() == "" or self.permAddress.get() == "" or self.contactNumber.get() == "" or self.email.get() == "":
                showwarning("ERROR","Invalid personal info submission")
                return
            else:
                query = "SELECT count( *) FROM student WHERE username=%s"
                c.execute(query, (self.username))
                count = c.fetchall()[0][0]
                if count == 1:
                    query = "UPDATE student SET major=%s, degree=%s, address=%s, name=%s, email=%s, dob=%s, permAddress=%s, gender=%s, contactNum=%s WHERE username=%s"
                    c.execute(query,
                            (self.major.get(),self.degree.get(),self.address.get(),self.name.get(),
                                self.email.get(),self.dob.get(),self.permAddress.get(),self.gender.get(),
                                self.contactNumber.get(),self.username))
                else:
                    showwarning("ERROR","Could not find student in database")
                    return

            for course in self.tutorCoursesSelected:
                query = """SELECT courseTitle FROM courseSection
                WHERE courseCode=%s"""
                c.execute(query, (course))
                course_title = c.fetchall()[0][0]
                query = """SELECT count( *) FROM tutorsFor WHERE tutorUsername=%s
                AND courseTitle=%s"""
                c.execute(query, (self.username, course_title))
                count1 = c.fetchall()[0][0]
                query = """SELECT count( *) FROM appliesForTutor WHERE studentUsername=%s
                AND courseTitle=%s"""
                c.execute(query, (self.username, course_title))
                count2 = c.fetchall()[0][0]
                if count1 == 1 or count2 == 1:
                    showwarning("ERROR","You cannot register to tutor for " +
                            course_title)
                    return
                else:
                    query = """INSERT INTO appliesForTutor VALUES(%s,%s)"""
                    c.execute(query, (self.username, course_title))

            for i in range(len(self.previousEduGradYear)):
                if self.previousEduSchool[i].get() == "" or self.previousEduMajor[i].get() == "" or self.previousEduDegree[i].get() == "":
                    #showwarning("ERROR","Invalid previous edu submission")
                    #return
                    break
                else:
                    query = "SELECT count( *) FROM eduHistory WHERE studentUsername=%s AND nameOfSchool=%s AND yearOfGrad=%s"
                    c.execute(query, (self.username,self.previousEduSchool[i].get(),self.previousEduGradYear[i].get()))
                    count = c.fetchall()[0][0]
                    if count == 1:
                        query = "UPDATE eduHistory SET degree=%s, major=%s, gpa=%s WHERE studentUsername=%s AND nameOfSchool=%s AND yearOfGrad=%s"
                        c.execute(query, (self.previousEduDegree[i].get(),self.previousEduMajor[i].get(),
                            self.previousEduGPA[i].get(),self.username,self.previousEduSchool[i].get(),
                            self.previousEduGradYear[i].get()))
                    else:
                        query = "INSERT INTO eduHistory VALUES(%s,%s,%s,%s,%s,%s)"
                        c.execute(query, (self.username,self.previousEduSchool[i].get(),self.previousEduGradYear[i].get(),
                        self.previousEduDegree[i].get(),self.previousEduMajor[i].get(),
                        self.previousEduGPA[i].get()))
            showinfo("Success", "You successfully updated your information")
        except:
            showwarning("ERROR","Something went wrong")
        c.close()
        db4.commit()
        db4.close()
        self.root.destroy()
        self.Driver.launch_homepage([1,0,0],self.username)

    def removeFromSelected(self):
        del self.tutorCoursesSelected[:]
        self.tutorCoursesText.delete("1.0", END)

    def radio_yes(self):
        self.tutorCoursesOptionMenu.grid_remove()
        self.tutorCourses = self.getTutorCourse()
        self.tutorCoursesOptionMenu = OptionMenu(self.tutorCoursesFrame,
                self.currentTutorCourse, *self.tutorCourses)
        self.tutorCoursesOptionMenu.grid(row=0,column=1)

    def radio_no(self):
        self.tutorCoursesOptionMenu.grid_remove()
        del self.tutorCourses[:]
        self.tutorCourses.append("--")
        self.tutorCoursesOptionMenu = OptionMenu(self.tutorCoursesFrame,
                self.currentTutorCourse, *self.tutorCourses)
        self.tutorCoursesOptionMenu.grid(row=0,column=1)

# This is the main method of the Login file to be used for debuggin purposes.
# This method is used to create an instance of the Login class.
if __name__=='__main__':
    app = StudentPI()
