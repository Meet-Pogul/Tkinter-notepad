from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno, showinfo
import webbrowser
import os

info = ""
fontsize = 12

# File Function


def New():
    global file, info
    # if TextArea.get(1.0, END) != info and askyesno("Save", "Would You Like To Save The Changes?") == True:
    #     Save()
    file = None
    root.title("Untitled - Notepad")
    TextArea.delete(1.0, END)
    info = TextArea.get(1.0, END)


def Open():
    global file, info
    # if TextArea.get(1.0, END) != info and askyesno("Save", "Would You Like To Save The Changes?") == True:
    #     Save()
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0, END)
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())
            info = f.read()


def Save():
    global file
    if file == None:
        Save_As()
    else:
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))


def Save_As():
    file = asksaveasfilename(defaultextension=".txt", filetypes=[
        ("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        # Save as new File
        with open(file, "w") as f:
            f.write(TextArea.get(1.0, END))
        root.title(os.path.basename(file) + " - Notepad")


def Exit():
    global info
    if TextArea.get(1.0, END) != info and askyesno("Save", "Would You Like To Save The Changes?") == True:
        Save()
    root.destroy()
    exit()

# Edit Function


def Cut():
    TextArea.event_generate(("<<Cut>>"))


def Copy():
    TextArea.event_generate(("<<Copy>>"))


def Paste():
    TextArea.event_generate(("<<Paste>>"))

# View Functions


def Zoom_In():
    global fontsize
    fontsize += 1
    TextArea.config(font=("Times New Roman", fontsize))


def Zoom_Out():
    global fontsize
    fontsize -= 1
    TextArea.config(font=("Times New Roman", fontsize))

# Help Function


def View_Help():
    webbrowser.open_new_tab(
        r"https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA")


def Send_Feedback():
    webbrowser.open(r"https://www.instagram.com/meetpogul/")


def About_Notepad():
    showinfo("Help", "Welcome to MSP Notepad, Please Send Feedback\nSo, I can Know How's your Experience")


if __name__ == "__main__":
    # Initialization
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("650x750")

    # Add TextArea
    TextArea = Text(root, font=("Times New Roman", fontsize))
    TextArea.pack(expand=True, fill="both")
    Scroll = Scrollbar(TextArea, command=TextArea.yview)
    Scroll.pack(side=RIGHT, fill=Y)
    TextArea.config(yscrollcommand=Scroll.set)

    file = None

    # Lests Create a menubar
    MenuBar = Menu(root)
    menulist = {"File": [New, Open, Save, Save_As, Exit],
                "Edit": [Cut, Copy, Paste],
                "View": [Zoom_In, Zoom_Out],
                "Help": [View_Help, Send_Feedback, About_Notepad]}
    for i in menulist.keys():
        k = Menu(MenuBar, tearoff=0)
        for j in menulist[i]:
            if j == About_Notepad or j == Exit:
                k.add_separator()
            k.add_command(label=j.__name__.replace("_", " "), command=j)
        MenuBar.add_cascade(label=str(i), menu=k)
    info = TextArea.get(1.0, END)
    root.config(menu=MenuBar)
    File = Menu(MenuBar)
    root.mainloop()
