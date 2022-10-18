# cs201

Each branch is a seperate lab that was required for cS201 - Programming Structures

Lab Portion - 50% of exam (54pts + 4pts Bonus)
You can lose points if you don't follow these requirements:

All files:

Must use only the the Line Feed character for line endings.
Must include the Hashbang.
Must have the executable bits set for all chmod entities.
Modules/Scripts (not necessary for ```.lab_tests.py``` files)

Must support the help arguments ```--help/-h``` with a relevant help message then exiting.
Must support the version arguments ```--version/-v ```with a version number then exiting.
Must have tests using ```if __name__ == "__main__":```.


Lab Setup
Turn in all the files by creating the following directory and placing them in that location on the CS Server.

mkdir -p ~/labs/midterm
Auto Grader
There is an auto-grader for this lab that should give you a reasonable idea of your grade. This program will help to ensure that you have named your files correctly and that your programs work reasonably well. Again, the result here does not guarantee your final lab grade, but is should give a reasonable estimate of your grade.

Navigate to your lab folder:

cd ~/labs/midterm
Then run the grader:

cs201-midterm-grader.py
