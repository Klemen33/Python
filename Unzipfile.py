from tkinter import *
from tkinter import messagebox
import zipfile



def Unzipping():
    file = filename.get()
    if ".zip" in file:
        pass
    else:
        file = file + ".zip"
    directory =directoryName.get()
    if file and directory:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(directory)
    else:
        messagebox.showerror("Error","Enter Filename and Directory.")

app = Tk()
app.title("Unzipping Files")

app.geometry("390x220")

label1 = Label(app,text="Welcome to Unzipit App\n",justify=CENTER,fg = "orange")
label1.grid(sticky=N,columnspan = 50)
label1.configure(font=("Helvetica", 14))
filename = StringVar()
directoryName = StringVar()

Label(app, text="      File Name or Path :-  * ",fg = "green").grid(row = 1,column = 0)
filename = Entry(app,width=35,fg = "navy")
filename.grid(row = 1,column = 1)
Label(app, text="       Where to Store?        *",fg = "green").grid(row = 2,column = 0)
directoryName = Entry(app,width=35,fg = "navy")
directoryName.grid(row = 2,column = 1)
Label(app, text = "\nYour files will be available in the directory you want.\n" ,fg = "blue").grid(row = 3,column = 0,columnspan = 65)

btn1 = Button(app,text="Unzip",activebackground="green",activeforeground='blue',bg = "blue",fg = "white",command=Unzipping)
btn1.grid(row = 4, column = 0,columnspan=100,rowspan=30)
btn1 = Button(app,text="Quit",activebackground="red",activeforeground='blue',bg = "yellow",fg = "red",command=app.destroy)
btn1.grid(row = 4, column = 1,columnspan=60,rowspan=30)

app.mainloop()

