from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext

filename = None

global text_selected
text_selected = False
#The following methods are called in the filemenu of the window
def newFile():
    '''
    Creates a new file to be edited and saved
    '''
    global filename
    filename = None
    editor.title("untitled-Akatsuki.txt")
    text.delete(0.0, END)
    
def saveFile():
    '''
    Saves all edits from previously saved .txt file. If not previously saved, saveAs is called in exception.
    '''
    global filename
    #within filename, all text from 0th row and 0th column to the end is gotten
    t = text.get(0.0, END)
    #file is saved under provided filename and text is written
    try:
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except:
        #if the file isn't already created, this does a saveAs
        f = filedialog.asksaveasfile(confirmoverwrite=False, mode = 'w', defaultextension = '.txt')
        t = text.get(0.0, END)
        try:
            filename = f.name
            display_name = filename[filename.rindex('/')+1:]
            f.write(t)
            editor.title(f"{display_name}")
        except:
            messagebox.showerror(title = "Oops!", message = "Unable to save file...")

def saveAs():
    '''
    Saves text in OS under designated name with default .txt extension
    '''
    global filename
    f = filedialog.asksaveasfile(confirmoverwrite=False, mode = 'w', defaultextension = '.txt')
    t = text.get(0.0, END)
    try:
        filename = f.name
        display_name = filename[filename.rindex('/')+1:]
        f.write(t)
        editor.title(f"{display_name}")
    except:
        messagebox.showerror(title = "Oops!", message = "Unable to save file...")
        
        
def openFile():
    '''
    Opens a .txt file created prior and displays text to edit
    '''
    global filename
    f = filedialog.askopenfile(mode = 'r')
    filename = f.name
    display_name = filename[filename.rindex('/')+1:]
    editor.title(f"{display_name}")
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def cut_text(event):
    global text_selected
    #check if keyboard shortcut was used
    if event:
        text_selected = editor.clipboard_get()
    else:
        if text.selection_get():
            text_selected = text.selection_get() #get selected text
            text.delete("sel.first", "sel.last") #delete selected text

            editor.clipboard_clear()  # clear what was initially on the clipboard
            editor.clipboard_append(text_selected)  # put selected text on the clipboard


def copy_text(event):
    global text_selected
    #check if keyboard shortcuts were used
    if event:
        text_selected = editor.clipboard_get()

    if text.selection_get():
        text_selected = text.selection_get()

        editor.clipboard_clear() #clear what was initially on the clipboard
        editor.clipboard_append(text_selected) # put selected text on the clipboard

def paste_text(event):
    global text_selected
    if event:
        text_selected = editor.clipboard_get()
    else:
        if text_selected:
            position = text.index(INSERT)
            text.insert(position, text_selected)


#setting up text editing window with Tkinter
editor = Tk()
editor.title("untitled-Akatsuki.txt")
editor.minsize(width = 500, height = 380)
editor.maxsize(width = 500, height = 380)

#adding text editing feature with scroll bar to Tkinter window
text = scrolledtext.ScrolledText(editor, undo=True)
text['font'] = ('consolas', '14')
text.pack(expand=True, fill='both')

#adding menu bar to Tkinter window
menubar = Menu(editor)

#filemenu items
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
menubar.add_cascade(label="File", menu=filemenu)

#editmenu items
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut   Ctrl+x", command=lambda: cut_text(False))
editmenu.add_command(label="Copy   Ctrl+c", command=lambda: copy_text(False))
editmenu.add_command(label="Paste   Ctrl+v", command=lambda: paste_text(False))
editmenu.add_command(label="Undo", command=text.edit_undo)
editmenu.add_command(label="Redo", command=text.edit_redo)
editmenu.add_separator()
menubar.add_cascade(label="Edit", menu=editmenu)

#shortcuts - binding
editor.bind("<Control-Key-x>", cut_text)
editor.bind("<Control-Key-c>", copy_text)
editor.bind("<Control-Key-v>", paste_text)


editor.config(menu=menubar)
editor.mainloop()