#CS3723 Ashley Abernathy assignment 7
#The program is passed the name of the BEEP source code file.
#It reads and prints all the BEEP source code lines (showing line numbers)
#and places them in a list
#has to be called p5 for w/e reason.



import sys
import traceback

from p6Dict import declareVar, printLabels, printVariables #import code from other file
from p6Exec import *

f = open(sys.argv[1], "r")

if len(sys.argv) < 2:
    print("Error: not enough arguments")
    sys.exit(1)

#variables
varTypeD = {}
varValueD = {}
labelD = {}
i = 0

print("BEEP source code in " + sys.argv[1] + ":")

#while reading the file is true
while True:

    fileLine = f.readline()

    if fileLine == "":
        break

    fileLine = fileLine.rstrip('\n') #removes the newline char

    i += 1 #line increment
    print('{}. {}'.format(i, fileLine)) #print the line with newly stripped fileLine

    lineTokens = fileLine.split() #splits fileLine and saves into lineTokens



    if len(lineTokens) == 0:
      continue

    if(lineTokens[0][-1] == ':'): #checks for label
        lineNumber = i
        token = lineTokens[0][:-1].upper()
        if(token in labelD): #If the same label is encountered at the beginning of two or more statements
            print('***ERROR: label \'{}\' appears in multiple lines:: {} and {}'.format(token, labelD[token], lineNumber))
        labelD[token] = lineNumber
        lineTokens = lineTokens[1:]

    if(lineTokens[0] == 'VAR'): #checks for VAR variable
        declareVar(lineTokens[1:], varTypeD, varValueD)

#print the labels and variables
printVariables(varTypeD, varValueD)
printLabels(labelD)

#close file
f.close()

if sys.argv[-1] == '-v':
    print("execution begins...")
    executeBEEPstate(lineTokens, varTypeD, varValueD, labelD)
