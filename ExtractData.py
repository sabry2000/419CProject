import xlrd
import ExperimentalStudent as es
import ControlledStudent as cs

#open the xlsx file
workbook = xlrd.open_workbook('test.xlsx')
worksheet = workbook.sheet_by_index(0)

#get general parameters
rows = worksheet.nrows
cols = worksheet.ncols

#initialize arrays to hold different types of students
controlledStudents = []
experimentalStudents = []

#read every row in the file
for i in range(1,rows):
    typeofstudent = worksheet.cell_value(i,1)                                   #get the type of student
    values = []                                                                 #array to hold student parameters

    if typeofstudent == 'Part 1':                                               #if it is a es, do this
        for j in range(2,17):
            values.append(worksheet.cell_value(i,j))
        student = es.ExperimentalStudent(values)
        experimentalStudents.append(student)
    
    else:                                                                       #if it is a cs, do this
        for j in range(17,cols):
            values.append(worksheet.cell_value(i,j))
        student = cs.ControlledStudent(values)
        controlledStudents.append(student)