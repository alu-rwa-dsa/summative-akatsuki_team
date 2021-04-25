<h1 align="center">Text Editor Using Python</h1>
<p align="center">
	<img src="assets/images/ken.gif" width="200" height="auto" alt="Ken">
	<img src="assets/images/kaneki.gif" width="200" height="auto" alt="Kaneki">
</p>

<h2 align="center"> Let's be Algo Experts </h2>

<p align="center">This prototype we programmed is a simple Text Editor. It uses Tkinter packages to have a small GUI (Graphical User Interface) to write, edit, and save files (.txt). We also implemented a redo and undo feature in our prototype to cover the one stack data structure concept,since the stack is LIFO (Last in First out) order, which is equivalent to the undo-redo feature. However in our prototype we can save as our file as a .py or other type of files but, we can not edit them in the text editor as python files or other type of files. Once we save the file we will see in our IDE that it is actually a python but by default it is a .txt file.For now let's just have .txt files.
For now the prototype GUI Demo looks like this you can find the demo below. In the future we will implement new features in our text editor and cover more data strucuture concept to show our understanding and our text editor will look a lot more like ones:)
</p>

## Demo(Prototype High-Fidelity).

<img src="assets/images/Peek%202021-04-21%2021-36.gif" alt="Demo">

## Technology used.

Python tkinter.

---

## Project File Structure.

The program is structured using the [module architecture](https://www.tutorialspoint.com/python/python_modules.htm#:~:text=A%20module%20allows%20you%20to,file%20consisting%20of%20Python%20code) to make the code readabiliy very easy.

<p>
<strong>Assets</strong>: Contains any Images that will be used in the course of the project
</p>
<p>
<strong>Main</strong>: Contains the python file containing the software implementation
</p>
<p>
<strong>Saved Files</strong>: This is where the files created after testing of the software will be saved. When testing the software, please save your file to this folder.
</p>

## How to setup/Run.

### Third party libraries:

- [tkinter](https://pypi.org/project/tkintertable/)

```bash
$pip install tkintertable
```

## </br>

We recommend you to use a virtual environment to install those packages for you to not get your computer overwhelmed in terms of space. you can visit this [website](https://docs.python.org/3/library/venv.html) if you would like to do so. Note that it would not be a problem to run the program if you did not use a virtual environment.

To execute the program, run the entry-point file using the command inside the project directory:

```bash
$cd main/high-fidelity
$python textEditor.py
```

If you have multiple versions of python in your system, use the command bellow:

```bash
$python3 textEditor.py
```

# Implemented features

<p>Below are data structure and algorithms we have added and some other features to make it beautiful </p>

- [x] Shotcuts like ctrl+x or ctrl+y, and many more you can find them in the menu bar
- [x] Checksum to make the data integrity checking easy
- [x] Copy/paste available through shortcuts or the menu bar
- [x] Words, lines and character countings available at the bottom while writing. Using hashmaps to keep track :)
- [x] Finding and replacing feature/algo available as well.
- [x] Changing the view using other fonts and sizes...
- [x] Fullscren, maximize, minimize all available in our text editor
- [x] You can play with graphics however you want (resizing, the design...)
- [ ] Help and about menu available but not functional (bear with us for future updates:) )

# Correctness of Algorithm
<strong>Test Cases</strong>

1.Testing Word count
<p>Test_data: "My name is Catherine."</p>
<p>AssertEquals("My name is Catherine.", 4)</p>
<p>Expected: True</p>

2.Testing open file
<p>File name: "trial.txt"</p>
<p>File content: "Hey there, what's io?"</p>
<p>AssertEquals("trial.txt".read(), "Hey there, what's io?")</p>
<p>Expected: True</p>

3.Testing open file without putting name
<p>File name: "trial.txt"</p>
<p>File content: "Hey there, what's io?"</p>
<p>AssertRaises(AssertionError,"trial.txt".read(), "Hey there, what's io?")</p>
<p>Expected: Throws Error</p>

# Usage

The project is open to any contribution, but read the [CONTRIBUTING.md](./CONTRIBUTING.md) file before making PRs.

# Citations

- [How do text editors work](http://www.text-editor.org/)
- [DSA used in text editors](https://iq.opengenus.org/data-structures-used-in-text-editor/)

### Akatsuki Members

- Brenda Gilisho
- Abideen Hamisu
- Catherine Muthoni
- Bello Moussa Amadou

<p>Thank you!! Have our loves all the way from Mars :)</p>
