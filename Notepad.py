from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import ctypes
import os

root = Tk()

file = None
def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        f = open(file,'r')
        TextArea.delete(1.0, END)
        TextArea.insert(1.0, f.read())
        f.close()

def saveAs():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()
        root.title(os.path.basename(file) + " - Notepad")
def exit():
    root.destroy()

def copy():
    TextArea.event_generate(("<<Copy>>"))


def cut():
    TextArea.event_generate(("<<Cut>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


v = BooleanVar()

def wrapFun():
    if v.get():
        TextArea.config(wrap=CHAR)
    else:
        TextArea.config(wrap=NONE)

def getFont():
    pass

def help():
    showinfo("NotePad", "This is notepad created by Pranav")


TextArea =None

scroll1 = Scrollbar(TextArea)
scroll2 = Scrollbar(TextArea, orient=HORIZONTAL)

TextArea = Text(root, font="Consolas  11", yscrollcommand=scroll1.set, xscrollcommand=scroll2.set, wrap=NONE)

scroll1.config(command=TextArea.yview)
scroll1.pack(fill=Y, side=RIGHT)

scroll2.config(command=TextArea.xview)
scroll2.pack(fill=X, side=BOTTOM)

TextArea.pack(fill=BOTH, expand=True)


Menubar = Menu(root)
FileMenu = Menu(Menubar, tearoff=0)
FileMenu.add_command(label="New", command=newFile)
FileMenu.add_command(label="Open", command=openFile)
FileMenu.add_command(label="Save", command=save)
FileMenu.add_command(label="Save As", command=saveAs)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=exit)

EditMenu = Menu(Menubar, tearoff=0)
EditMenu.add_command(label="Cut", command=cut)
EditMenu.add_command(label="Copy", command=copy)
EditMenu.add_command(label="Paste", command=paste)

FormatMenu = Menu(Menubar, tearoff=0)

FormatMenu.add_checkbutton(label="Word Wrap", command=wrapFun, variable=v)
FormatMenu.add_command(label="Font...", command=getFont)

HelpMenu = Menu(Menubar, tearoff=0)
HelpMenu.add_command(label="Help", command=help)


Menubar.add_cascade(label="File", menu=FileMenu)
Menubar.add_cascade(label="Edit", menu=EditMenu)
Menubar.add_cascade(label="Format", menu=FormatMenu)
Menubar.add_cascade(label="Help", menu=HelpMenu)

root.config(menu=Menubar)
root.title("Untitled - Notepad")
root.geometry(f"{int(root.winfo_screenwidth()/2)}x{root.winfo_screenheight()-300}+{int(root.winfo_screenwidth()/2-330)}+80")
myappid = " " # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconbitmap("notepad-icon.ico")

root.mainloop()