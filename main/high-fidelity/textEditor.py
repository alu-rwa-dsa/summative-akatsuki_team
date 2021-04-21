# Python TextEditor Code
# Using Python 3.6.5 and Tkinter
# By Akatsuki Team

""" NOTE: 1. Lambda function always takes arguments
          2. Only if u use undo will redo work """

# import tkinter module
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import os
import time
import hashlib


# creates GUI (Graphical User Interface)
root = Tk()
root.title("Untitled - Akatsuki Text Editor")
# root.protocol("WM_DELETE_WINDOW", lambda: __quit(1))
status = Label(
    root, text="", bd=1, relief=SUNKEN, anchor=W
)  # all this is for status bar
status.pack(side=BOTTOM, fill=X)
root.geometry("{}x{}".format(900, 500))

fontdict = {"family": "Calibri", "size": 14, "style": "normal"}

e = ScrolledText(
    root,
    bg="black",
    fg="white",
    insertbackground="white",
    selectbackground="blue",
    font=(fontdict["family"], fontdict["size"], fontdict["style"]),
    undo=True,
)
e.pack(fill="both", expand=True)

# Shortcuts
root.bind(
    "<Escape>", lambda x: root.attributes("-fullscreen", False)
)  # only if u use F11 will F5 work
root.bind("<F5>", lambda x: e.insert(INSERT, time.ctime()))
root.bind("<F4>", lambda x: e.insert(INSERT, colorchooser.askcolor()))
root.bind("<Control_L>+", lambda x: set_font_size(fontdict["size"] + 5))
root.bind("<Control_L>-", lambda x: set_font_size(fontdict["size"] - 5))
root.bind("<Control_L><d>", lambda x: delete_all(1))
root.bind("<Control_L><f>", lambda x: find(1))
root.bind("<Control_L><h>", lambda x: replace(1))


# status bar
def wordcount():
    status.config(
        text="Character count: "
        + str(len(e.get(1.0, "end-1c")))
        + "      Word count: "
        + str(len(e.get(1.0, "end-1c").split()))
        + "      Line count: "
        + str(len(e.get(1.0, "end-1c").split("\n")))
    )  # returns line count)
    root.after(200, wordcount)  # for refreshing or something


# create new file
def new(self):
    if root.title() == "Untitled - Akatsuki Text Editor":
        # There is content?
        if len(e.get("0.0", END)) > 1:  # non empty
            if messagebox.askyesno("Save?", "Do you wish to save?"):
                root.filename = filedialog.asksaveasfilename(
                    parent=root,
                    title="Save as",
                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                    defaultextension=".txt",
                )

                if root.filename:  # if file has a name
                    try:
                        with open(root.filename, "w", encoding="utf8") as w:
                            w.write(e.get(1.0, END))
                            e.delete("0.0", END)
                    except:
                        messagebox.showerror("Save file", "Could not save that file.")
                        return
                else:  # no name entered
                    messagebox.showerror("Error", "You did not enter a name to save")
                    return

            else:
                e.delete("0.0", END)
                root.title("Untitled - Akatsuki Text Editor")
        else:
            return

    # titled
    else:
        handle = open(root.filename, "r")
        if len(e.get("0.0", END)) != (
            len(handle.read()) + 1
        ):  # if it has been modified
            handle.close()
            if messagebox.askyesno("Save?", "Do you wish to save?"):

                try:
                    with open(root.filename, "w", encoding="utf8") as w:
                        w.write(e.get(1.0, END))
                        e.delete("0.0", END)
                        root.title("Untitled - Akatsuki Text Editor")
                except:
                    messagebox.showerror("Save file", "Could not save that file.")
                    return
            else:
                e.delete("0.0", END)
                root.title("Untitled - Akatsuki Text Editor")
        else:
            e.delete("0.0", END)
            root.title("Untitled - Akatsuki Text Editor")
        handle.close()


# open file
def openfile(self):
    # ----------------------------------------------- NON-EMPTY --------------------------------------------------------
    if len(e.get("0.0", END)) > 1:
        # --------------- UNTITLED ------------------
        if root.title() == "Untitled - Akatsuki Text Editor":
            if messagebox.askyesno("Save?", "Do you wish to save?"):

                # first save current file
                root.filename = filedialog.asksaveasfilename(
                    parent=root,
                    title="Save as",
                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                    defaultextension=".txt",
                )

                if root.filename:
                    try:
                        with open(root.filename, "w", encoding="utf8") as w:
                            w.write(e.get(1.0, END))
                    except:
                        messagebox.showerror("Save file", "Could not save that file.")
                        return

                else:
                    messagebox.showerror("Error", "You did not enter a name to save")
                    return

                # then open new file
                root.filename = filedialog.askopenfilename(
                    parent=root,
                    title="Open File",
                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                )

                if root.filename:
                    try:
                        with open(root.filename, "r", encoding="utf8") as w:
                            e.delete(0.0, END)
                            root.title(
                                os.path.basename(root.filename)
                                + " - Akatsuki Text Editor"
                            )
                            e.insert(END, w.read())
                    except:
                        messagebox.showerror("Open file", "Could not open that file.")
                        return
                else:
                    messagebox.showerror("Error", "You did not enter a filename")
                    return

            else:
                # open window pops up
                root.filename = filedialog.askopenfilename(
                    parent=root,
                    title="Open File",
                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                )

                if root.filename:
                    try:
                        with open(root.filename, "r", encoding="utf8") as w:
                            e.delete(0.0, END)
                            root.title(
                                os.path.basename(root.filename)
                                + " - Akatsuki Text Editor"
                            )
                            e.insert(END, w.read())
                    except:
                        messagebox.showerror("Open file", "Could not open that file.")
                        return

                else:
                    messagebox.showerror("Error", "You did not enter a filename")
                    return

        # ------------------ TITLED --------------------
        else:
            handle = open(root.filename, "r")
            # ---------- MODIFIED ----------
            if len(e.get("0.0", END)) != (len(handle.read()) + 1):
                handle.close()
                x = root.filename
                if messagebox.askyesno("Save?", "Do you wish to save?"):

                    # first save current file
                    try:
                        with open(x, "w", encoding="utf8") as w:
                            w.write(e.get("1.0", END))
                    except:
                        messagebox.showerror("Save file", "Could not save that file.")
                        return

                    # then open file
                    x = filedialog.askopenfilename(
                        parent=root,
                        title="Open File",
                        filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                    )

                    if x:
                        try:
                            with open(x, "r", encoding="utf8") as w:
                                e.delete(0.0, END)
                                root.title(
                                    os.path.basename(x) + " - Akatsuki Text Editor"
                                )
                                e.insert(END, w.read())
                        except:
                            messagebox.showerror(
                                "Open file", "Could not open that file."
                            )
                            return

                    else:
                        messagebox.showerror("Error", "You did not enter a filename")
                        return

                else:
                    x = filedialog.askopenfilename(
                        parent=root,
                        title="Open File",
                        filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                    )

                    if x:
                        try:
                            with open(x, "r", encoding="utf8") as w:
                                e.delete(0.0, END)
                                root.title(
                                    os.path.basename(x) + " - Akatsuki Text Editor"
                                )
                                e.insert(END, w.read())
                        except:
                            messagebox.showerror(
                                "Open file", "Could not open that file."
                            )
                            return

                    else:
                        messagebox.showerror("Error", "You did not enter a filename")
                        return

            # --------- NOT MODIFIED ---------
            else:
                handle.close()
                x = filedialog.askopenfilename(
                    parent=root,
                    title="Open File",
                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                )

                if x:
                    try:
                        with open(x, "r", encoding="utf8") as w:
                            e.delete(1.0, END)
                            root.title(os.path.basename(x) + " - Akatsuki Text Editor")
                            e.insert(END, w.read())
                    except:
                        messagebox.showerror("Open file", "Could not open that file.")
                        return

                else:
                    messagebox.showerror("Error", "You did not enter a filename")
                    return

    # -------------------------------------------------- IF EMPTY ------------------------------------------------------
    else:
        # -------------------- UNTITLED ----------------------
        if root.title() == "Untitled - Akatsuki Text Editor":

            root.filename = filedialog.askopenfilename(
                parent=root,
                title="Open File",
                filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
            )

            if root.filename:
                try:
                    with open(root.filename, "r", encoding="utf8") as w:
                        root.title(
                            os.path.basename(root.filename) + " - Akatsuki Text Editor"
                        )
                        e.insert(0.0, w.read())
                except:
                    messagebox.showerror("Open file", "Could not open that file.")
                    return

            else:
                messagebox.showerror("Error", "You did not enter a filename")
                return

        # --------------------- TITLED -----------------------
        else:
            handle = open(root.filename, "r")
            # ---------- MODIFIED ----------
            if len(e.get("0.0", END)) != (len(handle.read()) + 1):
                handle.close()
                x = root.filename
                if messagebox.askyesno("Save?", "Do you wish to save?"):

                    # first save current file
                    try:
                        with open(x, "w", encoding="utf8") as w:
                            w.write(e.get("1.0", END))
                    except:
                        messagebox.showerror("Save file", "Could not save that file.")
                        return

                    # then open file
                    x = filedialog.askopenfilename(
                        parent=root,
                        title="Open File",
                        filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                    )

                    if x:
                        try:
                            with open(x, "r", encoding="utf8") as w:
                                root.title(
                                    os.path.basename(x) + " - Akatsuki Text Editor"
                                )
                                e.insert(END, w.read())
                        except:
                            messagebox.showerror(
                                "Open file", "Could not open that file."
                            )
                            return

                    else:
                        messagebox.showerror("Error", "You did not enter a filename")
                        return

                else:
                    with open(x, "r", encoding="utf8") as w:
                        e.insert(END, w.read())

                    x = filedialog.askopenfilename(
                        parent=root,
                        title="Open File",
                        filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                    )

                    if x:
                        try:
                            with open(x, "r", encoding="utf8") as w:
                                root.title(
                                    os.path.basename(x) + " - Akatsuki Text Editor"
                                )
                                e.insert(END, w.read())
                        except:
                            messagebox.showerror(
                                "Open file", "Could not open that file."
                            )
                            return

                    else:
                        messagebox.showerror("Error", "You did not enter a filename")
                        return

            # --------- NOT MODIFIED ---------
            else:
                handle.close()
                x = filedialog.askopenfilename(
                    parent=root,
                    title="Open File",
                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                )

                if x:
                    try:
                        with open(x, "r", encoding="utf8") as w:
                            root.title(os.path.basename(x) + " - Akatsuki Text Editor")
                            e.insert(END, w.read())
                    except:
                        messagebox.showerror("Open file", "Could not open that file.")
                        return

                else:
                    messagebox.showerror("Error", "You did not enter a filename")
                    return


# Save file
def save(self):
    if root.title() == "Untitled - Akatsuki Text Editor":
        root.filename = filedialog.asksaveasfilename(
            parent=root,
            title="Save as",
            filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
            defaultextension=".txt",
        )

        if root.filename:
            try:
                with open(root.filename, "w", encoding="utf8") as w:
                    w.write(e.get(1.0, END))
                    root.title(
                        os.path.basename(root.filename) + " - Akatsuki Text Editor"
                    )
            except:
                messagebox.showerror("Save file", "Could not save that file.")
                return
        else:
            messagebox.showerror("Error", "You did not enter a name to save")
            return
    else:
        with open(root.filename, "w", encoding="utf8") as w:
            w.write(e.get(1.0, END))


# Save as function
def saveas():
    root.filename = filedialog.asksaveasfilename(
        parent=root,
        title="Save as",
        filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
        defaultextension=".txt",
    )
    if root.filename:
        try:
            with open(root.filename, "w", encoding="utf8") as w:
                w.write(e.get(1.0, END))
        except:
            messagebox.showerror("Save file", "Could not save that file.")
            return
    else:
        messagebox.showerror("Error", "You did not enter a name to save")
        return


# Checksum function(Hashing)
def checksum(algorithm, data):

    # text editor untitled
    if root.title() == "Untitled - Akatsuki Text Editor":
        messagebox.showerror("Error", "Save current file first or open a saved file.")

    # text editor has name
    else:
        if algorithm == "simple hash":
            sum = 0
            mul = 1
            for char in data:
                mul *= ord(char) * 10
                sum += mul
                mul = 1
            __checksum = str(sum)
        elif algorithm == "md5":
            __checksum = hashlib.md5(data).hexdigest()
        elif algorithm == "sha1":
            __checksum = hashlib.sha1(data).hexdigest()
        elif algorithm == "sha224":
            __checksum = hashlib.sha224(data).hexdigest()
        elif algorithm == "sha256":
            __checksum = hashlib.sha256(data).hexdigest()
        elif algorithm == "sha384":
            __checksum = hashlib.sha384(data).hexdigest()
        elif algorithm == "sha512":
            __checksum = hashlib.sha512(data).hexdigest()
        root.clipboard_clear()
        root.clipboard_append(__checksum)
        try:
            filepath = (
                root.filename
            )  # full path of file - root.filename() does not work
            handle1 = open(
                "/home/mamane19/chechsum.txt", "r+"
            )  # open file in read and append mode
            handle2 = open(
                "/home/mamane19/chechsum.txt", "a"
            )  # open file in append mode
            toWrite = filepath + " | " + algorithm + " | " + __checksum + "\n"
            lines1 = handle1.readlines()  # creates a list
            found = False
            for line in lines1:
                path1, alg1, hashvalue1 = line.split(" | ")
                if path1 == filepath and algorithm == alg1 in line:
                    found = True
                    break
            if found is False:
                handle1.write(toWrite)
                handle1.close()
            else:
                handle2.write(toWrite)
                handle2.close()
                handle1.close()
                dataintegrity(filepath)
        except:
            messagebox.showerror("Error", "Unable to calculate checksum of file")
        _checksum = __checksum
        print(_checksum)


def dataintegrity(fp):
    handle1 = open("/home/mamane19/chechsum.txt", "r")
    handle2 = open("/home/mamane19/chechsum.txt", "r")
    lines1 = handle1.readlines()
    lines2 = handle2.readlines()

    time.sleep(2)
    for i in lines2:  # scan checksum2

        path2, alg2, hashvalue2 = i.split(" | ")  # split each line in 2nd file
        for j in lines1:
            path1, alg1, hashvalue1 = j.split(" | ")
            if i == j:
                messagebox.showinfo(
                    "Data Integrity",
                    " File " + os.path.basename(fp) + " is not modified or corrupted.",
                )

                # remove entries of that filename
                handle1.close()
                handle1 = open("/home/mamane19/chechsum.txt", "w")
                for line in lines1:
                    if fp not in line:
                        handle1.write(line)
                handle1.close()

                # delete content of 2nd file
                handle2.close()
                handle2 = open("/home/mamane19/chechsum.txt", "w").close()

            elif path1 == path2 and alg1 == alg2 and hashvalue1 != hashvalue2:
                messagebox.showinfo(
                    "Data Integrity",
                    "File " + os.path.basename(fp) + " has been modified or corrupted.",
                )

                # remove entries of that filename
                handle1.close()
                handle1 = open("/home/mamane19/chechsum.txt", "w")
                for line in lines1:
                    if fp not in line:
                        handle1.write(line)
                handle1.close()

                # delete content of 2nd file
                handle2.close()
                handle2 = open("/home/mamane19/chechsum.txt", "w").close()

            else:
                continue


# Close current file
def close():
    # ----------------------------------------------- NON-EMPTY --------------------------------------------------------
    if len(e.get("0.0", END)) > 1:
        # --------------- UNTITLED ------------------
        if root.title() == "Untitled - Akatsuki Text Editor":
            if messagebox.askyesno("Save?", "Do you wish to save?"):

                # first save current file
                root.filename = filedialog.asksaveasfilename(
                    parent=root,
                    title="Save as",
                    filetypes=(("Text file", "*.txt"), ("All files", "*.*")),
                    defaultextension=".txt",
                )

                if root.filename:
                    try:
                        with open(root.filename, "w", encoding="utf8") as w:
                            w.write(e.get(1.0, END))
                    except:
                        messagebox.showerror("Save file", "Could not save that file.")
                        return

                else:
                    messagebox.showerror("Error", "You did not enter a name to save")
                    return

                e.delete(0.0, END)
                root.title("Untitled - Akatsuki Text Editor")

            else:
                e.delete(0.0, END)
                root.title("Untitled - Akatsuki Text Editor")

        # ------------------ TITLED --------------------
        else:
            handle = open(root.filename, "r")
            # ---------- MODIFIED ----------
            if len(e.get("0.0", END)) != (len(handle.read()) + 1):
                handle.close()
                x = root.filename
                if messagebox.askyesno("Save?", "Do you wish to save?"):

                    # first save current file
                    try:
                        with open(x, "w", encoding="utf8") as w:
                            w.write(e.get("1.0", END))
                    except:
                        messagebox.showerror("Save file", "Could not save that file.")
                        return

                    e.delete(0.0, END)
                    root.title("Untitled - Akatsuki Text Editor")

                else:
                    e.delete(0.0, END)
                    root.title("Untitled - Akatsuki Text Editor")

            # --------- NOT MODIFIED ---------
            else:
                handle.close()
                e.delete(0.0, END)
                root.title("Untitled - Akatsuki Text Editor")

    # -------------------------------------------------- IF EMPTY ------------------------------------------------------
    else:
        # -------------------- UNTITLED ----------------------
        if root.title() == "Untitled - Akatsuki Text Editor":
            return

        # --------------------- TITLED -----------------------
        else:
            handle = open(root.filename, "r")
            # ---------- MODIFIED ----------
            if len(e.get("0.0", END)) != (len(handle.read()) + 1):
                handle.close()
                x = root.filename
                if messagebox.askyesno("Save?", "Do you wish to save?"):

                    # first save current file
                    try:
                        with open(x, "w", encoding="utf8") as w:
                            w.write(e.get("1.0", END))
                    except:
                        messagebox.showerror("Save file", "Could not save that file.")
                        return

                    e.delete(0.0, END)
                    root.title("Untitled - Akatsuki Text Editor")

                else:
                    e.delete(0.0, END)
                    root.title("Untitled - Akatsuki Text Editor")

            # --------- NOT MODIFIED ---------
            else:
                handle.close()
                e.delete(0.0, END)
                root.title("Untitled - Akatsuki Text Editor")


# Exit from editor
def __quit(self):
    # ---------------- TITLED ------------------
    if root.title() != "Untitled - Akatsuki Text Editor":
        handle = open(root.filename, "r")
        # ---------- MODIFIED ----------
        if len(e.get("0.0", END)) != (len(handle.read()) + 1):
            handle.close()
            if messagebox.askokcancel(
                "Quit", "Do you want to quit? Any unsaved changes will be lost."
            ):
                root.destroy()
            else:
                return

        # --------- NOT MODIFIED ---------
        else:
            handle.close()
            root.destroy()

    # -------------------- UNTITLED ----------------------
    else:
        # ----------------------------------------------- NON-EMPTY ----------------------------------------------------
        if len(e.get("0.0", END)) > 1:
            # --------------- UNTITLED ------------------
            if root.title() == "Untitled - Akatsuki Text Editor":
                if messagebox.askokcancel(
                    "Quit", "Do you want to quit? Any unsaved changes will be lost."
                ):
                    root.destroy()
                else:
                    return

        # -------------------------------------------------- IF EMPTY --------------------------------------------------
        else:
            # -------------------- UNTITLED ----------------------
            if root.title() == "Untitled - Akatsuki Text Editor":
                root.destroy()


# Copy function
def copy():
    root.clipboard_clear()
    root.clipboard_append(e.selection_get())


# Cut Function
def cut():
    root.clipboard_clear()
    root.clipboard_append(e.selection_get())
    e.delete(SEL_FIRST, SEL_LAST)


# Paste function
def paste():
    e.insert(INSERT, root.clipboard_get())


# Delete some lines
def delete():
    e.delete(index1=SEL_FIRST, index2=SEL_LAST)


# To go to a specific line
def goto(self):
    top = Toplevel()
    top.geometry("200x200")
    top.title("Go To Line")
    Label(top, text="Line number:").pack()
    lineentry = Entry(top)
    lineentry.pack()

    def go_to():

        try:
            e.mark_set("insert", str(lineentry.get()) + ".0")
            text = Text(root)

            pos = e.index(str(float(lineentry.get())) + "lineend")
            print(pos)
            e.tag_add(SEL, str(float(lineentry.get())), pos)
            e.focus_set()
        except TclError:
            messagebox.showerror("Error", "Could not go to line " + lineentry.get())
            top.destroy()

    Button(top, text="Go to", command=go_to).pack(side="left", fill="both", expand=True)
    Button(top, text="Cancel", command=lambda: top.destroy()).pack(
        side="right", fill="both", expand=True
    )


# Select all text
def select_all():
    e.tag_add(SEL, "1.0", END)
    e.focus_set()


# Delete all text
def delete_all(self):
    e.delete("0.0", END)


# Find text
def find(self):
    findstring = simpledialog.askstring("Find...", "Enter text")
    textdata = e.get("0.0", END)
    occurences = textdata.count(findstring)

    t = e
    # ---

    word = findstring

    # word length use as offset to get end position for tag
    offset = "+%dc" % len(word)  # +5c (5 chars)

    # search word from first char (1.0) to the end of text (END)
    pos_start = t.search(word, "1.0", END)

    # check if found the word
    while pos_start:
        # create end position by adding (as string "+5c") number of chars in searched word
        pos_end = pos_start + offset

        print(pos_start, pos_end)  # 1.6 1.6+5c :for first occurance of searched word

        # add tag
        t.tag_add(SEL, pos_start, pos_end)
        t.focus_set()
        # search again from pos_end to the end of text (END)
        pos_start = t.search(word, pos_end, END)

    # ---
    if occurences > 0:
        messagebox.showinfo(
            "Results", findstring + " has " + str(occurences) + " occurences."
        )
    else:
        messagebox.showinfo("Results", "Given string not found.")


# Replace text
def replace(self):
    findstring = simpledialog.askstring("Find...", "Enter text")
    textdata = e.get("0.0", END)
    occurences = textdata.count(findstring)

    t = e

    # create tag style
    t.tag_config("red_tag", foreground="blue", underline=1)

    # ---

    word = findstring

    # word length use as offset to get end position for tag
    offset = "+%dc" % len(word)  # +5c (5 chars)

    # search word from first char (1.0) to the end of text (END)
    pos_start = t.search(word, "1.0", END)

    # check if found the word
    while pos_start:
        # create end position by adding (as string "+5c") number of chars in searched word
        pos_end = pos_start + offset

        print(pos_start, pos_end)  # 1.6 1.6+5c :for first occurance of searched word

        # add tag
        t.tag_add("red_tag", pos_start, pos_end)

        # search again from pos_end to the end of text (END)
        pos_start = t.search(word, pos_end, END)

    # ---
    if occurences > 0:
        messagebox.showinfo(
            "Results", findstring + " has " + str(occurences) + " occurences."
        )

        if (
            messagebox.askyesno(
                title="Replace",
                message="Do you want to replace the word "
                + findstring
                + " with something else?",
            )
            == True
        ):
            replacestring = simpledialog.askstring("Replace...", "Enter text")
            word = findstring

            # word length use as offset to get end position for tag
            offset = "+%dc" % len(word)  # +5c (5 chars)

            # search word from first char (1.0) to the end of text (END)
            pos_start = t.search(word, "1.0", END)

            # check if found the word
            while pos_start:
                # create end position by adding (as string "+5c") number of chars in searched word
                pos_end = pos_start + offset

                print(
                    pos_start, pos_end
                )  # 1.6 1.6+5c :for first occurence of searched word
                t.replace(pos_start, pos_end, replacestring)
                # add tag
                # t.tag_add('red_tag', pos_start, pos_end)

                # search again from pos_end to the end of text (END)
                pos_start = t.search(word, pos_end, END)
    else:
        messagebox.showinfo("Results", "Given string not found.")


# Font size
def set_font_size(size):
    e.config(
        font=(fontdict["family"], size, fontdict["style"])
    )  # other two are defaults
    fontdict["size"] = size


# Font type
def set_font_family(family):
    e.config(
        font=(family, fontdict["size"], fontdict["style"])
    )  # other two are defaults
    fontdict["family"] = family


# Font style
def set_font_style(style):
    e.config(
        font=(fontdict["family"], fontdict["size"], style)
    )  # other two are defaults
    fontdict["style"] = style


# Wordwrap - to move words to the next line
def wordwrap():
    if toggle2.get() is True:
        e.config(wrap=CHAR)
    elif toggle2.get() is False:
        e.config(wrap=NONE)


# Fullscreen on and off
def toggle_fullscreen(self):
    toggle1.set(not toggle1.get())
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))


# Help function
def help():
    messagebox.showinfo(
        "Features available",
        "1. Saving, Opening text files\n2. Get checksum for file\n3. Goto line number"
        "\n4. Find and replace\n5. Change font styling\n6. Change font family"
        "\n7. Change font size\n8. Change background/text colour\n"
        "9. Display Status Bar(Character,Word,Line count)\n10. System time/date",
    )


# About function
def about():
    messagebox.showinfo(
        "About",
        "Akatsuki Editor\nA Python Text Editor!!\nBetter Clone of Notepad\nVersion 5.0\nDeveloped by the Akatsuki team\nCopyright© 2021. All rights reserved.",
    )


# Shortcuts again
root.bind("<Control_L><s>", save)
root.bind("<Control_L><o>", openfile)
root.bind("<Control_L><n>", new)
root.bind("<Control_L><g>", goto)
root.bind("<F11>", toggle_fullscreen)
root.bind("<Control_L><q>", lambda self: __quit(1))


# FILE MENU
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=lambda: new(1), accelerator="Ctrl+N")
filemenu.add_command(label="Open", command=lambda: openfile(1), accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=lambda: save(1), accelerator="Ctrl+S")
filemenu.add_command(label="Save As", command=saveas)
checksum_menu = Menu(filemenu, tearoff=0)
filemenu.add_cascade(label="Checksum", menu=checksum_menu)
checksum_menu.add_command(
    label="Simple Hash", command=lambda: checksum("simple hash", data=(e.get(1.0, END)))
)
cryptographichash_menu = Menu(checksum_menu, tearoff=0)
checksum_menu.add_cascade(label="Cryptographic Hash", menu=cryptographichash_menu)
cryptographichash_menu.add_command(
    label="MD5", command=lambda: checksum("md5", data=(e.get(1.0, END)).encode("utf-8"))
)
cryptographichash_menu.add_command(
    label="SHA1",
    command=lambda: checksum("sha1", data=(e.get(1.0, END)).encode("utf-8")),
)
cryptographichash_menu.add_command(
    label="SHA224",
    command=lambda: checksum("sha224", data=(e.get(1.0, END)).encode("utf-8")),
)
cryptographichash_menu.add_command(
    label="SHA256",
    command=lambda: checksum("sha256", data=(e.get(1.0, END)).encode("utf-8")),
)
cryptographichash_menu.add_command(
    label="SHA384",
    command=lambda: checksum("sha384", data=(e.get(1.0, END)).encode("utf-8")),
)
cryptographichash_menu.add_command(
    label="SHA512",
    command=lambda: checksum("sha512", data=(e.get(1.0, END)).encode("utf-8")),
)
filemenu.add_separator()
filemenu.add_command(label="Close File", command=close)
filemenu.add_command(label="Exit", command=lambda: __quit(1), accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=filemenu)


# EDIT MENU
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=lambda: e.edit_undo(), accelerator="Ctrl+Z")
editmenu.add_command(label="Redo", command=lambda: e.edit_redo(), accelerator="Ctrl+Y")
editmenu.add_separator()
editmenu.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
editmenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
editmenu.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
editmenu.add_command(label="Delete", command=delete, accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Goto", command=lambda: goto(1), accelerator="Ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select all", command=select_all, accelerator="Ctrl+A")
editmenu.add_command(
    label="Delete all", command=lambda: delete_all(1), accelerator="Ctrl+D"
)
editmenu.add_command(
    label="Insert time",
    command=lambda: e.insert(INSERT, time.ctime()),
    accelerator="F5",
)
editmenu.add_command(
    label="Insert colour",
    command=lambda: e.insert(INSERT, colorchooser.askcolor()),
    accelerator="F4",
)
menubar.add_cascade(label="Edit", menu=editmenu)


# FIND MENU
findmenu = Menu(menubar, tearoff=0)
findmenu.add_command(label="Find", command=lambda: find(1), accelerator="Ctrl+F")
findmenu.add_command(label="Replace", command=lambda: replace(1), accelerator="Ctrl+H")
menubar.add_cascade(label="Find", menu=findmenu)


# FONT MENU
fontmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Font", menu=fontmenu)
sizemenu = Menu(fontmenu, tearoff=0)
fontmenu.add_cascade(label="Size", menu=sizemenu)
sizemenu.add_command(
    label="Increase size",
    command=lambda: set_font_size(fontdict["size"] + 5),
    accelerator="Ctrl+Shift++",
)
sizemenu.add_command(
    label="Decrease size",
    command=lambda: set_font_size(fontdict["size"] - 5),
    accelerator="Ctrl+Shift+-",
)
sizemenu.add_command(label="5", command=lambda: set_font_size(5))
sizemenu.add_command(label="10", command=lambda: set_font_size(10))
sizemenu.add_command(label="15", command=lambda: set_font_size(15))
sizemenu.add_command(label="20", command=lambda: set_font_size(20))
sizemenu.add_command(label="25", command=lambda: set_font_size(25))
sizemenu.add_command(label="30", command=lambda: set_font_size(30))
sizemenu.add_command(label="35", command=lambda: set_font_size(35))
sizemenu.add_command(label="40", command=lambda: set_font_size(40))
sizemenu.add_command(label="45", command=lambda: set_font_size(45))
sizemenu.add_command(label="50", command=lambda: set_font_size(50))
sizemenu.add_command(label="60", command=lambda: set_font_size(60))
sizemenu.add_command(label="70", command=lambda: set_font_size(70))
sizemenu.add_command(label="80", command=lambda: set_font_size(80))
sizemenu.add_command(label="90", command=lambda: set_font_size(90))
sizemenu.add_command(label="100", command=lambda: set_font_size(100))

fontfamily = Menu(fontmenu, tearoff=0)
fontmenu.add_cascade(label="Family", menu=fontfamily)
fontfamily.add_command(label="Courier", command=lambda: set_font_family("courier"))
fontfamily.add_command(label="Cousine", command=lambda: set_font_family("cousine"))
fontfamily.add_command(label="Ariel", command=lambda: set_font_family("ariel"))
fontfamily.add_command(label="Helvetica", command=lambda: set_font_family("helvetica"))
fontfamily.add_command(label="Times", command=lambda: set_font_family("times"))
fontfamily.add_command(label="DejaVu", command=lambda: set_font_family("dejavu"))
fontfamily.add_command(label="Freemono", command=lambda: set_font_family("freemono"))
fontfamily.add_command(label="Freesans", command=lambda: set_font_family("freesans"))
fontfamily.add_command(label="Freeserif", command=lambda: set_font_family("freeserif"))
fontfamily.add_command(label="Garuda", command=lambda: set_font_family("garuda"))
fontfamily.add_command(label="Kinnari", command=lambda: set_font_family("kinnari"))
fontfamily.add_command(label="Laksaman", command=lambda: set_font_family("laksaman"))
fontfamily.add_command(label="Loma", command=lambda: set_font_family("loma"))
fontfamily.add_command(label="Monospace", command=lambda: set_font_family("monospace"))
fontfamily.add_command(label="Norasi", command=lambda: set_font_family("norasi"))
fontfamily.add_command(label="System", command=lambda: set_font_family("system"))

fontstyle = Menu(fontmenu, tearoff=0)
fontmenu.add_cascade(label="Style", menu=fontstyle)
fontstyle.add_command(label="Normal", command=lambda: set_font_style("normal"))
fontstyle.add_command(label="Bold", command=lambda: set_font_style("bold"))
fontstyle.add_command(label="Italic", command=lambda: set_font_style("italic"))
fontstyle.add_command(
    label="Bold Italic", command=lambda: set_font_style("bold italic")
)
fontstyle.add_command(label="Roman", command=lambda: set_font_style("roman"))
fontstyle.add_command(label="Underline", command=lambda: set_font_style("underline"))
fontstyle.add_command(label="Overstrike", command=lambda: set_font_style("overstrike"))


# VIEW MENU
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
text_colour_menu = Menu(viewmenu, tearoff=0)
viewmenu.add_cascade(label="Text colour", menu=text_colour_menu)
text_colour_menu.add_command(label="Black", command=lambda: e.config(fg="black"))
text_colour_menu.add_command(label="White", command=lambda: e.config(fg="white"))
text_colour_menu.add_command(label="Blue", command=lambda: e.config(fg="blue"))
text_colour_menu.add_command(label="Green", command=lambda: e.config(fg="green"))
text_colour_menu.add_command(label="Red", command=lambda: e.config(fg="red"))
bgcolourmenu = Menu(viewmenu, tearoff=0)
viewmenu.add_cascade(label="Background colour", menu=bgcolourmenu)
bgcolourmenu.add_command(label="Black", command=lambda: e.config(bg="black"))
bgcolourmenu.add_command(label="White", command=lambda: e.config(bg="white"))
bgcolourmenu.add_command(label="Blue", command=lambda: e.config(bg="blue"))
bgcolourmenu.add_command(label="Green", command=lambda: e.config(bg="green"))
bgcolourmenu.add_command(label="Red", command=lambda: e.config(bg="red"))
viewmenu.add_separator()
viewmenu.add_command(label="Minimise", command=lambda: root.iconify())
viewmenu.add_command(label="Maximise", command=lambda: root.state("zoomed"))
toggle2 = BooleanVar()
toggle2.set(True)
viewmenu.add_checkbutton(label="Word Wrap", command=wordwrap, variable=toggle2)
toggle1 = BooleanVar()
viewmenu.add_checkbutton(
    label="Fullscreen",
    command=lambda: root.attributes("-fullscreen", not root.attributes("-fullscreen")),
    variable=toggle1,
)


# HELP MENU
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_cascade(label="How to Use", command=help)


# ABOUT MENU
menubar.add_cascade(label="About", command=about)


# TO HOLD OUTPUT WINDOW
root.config(menu=menubar)
root.after(500, wordcount)
root.mainloop()
