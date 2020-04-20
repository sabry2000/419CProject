#This file contains a function that will allow the administrator to read the data from the Survey.csv file, create the appropriate student objects,
#and store the students in their corresponding lists
import csv
from Student import LYStudent as lys
from Student import UYStudent as uys

#open the csv file
with open('data/Student Grades Survey.csv','r') as data:
    reader = csv.reader(data, delimiter=',')
    
    #initialize variables to help read the csv file
    stypeindex = 0
    start = 0
    upper_year_start = 0
    lower_year_start = 0

    lower_year = []
    upper_year = []
    
    #get the indices of the csv headings
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

    #read the rest of the file and extract the student data
    students = list(reader)
    for student in students:
        stype = student[stypeindex]                                                 #get the student type
        fyc = list(map(int, student[start:lower_year_start]))                       #get the first year course grades
        if stype == 'Lower Year':                                                   #if it is an lower_year student, do the following
            interests = list(map(int,student[lower_year_start:upper_year_start]))   #get their interests
            student = lys(fyc,interests)                                            #store their information
            lower_year.append(student)
        elif stype == 'Upper Year':                                                 #if it is a upper_year student, do the following
            major = student[upper_year_start]                                       #store their major
            uyc = list(map(int, student[upper_year_start+1:]))                      #store the grades of the upper year courses
            student = uys(fyc,uyc,major)
            upper_year.append(student)
        else:
            continue
