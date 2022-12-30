# cs201


## CS-201 - Programming Structures
### Fall 2022
### Instructor: Mr. Luke May
### Course Tools and Python Arguments
### Preparation

## 1) Sublime Editor (Preferences.sublime-settings)
Follow the tutorial on Installing and Configuring Sublime Editor. Install all relevant packages and make all the changes to your settings. Once completed, you'll need to find your Sublime configuration file which should be located in your user's Home directory. To locate the file, in sublime, click the menu Preferences -> Browse Packages, and a file explorer windows should open in the Packages directory. To receive credit for this part of the lab, you will need to add the preferences specified below to your Sublime preferences file (Preferences.sublime-settings), then use an SFTP Client to copy the preferences file to the CS Server. Place it in this location on the CS Server ~/labs/lab1/Preferences.sublime-settings. You can change the settings to your own personal preference, but to get full credit you must have a least 4 different settings that are different from the defaults.

Grading (10pts)
(10pts) File ~/labs/lab1/Preferences.sublime-settings exists and shows the configuration was completed as outlined in the tutorial.
2) Install Python 3 (python3.png)
If you have not already, watch and follow along with the Python 3 Installation Tutorial. Make sure you follow the steps to configure Sublime and PyFlakes. Open a terminal or command line on whatever OS you use and determine the version of Python 3 you have installed.

MacOS and Linux
python3 --version
Windows
python --version
Take a screenshot of just the terminal window showing that you have the proper version of node installed, and name the file python3.png (or some other image file extension, like .jpg, or .bmp). If you take a full-screen screenshot you will lose points. You are to install this on your own machine, so screenshots from running this command on the CS Server will not be counted.

Grading (10pts)
(10pts) File ~/labs/lab1/python3.png exists and shows you have Python 3 installed on your system and have it running from the terminal. Do not take a screenshot of running this command on the CS Server. It must be installed on your machine for credit.
3) Installing and Configuring Pyflakes Code Linter
Files
pyflakes-errors.png
pyflakes-fixed.png
linter_test.py
Pyflakes is a code linter, which is a program that scans your code and can make it cleaner (like a lint brush going over a shirt). Code linters are extremely helpful tools because they can help prevent you from making numerous simple mistakes. They cannot fix everything, but the can fix a lot.

From the previous tutorial make sure you followed the instructions to install and configure pyflakes for use with the Sublime. In that tutorial it instructs you to create a text file that intentionally has coding errors. Create that file and save it, then take a screenshot of the code in Sublime with the linter errors, and call it pyflakes-errors.png. It should looks something like the image in the tutorial.

Next fix the errors as the tutorial suggests, and take another screenshot without the linter errors. Call this file pyflakes-fixed.png.

Also include the file linter_test.py in your lab submission with the corrected code from the tutorial.

Grading (10pts)
(4pts) File ~/labs/lab1/pyflakes-errors.png and displays the bad code in Sublime and the linter errors.
(4pts) File ~/labs/lab1/pyflakes-fixed.png exists and displays the corrected code in Sublime and no linter errors.
(2pts) File ~/labs/lab1/linter_test.py exists and displays the corrected code.
4) Get Arguments (get_args.py)
Watch these tutorial videos on Python 3 Scripting Basics if you have not already.

Create a file named get_args.py in ~/labs/lab1. Add the appropriate hashbang at the top of the file, and set the permissions with chmod so that the file is executable by all entities. This program should list out any arguments provided to the program from the command-line. For example, running the program with the following arguments

./get_args.py banana fuji\ apple "mandarin orange"
should output

banana
fuji apple
mandarin orange
Version
It is good practice for programs to have a version argument to track which version of the program you may be using. If either of the arguments -v or --version appear in the arguments list, the standard behavior of the program should be ignored, the program should output a version number, and then the program should exit with no error code exit(0). For example running the program in any of these ways

./get_args.py --version
./get_args.py -v
./get_args.py banana fuji\ apple "mandarin orange" --version
should output a version number then exit, like this

0.0.6
Usually you might start the version number at 0.0.1, and as you make changes to the program and add features you might increment the version number.

Help
If the either of arguments -h or --help are provided, the normal behavior of the program should be ignored. Instead a help message should appear explaining what the program does (lists out provided arguments, 1 per line), and what special arguments can be used (-h, --help, -v, --version) and their associated functionality. Then the program should exit with status code 0. You may decide how to handle conflicts with both --version and --help however you like. One solution may be to always display the version is the the version arguments are present and ignore any others.

No Args
If no arguments are provided, a message should be displayed from stderr saying that you must provide the program with arguments: You must provide arguments to this program. or something similar. You may also direct them to the help text is you like Run with "--help" option for more information. or something similar. Remember you must use stderr to print those (e.g. print(message, file=sys.stderr)). Then at this point the program should exit with an error code 1 (exit(1)).

Grading (20pts)
You may lose points for incorrect file or argument naming (letter case matters!), failing to set the permissions, leaving off the hashbang, or wrong line endings.

(8pts) Program ~/labs/lab1/get_args.py displays all of the provided arguments to the program, one per line.
(4pts) Program ~/labs/lab1/get_args.py displays a version number if -v or --version are provided as arguments, then exits with status code 0.
(4pts) Program ~/labs/lab1/get_args.py displays a help message if -h or --help are provided as arguments, then exits with status code 0.
(4pts) Program ~/labs/lab1/get_args.py, when run with no arguments, displays an error message over stderr, and then exits with status code 1.
The above program can serve as a nice template to start many of your programs, but you won't be required to use it in that way.

