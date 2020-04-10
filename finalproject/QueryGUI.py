import tkinter as tk
from tkinter.filedialog import askopenfile

window = tk.Tk()
window.title("UGrade")
window.geometry('500x300+700+200')

def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 

namePrompt = tk.Label(window, text="What's your name? ")
namePrompt.grid(row=0,column=0, sticky=tk.W)

nameEntry = tk.Entry(window)
nameEntry.grid(row=0,column=1)

filePrompt = tk.Label(window, text="Enter your grades here:   ")
filePrompt.grid(row=1,column=0, sticky=tk.W)

btn = tk.Button(window, text ='Open', command = lambda:open_file()) 
btn.grid(row=1,column=1)

window.mainloop()
window.destroy()