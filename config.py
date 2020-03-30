import csv
import ExperimentalStudent as es
import ControlledStudent as cs
import pickle

#given data
courses = ['COSC 111','COSC 121','COSC222','MATH 100','MATH 101','MATH200','PHYS 111',
'PHYS 121','PHYS 112','PHYS 122','PHYS 216', 'CHEM 121','CHEM 123']

majors = ['COSC','MATH','PHYS'], 

#initialize arrays to hold different types of students
controlledStudents = []
experimentalStudents = []

student = []