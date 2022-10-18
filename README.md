# cs201

Each branch is a seperate lab that was required for cS201 - Programming Structures

**Lab Portion - 50% of exam (54pts + 4pts Bonus)
You can lose points if you don't follow these requirements:**

**All files:**

Must use only the the Line Feed character for line endings.
Must include the Hashbang.
Must have the executable bits set for all chmod entities.
Modules/Scripts (not necessary for ```.lab_tests.py``` files)

Must support the help arguments ```--help/-h``` with a relevant help message then exiting.
Must support the version arguments ```--version/-v ```with a version number then exiting.
Must have tests using ```if __name__ == "__main__":```.


**Lab Setup**
Turn in all the files by creating the following directory and placing them in that location on the CS Server.
```
mkdir -p ~/labs/midterm
```
_____________________________________________________________________________

#**1) Text Inside Parentheses (```parens.py``` and ```parens.lab_tests.py```)
For this lab we will be searching for and returning any text inside of the first set of parentheses found ```()```.**

Example Search String: ```"Hello, I'm Robert (Bob)."```

Example Result: ```"Bob"```

You do not need to code for nested parentheses, multiple parenthetical groups, or newlines in the parentheses. You may use the built-in string methods ```.find()``` or ```.index()``` in order to make this a bit easier. Feel free to look up the documentation on those string methods.

This should be an easy task. The difficulty will be in creating this functionality in a reusable module, and then also in how we get the initial search string data from the user. There will be 4 ways to get a search string:

Look for ```-f``` or ```--file``` in the arguments, and the following argument should be a file path. Open the file and read the data in, using that as the search string.
Join all of the **program arguments** (```sys.argv```) together with a space character, and use the resultant string data as the search string (```" ".join(args)```)
Use Standard Input in TTY mode (```sys.stdin.isatty()```).
Use Standard Input in PIPE mode (```not sys.stdin.isatty()```).


##**Module ```parens.py```**

Create a python module called ```parens.py```. In this file define a function ```in_parens()``` that takes a string as an argument. In this function you must search the provided string parameter for the first parentheses grouping you can find, returning the text between the parentheses as a result of the function. **Only return the text between parentheses, not the parentheses themselves.** If no matching parentheses pair can be found in the string, then ```return None```. If an empty pair is found (), then return the empty string "". Place all your own tests under ```if __name__ == "__main__":```.


##**Function Logic** ```in_parens(string)```

This function should accept a parameter of type string string. This parameter with hold the string in which we will search for the test between 2 parentheses.

First you must locate the open parenthesis (```(```). You may use the built-in string methods ```.index()``` or ```.find()``` if you like, or you can just search one character at a time using a loop looking for an opening parenthesis (```(```).

Next you must find a closing parenthesis (```)```) that necessarily occurs **after** the opening parenthesis. So you must start searching for this closing parenthesis **after** the location where the opening parenthesis was found. Again, you may use ```.index()```, ```.find()```, or manually search with a loop.

Finally, once you have the locations of the opening and closing parentheses, you must extract the text characters between them. Remember, you should not include the parentheses themselves in the output.

If no **valid** parenthesis pair is found, the function should return ```None```. Some examples of these would be a string with no parentheses (e.g. ```"Hi"```) or a string where the closing parenthesis comes first (e.g. ```"Look ) at ( this"```). Both of those should return ```None```.
_____________________________________________________________________________

##**Lab Testing the Module** ```parens.lab_tests.py```

Create a file called ```parens.lab_tests.py``` and copy and paste this code into the file. This will test the ```in_parens()``` function from your ```parens.py``` module.
```
#!/usr/bin/env python3

from parens import in_parens

all_passed = True

test = "(test1)"
if in_parens(test) != "test1":
    print("Test 1 failed.")
    all_passed = False

test = "next (test2)"
if in_parens(test) != "test2":
    print("Test 2 failed.")
    all_passed = False

test = "(test3) prev"
if in_parens(test) != "test3":
    print("Test 3 failed.")
    all_passed = False

test = "--(test4)--"
if in_parens(test) != "test4":
    print("Test 4 failed.")
    all_passed = False

test = "()"
if in_parens(test) != "":
    print("Test 5 failed.")
    all_passed = False

test = "--()"
if in_parens(test) != "":
    print("Test 6 failed.")
    all_passed = False

test = "Hi"
if in_parens(test) != None:
    print("Test 7 failed.")
    all_passed = False

test = ""
if in_parens(test) != None:
    print("Test 8 failed.")
    all_passed = False

test = "Look ) at ( this"
if in_parens(test) != None:
    print("Test 9 failed.")
    all_passed = False

test = "Look ) at (this) now"
if in_parens(test) != "this":
    print("Test 10 failed.")
    all_passed = False

if all_passed:
    print("All tests PASSED!")

```


####**Grading (20pts)**

 **(5pts)** - Module parens.py exists with a function in_parens defined in the global scope.
 **(5pts)** - Module parens.py makes use of if __name__ == "__main__": to run at least 1 module test of your own creation.
 **(10pts)** - Program parens.lab_tests.py passes all lab tests for the module parens.py without cheating (must actually search the string for parentheses).


##**Using the Module and Getting Search Data From the User**

For full credit you only need to create one of the two terminal programs ```stdin.py``` or ```arguments.py``` described below. You can create both if you want extra credit. You can also create a third program called ```all.py``` which makes use of all 4 data input methods in one program for the maximum extra credit.


##**No Parenthetical Groups Found**

In the programs ```arguments.py```, ```stdin.py``` or ```all.py```, if no opening parenthesis can be found, or if no closing parenthesis can be found after an opening parenthesis, the program should **print an error message to standard error (stderr) and exit with an error status code of ```1```.**

```
# If no parenthetical grouping is found (meaning in_parens() returned None)
# then display an error message to standard error, and exit with status code 1

    print ("Error: no parenthetical grouping found.", file=sys.stderr
    exit(1)
```
_____________________________________________________________________________

#**2) Standard Input (```stdin.py```)**

This program will support the 2 data input methods that relate to **standard input (stdin) data**.

If in TTY mode (```sys.stdin.isatty()```), collect string data from stdin in TTY mode (```input()```).
If in PIPE mode (```not sys.stdin.isatty()```), collect string data from stdin in PIPE mode (```sys.stdin.read()``` or ```for line in sys.stdin:```).

Program Setup Example
```
#!/usr/bin/env python3

import sys
import parens

def tty_mode():
    pass
def pipe_mode():
    pass
    
if __name__ == "__main__":
    #argument processing
    if sys.stdin.isatty():
        tty_mode()
    else:
        pipe_mode()
````

####**Grading (34pts or BONUS 2pts)**

 **(2pts)** - Program has ```--version```/```-v``` argument functionality.
 **(2pts)** - Program has ```--help```/```-h``` argument functionality.
 **(12pts)** - Program ```stdin.py``` collects user input from Standard Input. There must be a TTY mode and a PIPE mode (```if sys.stdin.isatty():```).
 **(12pts)** - Program will **ONLY** output the text from the search string found between the first found open parenthesis and the first found closed parentheses **following the open parenthesis** of the search string. **No other output.**
 **(3pts)** - Program will output a message to stderr and exit with an error status code of 1 if there is no opening parenthesis (.
 **(3pts)** - Program will output a message to **stderr** and exit with an error status code of ```1``` if there is no closing parenthesis ```)``` after the first found open parenthesis ```(```.
_____________________________________________________________________________

#**3) Arguments (arguments.py)**

This program will support the 2 data input methods that relate to **program argument** data.

If an argument option ```-f``` or ```--file``` is given, followed by an argument that is a path to a file, your program should open that file and read in the search string.
If ```-f``` or ```--file``` is not one of the arguments, but arguments are provided (```len(args) > 0```), the argument data itself should be considered the search string by joining all of the arguments together with a space character (```" ".join(args)```).

Program Setup Example:
```
#!/usr/bin/env

import sys
import parens

def file_mode():
    pass
    
def arg_mode():
    pass
    
if __name__ == "__main__":
    #argument processing
    if "-f" in args or "--file" in args:
        file_mode()
    else:
        arg_mode()
```

####**Grading (34pts or BONUS 2pts)**

 **(2pts)** - Program has ```--version```/```-v``` argument functionality.
 **(2pts)** - Program has ```--help```/```-h``` argument functionality.
 **(12pts)** - Program ```arguments.py``` collects user input using a file found from the argument option ```-f``` or ```--file```, and if those are not found, the an argument mode is used in which all the arguments are joined together with a space character.
 **(12pts)** - Program will ONLY output the text from the search string found between the first found open parenthesis and the first found closed parentheses following the open parenthesis of the search string. No other output.
 **(3pts)** - Program will output a message to stderr and exit with an error status code of ```1``` if there is no opening parenthesis ```(```.
 **(3pts)** - Program will output a message to stderr and exit with an error status code of ```1``` if there is no closing parenthesis ```)``` after the first found open parenthesis ```(```.
_____________________________________________________________________________

#**4) All Modes of Operation (all.py)**
This program is optional and only for bonus points. The idea is that all of the modes of operation used in both stdin.py and arguments.py will work in one program called all.py,

A potential setup for all.py.
```
#!/usr/bin/env python3

import sys
import stdin
import arguments

if __name__ == "__main__":
    #argument processing
    if len(args) == 0:
        if sys.stdin.isatty():
            stdin.tty_mode()
        else:
            stdin.pipe_mode()
    else:
        if "-f" in args or "--file" in args:
            arguments.file_mode()
        else:
            arguments.arg_mode()
```

####**BONUS Grading (4pts)**
 **(BONUS 2pts)** - You can complete both arguments.py and stdin.py.
 **(BONUS 2pts)** - You complete all.py and all the input methods work.
 _____________________________________________________________________________

#**Program Execution Examples**

##**File path provided as argument**
File ```text.txt```
```
Hi, I'm Robert (Bob).
Nice to meet you
```
Command (should work with ```all.py``` or ```arguments.py```)
```
./arguments.py --file text.txt
```
Expected output (stdout with exit status code 0)
```
Bob
```
_____________________________________________________________________________

##**File path provided as Argument - no parentheses found**

File ```text.txt```
```
Hello
```
Command (should work with ```all.py``` or ```arguments.py```)
```
./arguments.py --file text.txt
```
Expected output (stderr with exit status code 1)
```
Error: no parenthetical grouping found.
```
_____________________________________________________________________________

##**Search String as Argument**

Command (should work with ```all.py``` or ```arguments.py```)
```
./arguments.py Hi, I\'m Robert \(Bob\).
```
Expected output (stdout with exit status code 0)
```
Bob
```
_____________________________________________________________________________

##**Standard Input as TTY**

Commmand (should work with ```all.py``` or ```stdin.py```)
```
./stdin.py
```
Program Request for User Input, Followed by User input
```
Enter some text with something enclosed in parentheses: Hi, I'm Robert (Bob).
```
Expected output (stdout with exit status code 0)
```
Bob
```
_____________________________________________________________________________

##**Standard Input as PIPE**

Command (should work with ```all.py``` or ```stdin.py```
```
echo "Hi, I'm Robert (Bob)." | ./stdin.py
```
