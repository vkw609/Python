import re
import traceback

from p6Dict import *
# Raise several exceptions which should be caught by the execution
# function and cause the program to terminate

class TooFewOperands(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class VarNotDefined(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class LabelNotDefined(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class InvalidExpression(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

class InvalidValueType(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

#executeBEEPstate
#
#finds which variable and calls a function accordingly
#ASSIGN variableName expression
#IF expression label
#PRINT varLiteral1 varLiteral2 …
#GOTO label

def executeBEEPstate(lineTokens, varTypeD, varValueD, labelD):

    totalCount = 0
    lineNum = 0
    i = 0

    #while reading up until the end of lineTokens
    while i < len(lineTokens):
        lineNum = i+ 1

        if not (len(lineTokens) == 0):
            totalCount += 1

        if len(lineTokens) == 0:
            i+=1
            continue

        if lineTokens[0] == 'VAR':
            i += 1
            continue

        if lineTokens[0] == 'PRINT':
            execPrint(lineTokens[1:])

        if lineTokens[0] == 'ASSIGN':
            execAssign(lineTokens[1:],varTypeD, varValueD,lineNum)

        if lineTokens[0] == 'IF' or lineTokens[1] == 'IF':
            temp_line = execIf(lineTokens[2:], labelD,lineNum)
            if isinstance(temp_line, int):
                lineNum = temp_line-2
                i = temp_line-2

        if lineTokens[0] == 'GOTO':
                temp_line = execGoto(lineTokens[1:],labelD,lineNum)
                if isinstance(temp_line, int):
                    lineNum = temp_line-2
                    i = temp_line-2
        i += 1

        if totalCount > 5000:
            break

#expression function
#
#* varLiteral varNumber	return a string with varLiteral replicated varNumber times
#+ varNumber1 varNumber2	return the sum of the values
#- varNumber1 varNumber2	return the difference of the values (varNumber1 minus varNumber2)
#> varNumber1 varNumber2	return True if varNumber1 > varNumber2; this is a numeric comparison
#>= varNumber1 varNumber2	return True if varNumber1 >= varNumber2; this is a numeric comparison
#& varLiteral1 varLiteral2	return the concatenation of the two strings

def expression(lineTokens, lineNum):
    try:
        #compute for the expression
        if lineTokens[1] == '*':
            op1 = lineTokens[0]
            op2 = lineTokens[2]
            return str(op1) * op2

        if lineTokens[1] == '+':
            op1 = lineTokens[0]
            op2 = lineTokens[2]
            return int(op1) + int(op2)

        if lineTokens[1] == '-':
            op1 = lineTokens[0]
            op2 = lineTokens[2]
            return int(op1) - int(op2)

        if lineTokens[1] == '>':
            op1 = lineTokens[0]
            op2 = lineTokens[2]
            return int(op1) > int(op2)

        if lineTokens[1] == '>=':
            op1 = lineTokens[0]
            op2 = lineTokens[2]
            return int(op1) >= int(op2)
        if lineTokens[1] == '&':
            op1 = lineTokens[0]
            op2 = lineTokens[2]
            if op1 == False or op2 == False:
                return
            return str(op1) + str(op2)
        else:
            raise InvalidExpression ("'%s' is an Unknown operator" % (str(tokens[0])))
    except (InvalidExpression) as e:
        print ("\n*** line %d error detected ***" % (lineNum))
        print("%-10s %d *** %s ***" % (" ", lineNum, str(e.args[1])))
        return
    except Exception as e:
        print("\n*** line %d error detected ***" % (lineNum))
        print(e)
        return
    except:
        print("\n*** line %d error detected ***" % (lineNum))
        traceback.print_exc()
        return


#simply print. doesn't print what it is supposed to though
def execPrint(lineTokens):
    for token in lineTokens:
        print(token.strip('"'),end = ' ')
        print()


#function if case it is assign
def execAssign(lineTokens,varTypeD,varValueD,lineNum):
    try:
        if len(lineTokens):
            varL = varLiteral(lineTokens[1],varValueD,lineNum)
            if varL != False:
                tokens = [varTypeD[lineTokens[0].upper()],lineTokens[0].upper(),str(var_literal)]
                declareVar(tokens,varTypeD,varValueD)
        else:
            raise TooFewOperands('Too few operand for this operation')

    except (TooFewOperands) as e:
        print ("\n*** line %d error detected ***" % (lineNum))
        print("%-10s %d *** %s ***" % (" ", lineNum, str(e.args[1])))
        return
    except Exception as e:
        print("\n*** line %d error detected ***" % (lineNum))
        print(e)
        return
    except:
        print("\n*** line %d error detected ***" % (lineNum))
        traceback.print_exc()
        return


#function if case either if or goto
def execIf(lineTokens, labelD, lineNum):
    try:
        check = expression(lineTokens[1:3],lineNum)
        if isinstance(check,bool) and check == True:
            if lineTokens[3].upper() in labelD.keys():
                return int(labelD[lineTokens[3].upper()])
        else:
            raise LabelNotDefined ("'%s' is not defined as a label" % str(lineTokens[3]))

    except (LabelNotDefined) as e:
        print ("\n*** line %d error detected ***" % (lineNum))
        print("%-10s %d *** %s ***" % (" ", lineNum, str(e.args[1])))
        return
    except Exception as e:
        print("\n*** line %d error detected ***" % (lineNum))
        print(e)
        return
    except:
        print("\n*** line %d error detected ***" % (lineNum))
        traceback.print_exc()
        return

def execGoto(lineTokens, labelD, lineNum):
    try:
        check = expression(lineTokens[1:3],lineNum)
        if isinstance(check,bool) and check == True:
            if lineTokens[3].upper() in labelD.keys():
                return int(labelD[lineTokens[3].upper()])
        else:
            raise LabelNotDefined ("'%s' is not defined as a label" % str(lineTokens[3]))

    except (LabelNotDefined) as e:
        print ("\n*** line %d error detected ***" % (lineNum))
        print("%-10s %d *** %s ***" % (" ", lineNum, str(e.args[1])))
        return
    except Exception as e:
        print("\n*** line %d error detected ***" % (lineNum))
        print(e)
        return
    except:
        print("\n*** line %d error detected ***" % (lineNum))
        traceback.print_exc()
        return


#checks the type of varLiteral
def varLiteral (lineTokens, varValueD,lineNum):
    try:
        if lineTokens.upper() in varValueD.keys():
            return varValueD[lineTokens.upper()]
        if lineTokens.isdecimal():
            return int(lineTokens)
        else:
            raise VarNotDefined("'%s' is not defined" % (lineTokens))

    except VarNotDefined as e:
        print ("\n*** line %d error detected ***" % (lineNum))
        print("%-10s %d *** %s ***" % (" ", lineNum, str(e.args[1])))
        return False
    except Exception as e:
        print("\n*** line %d error detected ***" % (lineNum))
        print(e)
        return False
    except:
        print("\n*** line %d error detected ***" % (lineNum))
        traceback.print_exc()
        return False
