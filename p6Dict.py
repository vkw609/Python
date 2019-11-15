#CS3723 Ashley Abernathy
#This code provides the declareVar, printVariables, and printLabels functions.


#Takes in a list of tokens and stores the corresponding variable types and values
def declareVar(tokenM, varTypeD, varValueD):
    tokenType = tokenM[0].upper() #gets the type (converted in uppercase)
    tokenName = tokenM[1].upper() #gets the name (converted in uppercase)
    varTypeD[tokenName] = tokenType
    varValueD[tokenName] = tokenM[-1].strip("")


#simply formats and prints the labels with its following contents
def printLabels(labelD):
    print("Labels:")
    print("   Label \t Statement")
    for i in sorted(labelD):
          print("   ", i, "\t", labelD[i])

#simply formats and prints the variables with its following contents
def printVariables(varTypeD, varValueD):
     print("Variables:")
     print("   Variable \t Type \t Value")
     for i in sorted(varTypeD):
         print("   ", i, "\t", varTypeD[i], "\t", varValueD[i])
