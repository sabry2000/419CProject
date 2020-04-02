#This file contains a function that will allow the administrator to read the data from the Survey.csv file, create the appropriate student objects,
#and store the students in their corresponding lists in the global variables
import config
import ExperimentalStudent as es
import ControlledStudent as cs

def extract():
    #open the csv file
    with open('Survey.csv','r') as data:
        reader = config.csv.reader(data, delimiter=',')

        stypeindex = 0
        start = 0
        controlledstart = 0
        experimentalstart = 0
        
        csv_headings = next(reader)

        for i,element in enumerate(csv_headings):
            if element == 'Would you like to participate in Part 1 or Part 2?':
                stypeindex = i
                continue
            elif element == 'COSC 111? (if not applicable please type 0)':
                start = i
                continue
            elif element == 'How interested are you in COSC?':
                experimentalstart = i
                continue
            elif element == 'What is your major?':
                controlledstart = i
                break

        for student in reader:
            stype = student[stypeindex]                                                 #variable to hold student type
            fyc = list(map(int, student[start:experimentalstart]))                                    #get the first year course grades
            if stype == 'Part 1':
                interests = student[experimentalstart:controlledstart]                #array to hold student parameters
                student = es.ExperimentalStudent(fyc,interests)
                config.experimentalStudents.append(student)
            elif stype == 'Part 2':
                major = student[controlledstart]
                uyc = list(map(int, student[controlledstart+1:]))                                                #array to hold student parameters
                student = cs.ControlledStudent(fyc,uyc,major)
                config.controlledStudents.append(student)
            else:
                continue

    with open("data.pickle", "wb") as f:
        config.pickle.dump((config.experimentalStudents, config.controlledStudents), f)

if __name__ == "__main__":
    extract()
