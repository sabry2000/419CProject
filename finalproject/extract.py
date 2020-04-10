#This file contains a function that will allow the administrator to read the data from the Survey.csv file, create the appropriate student objects,
#and store the students in their corresponding lists
import csv
from LowerYearStudent import LYStudent as lys
from UpperYearStudent import UYStudent as uys

#initialize variables to help read the csv file
stypeindex = 0
start = 0
upper_year_start = 0
lower_year_start = 0

def analyzeCSV(reader):
    global stypeindex, start, upper_year_start, lower_year_start
    csv_headings = next(reader)
    for i,element in enumerate(csv_headings):
        if element == 'Would you like to participate as an Upper Year or as a Lower Year student?':
            stypeindex = i
            continue
        elif element == 'COSC 111?':
            start = i
            continue
        elif element == 'How interested are you in COSC?':
            lower_year_start = i
            continue
        elif element == 'What is your major?':
            upper_year_start = i
            break
    
    students = list(reader)
    return students

def getLowerYearStudents(students):
    lower_year = []
    for student in students:
        stype = student[stypeindex]                                                 #get the student type
        if stype == 'Lower Year':                                                       #if it is an lower_year student, do the following
            fyc = list(map(int, student[start:lower_year_start]))                  #get the first year course grades
            interests = student[lower_year_start:upper_year_start]                  #get their interests
            student = lys(fyc,interests)                                             #store their information
            lower_year.append(student)
        else:
            continue
    return lower_year

def getUpperYearStudents(students):
    upper_year = []
    for student in students:
        stype = student[stypeindex]                                                 #get the student type
        if stype == 'Upper Year':                                                       #if it is a upper_year student, do the following
            fyc = list(map(int, student[start:lower_year_start]))                  #get the first year course grades
            major = student[upper_year_start]                                        #store their major
            uyc = list(map(int, student[upper_year_start+1:]))                       #store the grades of the upper year courses
            student = uys(fyc,uyc,major)
            upper_year.append(student)
        else:
            continue
    return upper_year

#open the csv file
with open('Student Grades Survey.csv','r') as data:
    #global lower_year, upper_year
    reader = csv.reader(data, delimiter=',')
    students = analyzeCSV(reader)
    lower_year = getLowerYearStudents(students)
    upper_year = getUpperYearStudents(students)