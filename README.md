# ling1010exam
This is a script that shuffles the exam questions for LING 1010 as taught at UConn by Harry or Jon S.  
This document aims to explain to new Tech TAs how to create PDFs for exams from a list of questions and correct answers.
(Version from Spring 2016)

## Overview
You will get a Word-file with the questions and answers from the instructor.
You are supposed to **shuffle** the questions, and within each question shuffle the answers pseudo-randomly, and to make (probably) 3 versions ... for each exam.
Then it is recommended that you use the existing **LaTeX template** to make pretty exams.

This document will show you a way to automatize the shuffling and tell you how to use the LaTeX template.
The shuffling is done by the script called `shuffle2latex.py`, for which you need a computer that has Python and LaTeX installed.
(Python is a scripting language.
Despite the name, it won't bite you.)
You will need to put the questions and answers that they give you into a specific format for the script to be able to read it.
The output of the script can be fed into LaTeX, together with the template `exam-template.tex`.
Then, you will get a pretty PDF for printing.

---
## Setup

### Get the script

You need:
1. The file `shuffle2latex.py`
2. The file `exam-template.tex`

Optional:
* The file `sample-formattedQA.txt`			<= this is what requires work
* The file `sample-latexQA.tex`
* The file `sample-exam-withA.pdf`			<= this is what the final product will look like :)
* The file `sample-exam-withoutA.pdf`		<= and this

To get these files, go to https://github.com/laszabine/ling1010exam (if you're not there already) and use the green button that reads `Clone or download`.
Click `Download ZIP` and save it on your computer, then extract the zip archive.
Alternatively, if you're familiar with git, feel free to clone the repository.

### Install LaTeX

For Windows:
http://www.howtotex.com/howto/installing-latex-on-windows/

For Mac:
http://www.howtotex.com/howto/installing-latex-on-mac-os-x/

If you run into a problem, Google your problem.
You will find instructions and tutorials.

### Install Python 2.7

#### Find out whether you have Python 2.7 installed.

**Step 1**: Open your Command Line/Terminal.
"Command line" and "Terminal" are two words for the same application.
Here I will only call it "Terminal".

For Windows:
* Click the <kbd>Start</kbd> button
* click *Run*
* enter `cmd`
* hit <kbd>Enter</kbd>.
A black window will open, it's called *Command line*.

For Mac:
* Hold <kbd>Apple</kbd> and press <kbd>Space</kbd>,
* type `Terminal`,
* hit <kbd>Enter</kbd>.
A white window will open, it's called *Terminal*.

Remember how to get to your Terminal.
We will need this again.

**Step 2**. Type `python2` and hit <kbd>Enter</kbd>.

If you get a response saying something like `command not found`, you don't have python 2.7 installed.

If it says something like `Python 2.7.15` (any number that starts with 2.7), you do have python 2.7.


**Step 3**. Close the Terminal.

#### If you don't have Python 2.7, install it.

Go to https://www.python.org/downloads/release/python-2715/

Scroll down to *Files*.

For Windows:
  * Choose an *executable installer*, either "x86-64" or "x86", depending on your computer.
    * If you're not sure, choose "x86".

For Mac:
  * You probably have OS 10.11, so choose the one that says "10.9 or newer".

If you run into a problem, Google your problem.
You will find instructions and tutorials.
---

Now we turn to the actual procedure.

## Get the questions

The instructor will give you a list of questions to be asked in the exam.
They may ask you whether you need the questions and answers in a specific format.

Lie and say No.

A Word-document where all the questions are copy-pasted together in inconsistent formatting will do fine.

Remind the instructors/TAs that you need them to mark clearly for every question which answer is the correct one.
Suggest that they put an asterisk in front of the answer, or that they add the words "CORRECT" after the answer, or something like that.

## Format the questions

This is a very important step.
For the shuffling script to be able to read the questions and answers, the questions must be in a **plain text document**, and they must be written in a particular way.

### Find a good plain text editor

Do not use a rich text editor or a word processor.
Rich text editors are anything where you can make text bold or change the font size.
Word processors are even more powerful.
You want something that can show you the characters that you print and nothing else.
It should also be able to show you line numbers and white space characters.

If you have something like this, use it.

If you don't, here are some recommendations:

For Windows:
* Install Notepad++ from https://notepad-plus-plus.org/.
* Enable line numbers.
* Enable displaying white space characters.

For Mac:
* Install TextMate from https://macromates.com/.
* Enable line numbers.
* Enable displaying white space characters.

### Do the formatting

In this plain text editor, create a new document and save it under `exam-?.txt`, where `?` stands for either `1`, `2`, `final`, or `bonus` (or `final-Mon`, `final-Wed`, `bonus-Mon` etc.
  You'll see what you need.)

Copy-paste each question and its answers separately into this text document.
**Follow ALL the instructions below.**
Look at the file `sample-formattedQA.txt` to see an example of what it should look like.

* Use new lines exactly where these instructions tell you to use them.
Do not use them anywhere else.
This is because, for this script, every new line means "this is the end of the question text" resp. "this is the end of the answer text".
You don't want the script to think your text ends where it doesn't.

  * Clarification:
  "new line" means hitting <kbd>Enter</kbd>.
  You can see this by looking at the line numbers.
  New lines will have a new number.
  If the text in one line is too long to fit on the screen, your editor may continue it in the line below.
  This is fine.
  (You can change this in the settings. It's called "wrapping".)

* Start the file with an empty line.
Begin writing in the second line.

* You can start the question text with number+dot+space (for example `15. `), or you can start the text directly.
(Do not mix and match!)
If you use number+dot+space, your question will have an original number that makes the randomization easier to track.
  * It is a good idea to use extra large numbers, such as starting from 101 going to 140.
  This way you won't mix up this number, which is an identifier for the question, and the position of this question in the shuffled version (where numbers will go from 1 to 40).

* For the question and answer text, write everything in LaTeX commands (bold, italics, diacritics, trees).
Do not use LaTeX commands that should go into the preamble (like `\usepackage`).
  * You can typeset trees.
  Make sure `exam-template.tex` has the right package included.
  Do not use new lines inside trees!!!

* End the question text with one empty line.

* In the line beneath the question text, write the answer options.
Start each option with a letter+dot+space (e.g. `a. `).
You can have as many options as you like, but you need to have at least one.
  * Again, you can use any letter for identifiers of the answers (e.g. `x. `, `y. `, and `z. `).

* Mark correct answers with `\correct` (small letters) somewhere on the line of the correct answer.

* Write the next answer into the next line.
Again, start with letter+dot+space (e.g. `y. `).

* After the last answer option, leave one empty line before starting the next question.

* End the input file with the last answer option.
Do not leave an extra empty line at the end.
This is important.

* Do not start new lines anywhere else.

Check the file `sample-formattedQA.tex` to see an example of a correctly formatted file.

## Run the shuffler script

**Step 1.**
Open the Terminal.

**Step 2.**
Navigate to the folder where all these files are.
* On Windows, use `dir` to see the list of current files and folders.
* On Mac use `ls`.

Find the next folder you want to navigate to.
Write `cd foldername`, then hit <kbd>Enter</kbd>.
You are now one folder deeper.
Continue this until you are in the target folder.
If you've made a mistake and you need to go one level up, type `cd ..` and hit <kbd>Enter</kbd>.

Hint:
You can save yourself some typing if you just type the first couple of letters of the next foldername and then hit <kbd>Tab</kbd>.
This will auto-complete if the letters you've typed already uniquely identify a folder.
If it's not yet unique, you can hit <kbd>Tab</kbd> twice and you'll see a list of all files that match this beginning.

Hint:
Perhaps if you right-click in your file browser, or perhaps in the menu items, you can find an option “Open terminal here” or “Open command line here”.
This will save you the navigation.
If you can't find it, ask Google whether your browser supports this.

**Step 3.**
Once you've reached the target folder, type `python2 shuffle2latex.py exam-?.txt > exam-?-v?.tex`.
Pay attention to the spaces.
Substitute `exam-?` for the name of the exam you are currently working on and `v?` for the version you are currently generating.

**Step 4.**
Wait for the script to complete.
It should be done in a couple of seconds.

**Step 5.**
Now you have an additional file called `exam-?-v?.tex` (with whatever you chose instead of `?`).
It should look similar to the file `sample-latexQA.tex`.

**Step 6.**
Repeat this for the other version.
Change `v1` to `v2` etc.

## Set output parameters

**Step 1.**
Open `exam-template.tex` in your LaTeX editor.
You should have received one with your LaTeX installation.

1. Scroll down to where it says `CHANGE THIS HERE`

1. Change the values of `\CLASS`, `\EXAM`, `\SEMESTER`, and `\VERSION`, if necessary.
  * Leave the tilde `~`.
  It will show up as space in the output.

**Step 2.**
The last line in this block says `%\def\correct{}`.
If this line starts with a percentage symbol, the PDF will contain small arrows that indicates the correct answer.
This is useful for manual grading.
If this line does not start with a percentage symbol but looks like this: `\def\correct{}`, the PDF will not contain these small arrows.
You should create both kinds of PDFs.
(There's more on this line after this, but this is a comment too, as it starts with a percentage symbol. Leave it there.)

**Step 3.**
Scroll down to the end of the file where it again says `CHANGE THIS HERE`.

1. Change the value of `\input` to the name of your newly generated tex-file, e.g. `exam-1-v1.tex`

1. Save `exam-template.tex`.

## Run LaTeX

**Step 1.**
In your LaTeX editor, use `pdflatex` (should be the default) to generate a PDF out of `exam-template.tex`

**Step 2.**
This file will automatically be named `exam-template.pdf`.
Find it in your file browser and rename it to `exam-1-v1-withA.pdf` (for example).

**Step 3.**
Look at the PDF and check that everything is ok.
If they gave you 40 questions, chances are that they will fit exactly onto 4 pages.
If 1-3 questions are on the 5th page, you may be able to save a lot of paper by shuffling the questions differently so that you only need 4 pages.
For this go back to step "Run the shuffler script".
This may take a couple of trials.
Don't give up, think of the trees :)

**Step 4.**
Overall, for each exam, you should create the following PDFs:

  1. `exam-?-v1-withA.pdf`
	1. `exam-?-v1-withoutA.pdf`
	1. `exam-?-v2-withA.pdf`
	1. `exam-?-v2-withoutA.pdf`
	1. `exam-?-v3-withA.pdf`
	1. `exam-?-v3-withoutA.pdf`

**Step 5.**
Share these PDFs with the other TAs.

**Step 6.**
When you print the hundreds of copies for the exam, pay attention to printing the versions “withoutA” ;)

**Step 7.**
Keep all the auxiliary documents, such as `exam-1.txt` and `exam-1-v1.tex`.
Do not delete them until a year after the semester is over.
This may be necessary if there was a problem and students have questions about their grade.
