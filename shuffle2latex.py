'''
ABOUT THIS FILE:

Name: shuffle2latex.py

Author: Sabine Laszakovits <sabine@laszakovits.net>

Date created: Spring 2015
Date modified: February 2016

Purpose: This file takes one argument, which is the name of the input file. The input file contains questions and answers formatted in a particular way. This program will randomize the order of the questions and the order of the answers per question and output LaTeX code to be included in a larger LaTeX file. 

How to call: copy the line below into your terminal/command line and change INPUTFILE and OUTPUTFILE to your file names.
python shuffle2latex.py INPUTFILE.txt > OUTPUTFILE.tex

How to format the INPUTFILE (sample included):
 - Use a plain text editor, not a rich text editor or text processor like Word. 
 - Be very careful where you put line breaks. They have the meaning that the question text resp. answer text ends and the next question/answer starts. Enable viewing line numbers and/or white space characters in your text editor to be aware of this. 
 - Start the INPUTFILE with an empty line. Begin your text on the second line. 
 - For the question and answer text, write everything in LaTeX commands (bold, italics, diacritics, trees). Do not use LaTeX commands that should go into the preamble (like '\usepackage'). 
 - You can typeset trees. Make sure your LaTeX template has the right package included. Do not use line breaks inside trees typeset here in question or answer!!! 
 - You can start the question text with number+dot+space. This way your question will have an original number that makes the randomization easier to track. This is optional however. 
 - End the question text with one line break. 
 - Directly beneath the question text, write the answer options. Start each option with a letter+dot+space. You can have as many options as you like, but at least one. 
 - Mark correct answers with '\correct' somewhere on the line. If you would like to use a different command for your LaTeX, change the value of the variable 'correctness' below. 
 - End your answer text with a line break.
 - After the last answer option, leave one empty line before starting the next question. 
 - Do not leave empty lines anywhere else. 
 - End the input file with the last answer option. Do not have extra lines at the end. 
'''

# change this to the command that your LaTeX uses to mark the correct answer
correctness = '\correct'

# beneath this line, don't change anything
#########################################################
import os
import random
import sys

class Answer:
	def __init__(self, atext, correct):
		self.atext = atext
		self.correct = correct
	def __str__(self):
		out = ""		
		if self.correct:
			out += "# "
		out += self.atext
		return out

class Question:
	def __init__(self, qtext, orignr):
		self.qtext = qtext
		self.orignr = orignr
		self.answers = []
	def addAnswer(self, a):
		self.answers.append(a)
	def shuffle(self):
		random.shuffle(self.answers)
	def printLatex(self):
		out = '% Q' + self.orignr + os.linesep
		out += '\Q{' + self.qtext + os.linesep + '\A{' + os.linesep
		for a in self.answers:
			out += '\item '
			if a.correct:
				out += '\correct '
			out += a.atext + os.linesep
		out += '}}' + os.linesep
		return out
	def __str__(self):
		out = self.orignr
		return out
	def number(self):
		return self.orignr

input_filename = sys.argv[1]
input = file(input_filename, 'r')

allQ = []

# read blocks, split at new lines
blocks = []
for line in input:
	# if empty line, start new block
	if line in ('\n', '\r\n'): 
		blocks.append([])
	else:
		pureline = line
		pureline = pureline.split('\n')[0]
		pureline = pureline.split('\r\n')[0]
		blocks[len(blocks)-1].append(pureline)

# parse blocks line by line
for block in blocks:
	q = block[0]
	# remove leading number if present
	if q[0].isdigit():
		(orignr,qtext) = q.split('. ', 1)
	else:
		(orignr,qtext) = (0,q)
	# create question
	thisquestion = Question(qtext,orignr)
	# parse answers
	for i in range(1,len(block)):
		a = block[i]
		# remove leading letter
		atext = a.split('. ', 1)[1]
		# find correctness symbol & create answer
		if correctness in atext:
			atext = atext.replace(correctness,'')
			thisanswer = Answer(atext, True)
		else:
			thisanswer = Answer(atext, False)
		# store answer		
		thisquestion.addAnswer(thisanswer)
	# shuffle answers
	thisquestion.shuffle()
	# store question
	allQ.append(thisquestion)

random.shuffle(allQ)
for q in allQ:
	print "% " + q.number()

for q in allQ:
	print q.printLatex()

