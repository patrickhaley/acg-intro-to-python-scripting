# A Cloud Guru: Introduction to Python Scripting

## Course Overview

This course provides an introduction to Python scripting. Learn the basics of Python programming and how to use it for scripting tasks.

**Course Link:** [Introduction to Python Scripting](https://learn.acloud.guru/course/introduction-to-python-scripting/overview)

## Lab: Drawing an ASCII Shape with Python

**Lab Link:** [Drawing an ASCII Shape with Python](https://learn.acloud.guru/course/introduction-to-python-scripting/learn/11033651-0032-4f0f-bfd2-1222f68562b3/a9077638-d662-4f89-bac4-1a5a1539e19a/lab/a9077638-d662-4f89-bac4-1a5a1539e19a)

### Task 1: Create an Executable File with the Python Interpreter Path Instruction

1. Create a file called `asciiShape.py`:
   ```
   touch asciiShape.py
   ```
2. Make it executable:
   ```
   chmod +x asciiShape.py
   ```
3. Insert the instruction for the Python interpreter path at the beginning of the file:
   ```
   vim asciiShape.py
   ```

### Task 2: Write Two "for" Loops to Draw a Pyramid

```
    length = 10
    astr = "*"
        for i in range(length):
            for j in range(length-i):
                print(" ", end='')
            print(astr)
            astr += "**"
```

### Task 3: Write a Loop to Draw an Upside-Down Pyramid

```
length -= 1
space = 1
astrNum = ((length*2)-1)
astr = "*" * astrNum
for i in range(length):
    print(" " + space * " " + astr)
    astrNum -= 2
    astr = "*" * astrNum
    space += 1
```

### Task 4: Test the File

1. Save and exit the file:
   1. Press Escape
   2. Type `:wq`
   3. Press Enter
2. Execute the file:

```
python asciiShape.py
```

## Lab: Writing Four Functions to Perform Different Arithmetic Operations in Python

**Lab Link:** [Writing Four Functions to Perform Different Arithmetic Operations in Python](https://learn.acloud.guru/course/introduction-to-python-scripting/learn/c304156a-81fb-486e-90ad-104de350947e/a9908b71-baa7-4734-8fa1-0a833d48c674/lab/a9908b71-baa7-4734-8fa1-0a833d48c674)

### Task 1: Create a File and Make It Executable

### Task 2: Write Three Functions That Are Able to Add, Subtract, and Multiply Two Numbers

### Task 2: Write a Function to Divide Two Numbers and Implement a Check for Division by 0

### Task 2: Run Tests and Call All Four Functions
