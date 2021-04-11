<h1 align="center">Final Project - DSA</h1>
<h2 align="center"> Let's be Algo Experts </h2>
<p align="center">
	<img src="assets/images/ken.gif" width="200" height="auto" alt="Ken">
	<img src="assets/images/kaneki.gif" width="200" height="auto" alt="Kaneki">
</p>

# TextEditor
In this project, we will be building a Text Editor. We will be using Tkinter to have a GUI (Graphical User Interface) where users can open, view, edit, write, and save files in their OS. Our text editor will be able to perform Data Integrity checks on files via Cryptographic Checksum. Text editors deal with manipulating text and provide features to enhance the experience. As mentioned before, text editors’ significant functionalities are: inserting, deleting, and viewing the text. That being said, we will add some features such as copy/paste, undo/redo. We will also add some shortcuts like find and replace, ctrl+x, and ctrl+y, etc.

We will be perusing through some of the concepts that we have learned so far in DSA class and other courses to make this text editor as much as precise and relaxed as we can. But our main focus is to apply data structures. We have said Text Editor so many times, but what is really a text editor, and why have we decided to make one ?

Well while you are reading this, you are definitely reading a text that we have written using a text editor :) No doubt this helps get it, but let's talk about Google Docs, Word or even libre office if you are a Mars alien. Those are used to help us create files, write into those files and save them somewhere or even print them. Yeah we've got that, but what is hidden behind a text editor. Some programmers hard work is hiden there :) But most importantly a lot of logic and algorithms. Yeah sounds different now. Someone sit down, thought of all the features that you are able to inform in a text editor and thought of how to structure the data that will be used using the power of algorithms. But it did not end there, they also bring those thoughts into life, which takes us to a text editor. VERY INTERESTING RIGHT 😉️. Alright now that you've understood what we are doing let's walk you through our motivation for this and perhaps motivate you to be an algo expert as well 🤓️.

# Motivation
We use text editors on a daily basis in our lives. from word, google docs, programmers text editor to Mars people ones (I am sure they have ones as well 😄️). The point is that it is in our daily usage, but we just use them right, we do not even know how they are made nor what are they compose of beside the features that we see. Probably you have once said God bless the guy who created undo/redo haha. Well we also love him, and love using text editors s we are doing right now. That's why we wanted to understand how they really work behind the scenes, and how are they made. Yeah you might thing of this as a curiosity, yes it is true but far mmore than that it's a driven passion of technology that brought us here. We have studied various datastructures, and even saw how the undo and redo works, yeah from there we wanted to explore more how text editors work and how we can use DSA concepts to make our own.

Another motivation is that we believe in learning by building, and team work. The more you learn and you are able to picture your learnings into real life cases, the more you will understand what's really going on. When it comes to team work, it is also a learning purpose. Someone can understand something quicker than you will, and it will save you time when they will walk you through their understanding and save you time(vice versa). It is a learning from each other and growing together. 
I hope by now we've convinced you to also be an algo expert as we are aspiring to be 😅️ 😅️. 
Be an algo expert wherever you find yourself, not only in tech fields !!


## Notes
*This is for learning purposes. There are definitely many aspects that we will not consider as in it would be when developing a real text editor like vs code, or docs. So yeah do not be surprised if there are some missing things. But we made sure that it is a fully functional text editor where you can write, edit, save and reopen your txt files. We will probably think of a way to adding more features in the future but for now only .txt files :)*

# DSA Concepts and purposes of usage
- <h3>One Stack</h3> used for undo-redo purposes. Since the stack is LIFO (Last in First out) order, which is equivalent to the undo-redo feature, i.e., the last re-do is undo first.
- <h3>Two Stacks</h3> - The idea behind this data structure is to mimic editing lines rather than a vast document. The two stacks are used to represent the contents where the cursor is. One stack will represent all the contents left of the cursor, while the other stack will represent all the contents right of the cursor.
- <h3>Queues</h3> For copying and pasting texts, Queues are used where you can enqueue or dequeue from the same end. You are just changing the name of push and pop operations of a stack and telling it to Dequeue(for paste command) and Enqueue(for copy command). With every request for a copy and paste, a system call is made along with Enqueue and Dequeue’s individual needs.
- <h3>Hashing</h3> To help us keep track of the words and display the number of words while the user is typing.
- <h3>Checksum/Hashes Algo</h3> To help get the integrity of the data that is being saved.




# Usage 
The project is open to any contribution, but [read the CONTRIBUTING.md](./CONTRIBUTING.md) file before making PRs.





# Citations
- [How do text editors work](http://www.text-editor.org/) 
- [DSA used in text editors](https://iq.opengenus.org/data-structures-used-in-text-editor/)
- add 
- add
- add




### Akatsuki Members
  - Berenda Gilisho
  - Abideen Hamisu
  - Catherine Muthoni
  - Bello Moussa Amadou

<p>Thank you!! have our loves all the way from Mars :)</p>