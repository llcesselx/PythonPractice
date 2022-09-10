# cs201

CS-201 - Programming Structures
Fall 2022
Instructor: Mr. Luke May
Program Communication
Preparation
Make sure you have watched the videos from Scripting Basics.

Requirements of all command-line utility programs going forward (you can lose points if your leave any of these off):

Must include the Hashbang.
Must have the executable bits set for all chmod entities.
Must use only the the Line Feed character for line endings.
Must support the version arguments --version/-v with a version number then exiting.
Must support the help arguments --help/-h with a relevant help message then exiting.
Lab Setup
Turn in all the files by creating the following directory and placing them in that location on the CS Server.

mkdir -p ~/labs/lab2
Auto Grader
There is an auto-grader for this lab that should give you a reasonable idea of your grade. This program will help to ensure that you have named your files correctly and that your programs work reasonably well. Again, the result here does not guarantee your final lab grade, but is should give a reasonable estimate of your grade.

Navigate to your lab folder:

cd ~/labs/lab2
Then run the grader:

cs201-lab2-grader.py
Lab Problems (63pts)
1) Permissions And Boolean Logic (perms.py)
Read the article on Linux Permissions if you have not yet done so.

Create a Python 3 program file named perms.py. In addition to the standard version and help argument options, this program should accept 3 additional argument options representing the 3 permission types: read, write, and execute. Then, based on the presence of those argument options when the command is executed, it should output the octal number associated with those permissions. All eight possibilities should be addressed. If an option is not provided as an argument, it is assumed that the associated permission bit is a 0. Here are the argument options you should support:

-v or --version, display the version number of program, then exit(0). It is your choice on how to user version numbers, but something as simple as a date YYYY-MM-DD would suffice.
-h or --help, display help on how to use the command, then exit(0).
-r or --read, indicates the read permissions would be set to a 1.
-w or --write, indicates the write permissions would be set to a 1.
-x or --execute, indicates the execute permissions would be set to a 1.
Hint: Make a large if/elif/else statement, and make one if or elif for each octal number. To prevent the boolean expressions from being too long you might create variables for each permissions. Here is how you might start:

The above is a very rudimentary solution, but it does indeed work. See if you can think of a better solution. There are many different ways to solve problems in computer science.

Examples
Command	Output
./perms.py -r -w --execute	7
./perms.py --read -w	6
./perms.py -r	4
Grading (10pts)
(1pts) File perms.py has working -v and --version functionality.
(1pts) File perms.py has working -h and --help functionality.
(8pts) File perms.py exists and shows the completion of each step outlined above. Every possible permutation of command options given as arguments (with either the long or short version) displays the appropriate octal number for that permission set value.
2) Get Labeled Argument Pairs (labeled_pairs.py)
Create a program called labeledParis.py that creates a dictionary of labeled pairs of arguments. You can assume all the named arguments provided to this program will be in pairs, such that the argument with the name will come first and then following argument will be the value associate with that name. In this way we can construct a Python dictionary of argument names and their associated values.

Example:

./labeled_pairs.py -a 5 -b banana -x 123.2 --color orange
Should print a dictionary like this (order may vary):

{
    "a": 5,
    "b": "banana",
    "x": 123.2,
    "color": "orange",
}
Notice that for the short command options like -a and -b, the hyphen is removed from the key name in the dictionary. Similarly, for the longer style command options that begin with two hyphens, like --color, both hyphens are also removed in the resulting dictionary keys.

Remember, all arguments to a program start as string data. So an important requirement to this program is that if an argument value is provided that can be converted to an int, then that value will be converted to an integer in the resultant dictionary. Similarly, if an argument value is provided that can be converted to a float, then that value will be converted to a floating point decimal in the resultant dictionary. For this you will want to make use of try/except clauses. The only tricky part is deciding which to try first. As a clue, all integers can be converted into floats, but not all floats can be converted into integers. Remember, if it can be converted to an integer, it should show up in the dictionary as an int not a float.

The last intriguing part of this assignment is how to get the dictionary to be printed nicely as shown in the example above. Usually if we just print the dictionary using print like this:

we would get some ugly output like this:

{'a': 5, 'b': 'banana', 'x': 123.2, 'color': 'orange'}
Instead we would like to see the output look prettier, like how it is written in our code, with one key-value pair per line, and 4 space indentation. To do this we can use a built-in python package called json. JSON is an acronym that stand for JavaScript Object Notation. Despite JavaScript being in the name, JSON is not limited to just JavaScript. JSON is a data structuring language that was originally developed for use in JavaScript, and it's syntax is quite close to the Python 3 syntax for lists and dictionaries. The primary difference being that you must use double quotes (") for strings, and there can be no trailing commas after the last element of a list or dictionary.

To achieve a prettier print, we can use the json.dumps() function, which stands for dump string. As an example, try this little program to compare two different outputs for a dictionary:

You could even make a nice function out of it:

So for full credit, make sure you print the resulting argument dictionary using this method.

Full Walkthrough of labeled_pairs.py
If you don't have a location on your computer to store files for this class, create one. I recommend you create a folder cs201 on your Desktop, by right-clicking on the Desktop and selecting New Folder. Once you have the new folder called cs201, open Atom. In the top menu click File then click Add Project Folder then navigate to and select that newly created folder. You should see the folder appear in a tree view on the left-hand side of Atom. Right click on the cs201 folder in that tree view and select New Folder to create a folder inside called lab1.

First create the file labeled_pairs.py. Right click on the lab1 folder and click New File and name the file labeled_pairs.py. Make sure your editor only uses the Line Feed line ending by looking on the bottom indicator tray for a yellow or green dot and the letters LF. If instead you see the letters CRLF you should click on them and change it to LF. Add the hashbang as the first line of the file (#!/usr/bin/env python3). Change the permissions of the file to make it executable by right clicking the file and selecting Change Mode, then setting the octal permissions to 755.

The first thing we need to do is collect arguments, so we will need to import the sys package. We will also want to trim of the first argument from the argument vector argv because we don't need it.

Next we need to handle the version arguments.

Next we need to handle the help text arguments:

Next we need to check to see if we have no arguments, and if so it is an error, so we should issue an error message and exit with error code 1.

Now we get to the meat of the program. We must take every pair of arguments from our arguments list and create a dictionary from them. The first argument is to be the key, and any hyphens should be trimmed off. The second argument is to be the value. The expectation is that you will receive arguments in pairs, but if not, you do not have to handle that case.

Now we have a dictionary with labeled values, however, the values are all strings, because all argument data starts out as string data. So we need to go through the list of argument values and convert them to an integer if possible, and then try to see if the can be converted to a float. It is important we try the integer conversion first because a both an int and a float can be made from the string value "7", but only a float can be made from "8.2". So in the above code where the comment #Insert code is locaded, we will insert some code to do that.

The last thin we want to do is to print the dictionary out in a pretty JSON formatted way. So near the beginning of the program where we have out imports, we need to add the json package, and a simple little function to print collections out nicely.

Then the very last thing is to go back to the bottom of our program and print out our dictionary using this nice helper function:

Move this file to the CS Server using an FTP Client to the directory ~/labs/lab1.

Grading (13pts)
You may lose points for incorrect file or argument naming (letter case matters!), failing to set the permissions, leaving off the hashbang, or wrong line endings.

(2pts) Program labeled_pairs.py displays a dictionary of labeled argument pairs. Barring the help and version arguments, if any arguments are provided they are expected to be in pairs of the form --key value or -k value, such that the label argument comes first, followed by the value argument. You do not need to account for arguments in the wrong format.
(2pts) Program labeled_pairs.py removes hyphens from short and long argument labels (NOT from argument values).
(2pts) Program labeled_pairs.py always converts numeric values that are able to be converted to ints.
(2pts) Program labeled_pairs.py always converts numeric values that can't be converted to ints into floats.
(2pts) Program labeled_pairs.py prints the dictionary nicely using json.dumps with an indentation of 4 spaces.
(1pts) Program labeled_pairs.py displays a version number if -v or --version are provided as arguments, then exits with status code 0.
(1pts) Program labeled_pairs.py displays a help message if -h or --help are provided as arguments, then exits with status code 0.
(1pts) Program labeled_pairs.py, when run with no arguments, displays an error message over stderr, and then exits with status code 1.
3) Get Keyword Arguments (keyword_args.py)
Requirements of all executable programs going forward (you can lose points if your leave any of these off):

Must include the Hashbang.
Must have the executable bits set for all chmod entities.
Must use only the the Line Feed character for line endings.
Must support the version arguments --version/-v with a version number then exiting.
Must support the help arguments --help/-h with a relevant help message then exiting.
Like problem 2, but with keyword arguments. Create a program called keyword_args.py that creates a dictionary of labeled pairs of arguments. You can assume all the named arguments provided to this program will be of the form --argName=someValue or -n=value, Construct a Python dictionary of argument names and their associated values. Hyphens on the names should not be included.

Example:

./keyword_args.py --a=5 --b=banana --x=123.2 --color=orange
Should print a dictionary like this (order may vary):

{
    "a": 5,
    "b": "banana",
    "x": 123.2,
    "color": "orange",
}
Grading (13pts)
You may lose points for incorrect file or argument naming (letter case matters!), failing to set the permissions, leaving off the hashbang, or wrong line endings.

(2pts) (2pts) Program keyword_args.py displays a dictionary of labeled argument pairs. Barring the help and version arguments, if any arguments are provided they are expected to be of the form --key=value or -k=value all as one argument, such that the label comes first, followed an equals sign, then followed by the value argument.
(2pts) Program keyword_args.py removes hyphens from short and long argument labels (NOT from argument values).
(2pts) Program keyword_args.py always converts numeric values that are able to be converted to ints.
(2pts) Program keyword_args.py always converts numeric values that can't be converted to ints into floats.
(2pts) Program keyword_args.py prints the dictionary nicely using json.dumps with an indentation of 4 spaces.
(1pts) Program keyword_args.py displays a version number if -v or --version are provided as arguments, then exits with status code 0.
(1pts) Program keyword_args.py displays a help message if -h or --help are provided as arguments, then exits with status code 0.
(1pts) Program keyword_args.py, when run with no arguments, displays an error message over stderr, and then exits with status code 1.
4) Generate Random Numbers (rand.py)
Create a Python 3 program file named rand.py. Standard version and help argument options should be included in your program. This program will generate a list of random floating point decimals. This program should accept an optional named argument for a maximum value (-M or --max defaulting to 100.0), an optional named argument for a minimum value (-m or --min, defaulting to 0.0), and a required positional argument representing the number of random numbers to generate.

We will need to import the library random into our program. To generate random numbers between a given minimum and maximum floating point decimal value, use random.uniform(min, max). Here is an example starting point for your program:

Examples
All of these would return the same results, they just show different ways of specifying the arguments. Notice the ordering does not matter.

./rand.py -m 65.0 -M 95.0 5
./rand.py --max 95.0 --min 65.0 5
./rand.py --min 65.0 -M 95.0 5
./rand.py --max 95.0 -m 65.0 5
Output may look something like this (it won't be exactly this because of the randomization):

66.33815185823457
93.31050942336518
69.56985457195861
74.54913080038324
91.89096001065893
Grading (10pts)
(1pts) File rand.py has working -v and --version functionality.
(1pts) File rand.py has working -h and --help functionality.
(2pts) File rand.py exists and generates at least one random number if the last argument is a number.
(2pts) File rand.py exists and generates X random numbers based on the last argument (the 5 in the above examples).
(2pts) arguments -m and --min work as described.
(2pts) arguments -M and --max work as described.
5) Average Floats From Standard Input (avg.py)
Create a Python 3 program file named avg.py. Standard version and help argument options should be included in your program. This program should expect floating point decimals from Standard Input (stdin), and it will computer the average from them.

This program must operate in 3 different modes. If arguments are provided, the arguments will be used as input. If no arguments are added, then depending on how the stdin is being received the program will either operate in TTY Mode or PIPE Mode. You can determine which stdin input mode is in use by calling sys.stdin.isatty(), which will return True if the terminal was run from a TTY, and False if run using a PIPE.

IMPORTANT! - This is all describing Linux based terminal communication. While some things are similar in Windows, what is being described here will only work on Linux and MacOS. So if you run Windows as your OS, make sure you test your program on the CS Server, otherwise you will get errors when the program actually works fine.

Argument Mode - We are in this mode if there are any arguments detected (len(sys.argv[1:]) > 0). This mode could be tested by running the program like this:

 ./avg.py 99.8 85.2 92.5
TTY Mode (STDIN) - We are in this mode if there are no arguments, and the stdin is coming from a TTY (TeleTYpewriter), which essentially means a user ran the program from a terminal and is expecting program feedback. This mode could be tested by running the program like this:

 ./avg.py
PIPE Mode (STDIN) - We are in this mode if there are no arguments, and the stdin is coming from a PIPE, which essentially means the program is being fed input from a terminal PIPE or from file input redirection. This mode could be tested by running the program in either of theses ways:

 echo -n "99.8\n85.2\n92.5\n" | ./avg.py
 ./avg.py < floats.txt
Where floats.txt is a file containing floating point decimal numbers, one per line:

 99.8
 85.2
 92.5
If running in TTY mode (sys.stdin.isatty() == True), your program should take floating point decimal data from stdin in a loop, until the user leaves the input blank and presses Enter. Each time the user inputs a value, if it is a valid floating point decimal, you will include it in your final average. If the value cannot be converted to a float, it should be ignored. You should include a message when calling the input() function here, since we know there is a user at a TTY running the program. Once the user leaves an input blank and presses Enter, the data collection portion of the program will be complete, and then you will need to average all of the items collected, and output the average value. The final output from this mode of the program should only be the final averaged result without labels or any other output on stdout.

If running in PIPE mode (sys.stdin.isatty() == False), your program should take floating point decimal data from stdin one line at a time using this for loop:

for line in sys.stdin:
    # remove the newline character from line if it exists
    # etc.
Everything else is the same as the other mode. You will calculate the average and display it only as output. This program mode should NOT make use of the input() function. Remember the only output should be the result, with no labels.

Hint - It may be helpful for you to write each mode as a separate program first, then write one final program that combines the functionality of the other 3.

Grading (17pts)
(1pts) File avg.py has working -v and --version functionality.
(1pts) File avg.py has working -h and --help functionality.
(4pts) File avg.py exists and works as describe in Arguments Mode.
(4pts) File avg.py exists and works as describe in TTY Mode.
(4pts) File avg.py exists and works as describe in PIPE Mode.
(3pts) Each mode ignores bad data without crashing the program. Bad data could include text values that cannot be converted to floats, or in the case of a file input, bad data may be additional blank lines.
