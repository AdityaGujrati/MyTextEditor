from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def menuAtTop():
    # add textarea

    def about():
        showinfo("Notepad", "Notepad by Aditya Gujrati")

    def newFile():
        global file
        root.title("Untitled-Notepad")
        file = None
        TextArea.delete(1.0, END)

    def OpenFile():
        global file
        file = askopenfilename(defaultextension=".txt", filetypes=[
            ("All Files", "*.*"), ("Text Document", "*.*")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file)+"-Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()

    def SaveFile():
        global file
        if file == None:
            file = asksaveasfilename(initialfile="Untitiled.txt",
                                     defaultextension=".txt", filetypes=[
                                         ("All Files", "*.*"), ("Text Document", "*.*")]
                                     )
            if file == "":
                file = None
            else:
                f = open(file, "w")
                f.write(TextArea.get(1.0, END))
                f.close()
                root.title(os.path.basename(file)+"-Notepad")
                print("file is saved")
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

    def QuitApp():
        root.destroy()

    def cut():
        TextArea.event_generate(("<<Cut>>"))

    def Copy():
        TextArea.event_generate(("<<Copy>>"))

    def Paste():
        TextArea.event_generate(("<<Paste>>"))

    TextArea = Text(root, font="lucidia 13")
    TextArea.pack(expand=True, fill=BOTH)
    file = None
    Menubar = Menu(root)
    # filemenu
    FileMenu = Menu(Menubar, tearoff=0)
    # to open the file
    FileMenu.add_command(label="New", command=newFile)
    # to open file already
    FileMenu.add_command(label="Open", command=OpenFile)
    FileMenu.add_command(label="Save", command=SaveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=QuitApp)
    FileMenu.add_command(label="Split", command=menuAtTop)
    Menubar.add_cascade(label="File", menu=FileMenu)

    # edit menu
    EditMenu = Menu(Menubar, tearoff=0)
    EditMenu.add_command(label="cut", command=cut)
    EditMenu.add_command(label="Copy", command=Copy)
    EditMenu.add_command(label="Paste", command=Paste)
    Menubar.add_cascade(label="Edit", menu=EditMenu)
    root.config(menu=Menubar)
    #    help menu
    HelpMenu = Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    Menubar.add_cascade(label="Help", menu=HelpMenu)
    # adding scrollBar
    scroll = Scrollbar(TextArea, cursor="arrow")
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)


def NewWindow():
    global i
    root1 = Tk()
    root1.title("Notepad")
    root1.geometry("400x500")
    menuAtTop()
    root.mainloop()

i=1
if __name__ == "__main__":
    root = Tk()
    root.title("Notepad")
    root.geometry("400x500")
    menuAtTop()
    root.mainloop()
