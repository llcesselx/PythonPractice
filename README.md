# cs201


CS-201 - Programming Structures
Fall 2022
Instructor: Mr. Luke May
2D Terminal Displays
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

mkdir -p ~/labs/lab3
Lab Problems (60pts)
1) Terminal Box (box.py)
Create a Python 3 program file named box.py. In addition to the standard version and help argument options, this program should accept 2 optional positional arguments. The first positional argument should be a number of columns, and the second should be the number of rows. If either is not provided then they should default to 8. This program should draw a box in the terminal based on these column and row values. The corner piece character should be the plus sign (+), the horizontal character should be a hyphen (-), and the vertical character should be the pipe (|). Here is an example program execution and the expected program results.

Example:
./box.py 10 5
+--------+
|        |
|        |
|        |
+--------+
Setup
On this problem we can just set up a nested for loop. We must be careful about the loop nesting order, however, specifically because of the way that printing characters to the terminal works. The outer loop must iterate through the rows, and the inner loop must iterate through the characters of a particular row. This is how printing to the terminal works -- we start on the first row and print one character at a time until all of the characters on that row have been printed, then we go to the next row and repeat. Moving to the second row is like being on the second iteration of the outer loop, just before you start the inner loop. After the inner loop, each character on that row has been printed.

BONUS Copy the working program from above to a file named box.bonus.py. Keep the original functionality, but add 3 additional arguments to dictate which characters are used for the --horizontal (-H), --vertical (-V), and --corner (-C) components of the box. We will use capital letters for all three of the shortened arguments not to conflict with --version, -v, and --help, -h. For example, if you ran the program with these arguments:

./box.bonus.py -H "^" -V "=" -C "*" 6 4
or

./box.bonus.py --horizontal "^" --vertical "=" --corner "*" 6 4
You would get the following output:

*^^^^*
=    =
=    =
*^^^^*
Note - Putting quotations around the characters limits the ways the shell can misinterpret what we want it to do. We know the shell interprets the pipe (|) as a way to redirect one command's stdout to another commands stdin, so we must use quotes to get the shell to ignore it's normal behavior for that symbol.

Grading (16pts)
Coming soon.
2) Plot Points (plot.py)
Create a Python 3 program file named plot.py. This program will display a Cartesian plane, and plot points (ordered pairs) onto the graph. In addition to the standard version and help argument options, this program should accept an indefinite number of additional positional arguments, each representing a point to plot on a Cartesian plane. If no positional arguments are included, then just the Cartesian plane itself will be displayed. The graph's horizontal axis and borders should use the hyphen - character, and vertical axis and vertical borders should use the pipe character |. There is no need for a special corner character or a special origin (0, 0) character, and you may choose whichever character you like to display when the horizontal or vertical lines intersect (either - or | is acceptable, or something else if you want to get fancy). The dimensions of the Cartesian plane should be 17 by 17, meaning that both the axis values go from -8 to 8.

So an empty Cartesian plane would be displayed with the following command:

./plot.py
Output:

-----------------
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
-----------------
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
|       |       |
-----------------
If you prefer, you may use 2 characters to represent each point on the graph to make the x and y scales look more even. Each positional argument provided should be an ordered pair (x and y coordinate), and should syntactically be represented by two integers separated by a comma. Using a capital letter x (X) to mark the location of plotted point, for each ordered pair argument, plot that point on the graph. Here is an example of running the command and the final output.

./plot.py 2,4 -2,-2 6,-6 -1,1
Output:

-----------------
|       |       |
|       |       |
|       |       |
|       | X     |
|       |       |
|       |       |
|      X|       |
-----------------
|       |       |
|     X |       |
|       |       |
|       |       |
|       |       |
|       |     X |
|       |       |
-----------------
BONUS Copy the working program from above to a file named plot.bonus.py. Keep the original functionality, but double the width of the graph so that each point takes 2 characters. For the horizontal lines use ==, for vertical lines use ||, for the plot points use [], and you must also plot the origin with () if and only if there is not positional plot point provided by the user at point (0, 0).

./plot.bonus.py 2,4 -2,-2 6,-6 -1,1
Output:

==================================
||              ||              ||
||              ||              ||
||              ||              ||
||              ||  []          ||
||              ||              ||
||              ||              ||
||            []||              ||
================()================
||              ||              ||
||          []  ||              ||
||              ||              ||
||              ||              ||
||              ||              ||
||              ||          []  ||
||              ||              ||
==================================
Partial solution to this problem

Grading (20pts)
Coming soon.
3) Move a Character in a Box (boxmove.py)
Create a Python 3 program file named boxmove.py. This program will start off similar to a previous program we made the terminal display a box using the characters - for horizontal lines and | for vertical lines. The first stage of this program will to be to recreate that effect making a box that is by default 13 rows by 23 columns, and that is outlined as before. The program should accept 2 optional positional arguments for the rows and columns. If not provided the above defaults will be used.

Next you will have a character * positioned in the center of the box. You will keep track of the location of that character using whatever system you like. You will get user input from stdin to move the character * to different locations in the box. So in a loop that only ends when a user leaves the input blank, ask the user for input.

The user will enter one of four letters (U for Up, R for Right, D for Down, and L for Left) and then a positive integer. The program should accept upper or lowercase letters. This will be what we call the user command, and your program should respond to such commands accordingly by moving the * character, if possible. For example, a command of L4 should move the * left four spaces. Then another command U2 would move the * up 2 rows. If you are unable to move the character that many spaces while staying in the box, say so, and continue with the loop. So an example output of the program may look something like this:

./boxmove.py
-----------------------
|                     |
|                     |
|                     |
|                     |
|                     |
|          *          |
|                     |
|                     |
|                     |
|                     |
|                     |
-----------------------
Enter a direction character (U, R, D, L) followed by a number of spaces: l4
-----------------------
|                     |
|                     |
|                     |
|                     |
|                     |
|      *              |
|                     |
|                     |
|                     |
|                     |
|                     |
-----------------------
Enter a direction character (U, R, D, L) followed by a number of spaces: u5
-----------------------
|      *              |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
-----------------------
Enter a direction character (U, R, D, L) followed by a number of spaces: u1
Unable to move that many characters.
Enter a direction character (U, R, D, L) followed by a number of spaces: d1
-----------------------
|                     |
|      *              |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
-----------------------
Enter a direction character (U, R, D, L) followed by a number of spaces:
No input detected.  Exiting program.
BONUS Copy the working program from above to a file named boxmove.bonus.py. Keep the original functionality, but include an option in which you can specify an row-column pair and that will move the asterisk character (*) directly to that location, if and only if that location is within the bounds of the box.

For additional points, whenever a number is specified that exceeds the bounds of the box, just move the character to the box edge. Previously we would instead print a message saying that the character could not be moved that far and then we did nothing. This time we will make sure the character is in the maximum position in that direction.

./boxmove.py
-----------------------
|                     |
|                     |
|                     |
|                     |
|                     |
|          *          |
|                     |
|                     |
|                     |
|                     |
|                     |
-----------------------
Enter a direction character (U, R, D, L) followed by a number of spaces: u77
-----------------------
|          *          |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
-----------------------
Enter a direction character (U, R, D, L) followed by a number of spaces: r99
-----------------------
|                    *|
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
|                     |
-----------------------
Enter a direction character (U, R, D, L) followed by a number of spaces:
No input detected.  Exiting program.
Notice the character can never be on the same location as the box border.

Partial solution to this problem:

Grading
Coming soon.
