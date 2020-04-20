import tkinter as tk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import tkinter.ttk as ttk

import project
import config
import tests as t

app = tk.Tk()
app.title("UniNav")
app.geometry('500x300+700+200')

content = 0
window = tk.Frame(app)


#
# Do everything you wanna do in this
#
def submit_request():
    # example usage of the entry fields, can remove of course
    #print(content)
    #answerLabel['text'] = nameEntry.get()+" in class "+lectureEntry.get()
    response = tk.Toplevel(app)
    response.title('Your Prediction!!!')
    response.geometry('500x300+800+300')
    response.configure(bg = "#838383")
    area = tk.Frame(response)
    area.grid(row=0,column=0)
    area.configure(bg = "#838383")
    predictionLabel = ''
    # test or student?
    try:
        predictionLabel = tk.Label(area, text=project.printToGUI(config.lower_year_students[int(nameEntry.get())],'all' if lectureEntry.get() == "" else lectureEntry.get()))
    except:
        print("Test cases")
        if '1' in nameEntry.get():
            #predictionLabel = tk.Label(area, text=nameEntry.get())
            predictionLabel = tk.Label(area, text=project.printToGUI(t.testCase1(),'all' if lectureEntry.get() == "" else lectureEntry.get()))
        elif '2' in nameEntry.get():
            predictionLabel = tk.Label(area, text=project.printToGUI(t.testCase2(),'all' if lectureEntry.get() == "" else lectureEntry.get()))
        elif '3' in nameEntry.get():
            predictionLabel = tk.Label(area, text=project.printToGUI(t.testCase3(),'all' if lectureEntry.get() == "" else lectureEntry.get()))
        elif '4' in nameEntry.get():
            predictionLabel = tk.Label(area, text=project.printToGUI(t.testCase4(),'all' if lectureEntry.get() == "" else lectureEntry.get()))

    predictionLabel.grid(row=1,column=1)
    predictionLabel.configure(bg = "#838383")
    area.grid_rowconfigure(1, weight=1)
    area.grid_columnconfigure(1, weight=1)
    response.grid_rowconfigure(0, weight=1)
    response.grid_columnconfigure(0, weight=1)
    response.mainloop()


bannerOpen = Image.open('finalproject/build/UniNav_banner.png')
bannerRender = ImageTk.PhotoImage(bannerOpen)
bannerImage = ttk.Label(window, image=bannerRender,background="#838383")
bannerImage.grid(row=0,column=0,columnspan=3, rowspan=2)

namePrompt = tk.Label(window, text="Which Student are You Predicting? ")
namePrompt.grid(row=2,column=0, sticky=tk.W)
namePrompt.configure(bg = "#838383")

#
# Use nameEntry.get() to get the value user entered
#
nameEntry = tk.Entry(window)
nameEntry.grid(row=2,column=1)

fillerLabel1 = tk.Label(window, text="\n")
fillerLabel1.grid(row=3,column=1,sticky=tk.W+tk.E)
fillerLabel1.configure(bg = "#838383")

lecturePrompt = tk.Label(window, text="Specific Course Request? ")
lecturePrompt.grid(row=4,column=0, sticky=tk.W)
lecturePrompt.configure(bg = "#838383")

#
# Use lectureEntry.get() to get the class the user entered
# You can enter whatever and just have it as filler
#
lectureEntry = tk.Entry(window)
lectureEntry.grid(row=4,column=1)

fillerLabel2 = tk.Label(window, text="\n")
fillerLabel2.grid(row=5,column=1,sticky=tk.W+tk.E)
fillerLabel2.configure(bg = "#838383")

submitButton = tk.Button(window,text='Predict!', command = lambda:submit_request())
submitButton.grid(row=6,column=2,sticky=tk.W+tk.E)

#
# This is what our answer will print into
#
#answerLabel = tk.Label(window, text="")
#answerLabel.grid(row=6,column=1,sticky=tk.E)

window.pack(padx=10)
window.configure(bg = "#838383")
app.configure(bg = "#838383")
window.mainloop()
window.destroy()