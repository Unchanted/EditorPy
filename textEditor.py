from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

filename = None

def new_file():
    global filename
    filename = "Untitled"
    text.delete(1.0, END)

def save_file():
    global filename
    if filename:
        with open(filename, 'w') as f:
            f.write(text.get(1.0, END))
    else:
        save_as()

def save_as():
    global filename
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f:
        filename = f.name
        try:
            with open(filename, 'w') as file:
                file.write(text.get(1.0, END).rstrip())
        except Exception as e:
            showerror(title="Error", message=f"Unable to save file: {e}")

def open_file():
    f = askopenfile(mode='r')
    if f:
        text.delete(1.0, END)
        text.insert(1.0, f.read())

root = Tk()
root.title("Text Editor in Python")
root.geometry("400x400")

text = Text(root)
text.pack(expand=YES, fill=BOTH)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save As...", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
