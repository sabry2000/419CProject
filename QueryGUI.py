import tkinter as tk

window = tk.Tk()
window.title("UGrade")
window.geometry('500x300+700+200')

greeting = tk.Label(window, text="UGrade Grade Predictor", height=2, bg="green", fg="white")
titleFont = ('default',20,"bold")
greeting.config(font=titleFont)
greeting.pack(pady=5, padx=5, fill='x')

def open_file(): 
    file = penfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content) 
  
btn = tk.Button(window, text ='Open', command = lambda:open_file()) 
btn.pack(side ='top', pady = 10) 

window.mainloop()
window.destroy()