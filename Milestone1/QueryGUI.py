import tkinter as tk
from tkinter.filedialog import askopenfile

app = tk.Tk()
app.title("UGrade")
app.geometry('500x300+700+200')

content = 0
window = tk.Frame(app)


#
# Do everything you wanna do in this
#
def submit_file():
    # example usage of the entry fields, can remove of course
    print(content)
    answerLabel['text'] = nameEntry.get()+" in class "+lectureEntry.get()


#
# this handles reading in the file
#

def open_file(): 
    gradeFile = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if gradeFile is not None: 
        global content
        content = gradeFile.read()


namePrompt = tk.Label(window, text="What's your name? ")
namePrompt.grid(row=0,column=0, sticky=tk.W)

#
# Use nameEntry.get() to get the value user entered
#
nameEntry = tk.Entry(window)
nameEntry.grid(row=0,column=1)

fillerLabel1 = tk.Label(window, text="\n")
fillerLabel1.grid(row=1,column=1,sticky=tk.W+tk.E)

lecturePrompt = tk.Label(window, text="What class mark do you want to predict? ")
lecturePrompt.grid(row=2,column=0, sticky=tk.W)

#
# Use lectureEntry.get() to get the class the user entered
# You can enter whatever and just have it as filler
#
lectureEntry = tk.Entry(window)
lectureEntry.grid(row=2,column=1)

fillerLabel1 = tk.Label(window, text="\n")
fillerLabel1.grid(row=3,column=1,sticky=tk.W+tk.E)

filePrompt = tk.Label(window, text="Enter your grades here:   ")
filePrompt.grid(row=4,column=0, sticky=tk.W)

btn = tk.Button(window, text ='Open', command = lambda:open_file()) 
btn.grid(row=4,column=1)

fillerLabel = tk.Label(window, text="\n")
fillerLabel.grid(row=5,column=1,sticky=tk.W+tk.E)

submitButton = tk.Button(window,text='Predict!', command = lambda:submit_file())
submitButton.grid(row=6,column=0,sticky=tk.W+tk.E)

#
# This is what our answer will print into
#
answerLabel = tk.Label(window, text="")
answerLabel.grid(row=6,column=1,sticky=tk.E)

window.pack(padx=10,pady=50)
window.mainloop()
window.destroy()