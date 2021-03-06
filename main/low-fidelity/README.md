<h1 align="center">Text Editor Using Python</h1>
<p align="center">
	<img src="./../../assets/images/ken.gif" width="200" height="auto" alt="Ken">
	<img src="./../../assets/images/kaneki.gif" width="200" height="auto" alt="Kaneki">
</p>


<h2 align="center"> Let's be Algo Experts </h2>

<p align="center">This prototype we programmed is a simple Text Editor. It uses Tkinter packages to have a small GUI (Graphical User Interface) to write, edit, and save files (.txt). We also implemented a redo and undo feature in our prototype to cover the one stack data structure concept,since the stack is LIFO (Last in First out) order, which is equivalent to the undo-redo feature. However in our prototype we can save as our file as a .py or other type of files but, we can not edit them in the text editor as python files or other type of files. Once we save the file we will see in our IDE that it is actually a python but by default it is a .txt file.For now let's just have .txt files.
For now the prototype GUI Demo looks like this you can find the demo below. In the future we will implement new features in our text editor and cover more data strucuture concept to show our understanding and our text editor will look a lot more like ones:)
</p>

## Demo(Prototype low-fidelity).
<img src="./../../assets/images/demo.gif" alt="Demo">

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
</br>
---

We recommend you to use a virtual environment to install those packages for you to not get your computer overwhelmed in terms of space. you can visit this [website](https://docs.python.org/3/library/venv.html) if you would like to do so. Note that it would not be a problem to run the program if you did not use a virtual environment.



To execute the program, run the entry-point file using the command inside the project directory:

```bash
$cd main 
$python textEditor.py
```
If you have multiple versions of python in your system, use the command bellow:
```bash
$python3 textEditor.py
```
# Future Updates
<p>Below are data structure and algorithms we will be adding to the text editor; </p>

- <h3>Two Stacks</h3> The idea behind this data structure is to mimic editing lines rather than a vast document. The two stacks are used to represent the contents where the cursor is. One stack will represent all the contents left of the cursor, while the other stack will represent all the contents right of the cursor.
- <h3>Queues</h3> For copying and pasting texts, Queues are used where you can enqueue or dequeue from the same end. You are just changing the name of push and pop operations of a stack and telling it to Dequeue(for paste command) and Enqueue(for copy command). With every request for a copy and paste, a system call is made along with Enqueue and Dequeue’s individual needs.
- <h3>Hashing</h3> To help us keep track of the words and display the number of words while the user is typing.
- <h3>Checksum/Hashes Algo</h3> To help get the integrity of the data that is being saved.

# Usage 
The project is open to any contribution, but [read the CONTRIBUTING.md](./CONTRIBUTING.md) file before making PRs.

# Citations
- [How do text editors work](http://www.text-editor.org/) 
- [DSA used in text editors](https://iq.opengenus.org/data-structures-used-in-text-editor/)

### Akatsuki Members
  - Brenda Gilisho
  - Abideen Hamisu
  - Catherine Muthoni
  - Bello Moussa Amadou

<p>Thank you!! Have our loves all the way from Mars :)</p>


