#This file contains a function that will allow the administrator to read the data from the Survey.csv file, create the appropriate student objects,
#and store the students in their corresponding lists in the global variables
import csv
from ExperimentalStudent import ExperimentalStudent as es
from ControlledStudent import ControlledStudent as cs

#initialize variables to help read the csv file
stypeindex = 0
start = 0
controlledstart = 0
experimentalstart = 0

#initialize arrays to hold students
experimental, controlled = [], []

def analyzeCSV(reader):
    global stypeindex, start, controlledstart, experimentalstart
    csv_headings = next(reader)
    for i,element in enumerate(csv_headings):
        if element == 'Would you like to participate in Part 1 or Part 2?':
            stypeindex = i
            continue
        elif element == 'COSC 111?':
            start = i
            continue
        elif element == 'How interested are you in COSC?':
            experimentalstart = i
            continue
        elif element == 'What is your major?':
            controlledstart = i
            break
    
    students = list(reader)
    return students

def getExperimentalStudents(students):
    experimental = []
    for student in students:
        stype = student[stypeindex]                                                 #get the student type
        if stype == 'Part 1':                                                       #if it is an experimental student, do the following
            fyc = list(map(int, student[start:experimentalstart]))                  #get the first year course grades
            interests = student[experimentalstart:controlledstart]                  #get their interests
            student = es(fyc,interests)                                             #store their information
            experimental.append(student)
        else:
            continue
    return experimental

def getControlledStudents(students):
    controlled = []
    for student in students:
        stype = student[stypeindex]                                                 #get the student type
        if stype == 'Part 2':                                                       #if it is a controlled student, do the following
            fyc = list(map(int, student[start:experimentalstart]))                  #get the first year course grades
            major = student[controlledstart]                                        #store their major
            uyc = list(map(int, student[controlledstart+1:]))                       #store the grades of the upper year courses
            student = cs(fyc,uyc,major)
            controlled.append(student)
        else:
            continue
    return controlled

#open the csv file
with open('Survey.csv','r') as data:
    #global experimental, controlled
    reader = csv.reader(data, delimiter=',')
    students = analyzeCSV(reader)
    experimental = getExperimentalStudents(students)
    controlled = getControlledStudents(students)