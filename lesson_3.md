# Review Document: Python Variables and Shell Commands

This document will help you review what we've learned about Python variables
and shell commands. Let's dive in!

## 1. Python Variables

In Python, a variable is like a container that stores information. You can give
it a name and use it to store numbers, words, or other data.

### How to Create a Variable
To create a variable, you need:

- A name for the variable (e.g., num_apple, score).

- The value you want to store (e.g., 10, 95.5).

Example:

```python
apple = 10
banana = 5
```

### Rules for Variable Names
- Variable names can only contain letters, numbers, and underscores (_).
- The have to be meaningful.

Example of good variable names:

```python
num_apple = 10
```

### Using variables

You can use variables in your code to perform calculations or print messages.

Example:

```python
num_apple = 5
num_banana = 10
total = num_apple + num_banana
print(total)
```

## 2. Shell Commands
The shell is a program that lets you talk to your computer using text commands.
Here are the commands we learned:

1. pwd (Print Working Directory) This command tells you where you are in the
   computer's file system.

```bash
$ pwd
/home/username
```

2. cd (Change Directory)
This command lets you move to a different folder.

```bash
$ cd learn_python
```

3. mkdir (Make Directory)
This command creates a new folder.

```bash
$ mkdir new_folder
```

4. ls (List)
This command shows you all the files and folders in your current directory.

```bash
$ ls
```
5. python3
This command runs Python code or starts the Python interpreter.

```bash
$ python3 variables.py
```

6. nvim (Neovim)
This is a text editor you can use to write and edit code.

```bash
$ nvim variables.py
```

To save and exit, press ESC, then type :wq and press Enter.
