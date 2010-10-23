#!/usr/bin/env python2
import re
import math
import sys
import getopt
import os.path

inventoryFile="capa.txt"
nbIter=2


def tranformValue(val, extension):
    extension=extension.lower()
    if extension=="f":
        value=val
    elif extension=="mf":
        value=val * 10**-3
    elif extension=="uf":
        value=val * 10**-6
    elif extension=="nf":
        value=val * 10**-9
    elif extension=="pf":
        value=val * 10**-12
    else:
        raise InputError, "extension error"


    return value

def parseString(st):
    val = float(re.search(r"^[^ a-zA-Z]*", st).group(0))
    ext = re.search(r"[a-zA-Z]+", st).group(0)
    return val, ext

# Calculate value by adding value of given index
def calculate(listIndex, capa_col):
    res=0
    for val in listIndex:
        if val != -1:
            res += capa_col[val][0]
    return res

def iterate(targetValue, iterNum, bestListIndex, currentListIndex, capa_col):
    global nbIter

    if iterNum == nbIter:
        current = calculate(bestListIndex, capa_col)
        new = calculate(currentListIndex, capa_col)
        if (math.fabs(targetValue-new) < math.fabs(targetValue-current)):
            bestListIndex = list(currentListIndex)
    else:
        currentListIndex[iterNum] = -1
        bestListIndex = iterate(targetValue, iterNum + 1, bestListIndex, currentListIndex, capa_col)
        for i in range(0, len(capa_col)):
            currentListIndex[iterNum] = i
            bestListIndex = iterate(targetValue, iterNum + 1, bestListIndex, currentListIndex, capa_col)

    return bestListIndex

def usage():
    global nbIter
    global inventoryFile
    print "Usage:"
    print "%s [options] target_value" % os.path.basename(sys.argv[0])
    print "options:"
    print " --help, -h: this help"
    print " --number, -n: number of capacitor in the association to use (default %i)" % nbIter
    print " --inventory, -i: capacitor inventory file to use (default %s)" % inventoryFile
    print "target_value: target capacitor value to get with capacitor association"

    return

def openCollection(inventoryFile):
    try:
        f = open(inventoryFile);
    except:
        print "Error while opening file %s" %inventoryFile
        sys.exit(-1)

    line_num = 0
    capa_col = []

    for line in f:
        line_num += 1
        try:
            val, ext = parseString(line)
            valFarad = tranformValue(val, ext)
            capa_col.append((valFarad, "%f %s"%(val,ext)))
        except:
            print"error while parsing line %d" % line_num

    return capa_col


def getAssociation(targetValue, capa_col):
    result = [-1] * nbIter
    tmpCur = list(result)
    result = iterate(targetValue, 0, result, tmpCur, capa_col)
    return result

def smartPrint(value, ext):
    stRes=""
    if value >= 1:
        stRes = "%f %s"%(value, ext)
    elif value >= 0.001:
        stRes = "%f m%s"%(value*1000, ext)
    elif value >= 0.000001:
        stRes = "%f u%s"%(value*1000000, ext)
    elif value >= 0.000000001:
        stRes = "%0.3f n%s"%(value*1000000000, ext)
    elif value >= 0.000000000001:
        stRes = "%f p%s"%(value*1000000000000, ext)
    return stRes

def printAssociation(associationResult, capa_col):
    nb = 0
    for i in range(0, nbIter):
        if associationResult[i] != -1:
            nb += 1
            print "capa %d: %s (%s)" %(nb, smartPrint(capa_col[associationResult[i]][0], 'F'), capa_col[associationResult[i]][1])


def main():
    global inventoryFile
    global nbIter

    # Check parameters
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn:i:", ["help", "number=", "inventory="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-n", "--number"):
            nbIter = int(arg)
        elif opt in ("-i", "--inventory"):
            inventoryFile = arg
    if len(args) == 1 :
        targetValueSt = args[0]
    else:
        usage()
        sys.exit()

    # Open collection
    capa_col = openCollection(inventoryFile)

    # Get target value
    try:
        val, ext = parseString(targetValueSt)
        targetValue = tranformValue(val, ext)
    except:
        print "Target value syntax error"

    # Calculate best association
    result = getAssociation(targetValue, capa_col)

    # Print result
    totalCap = calculate(result, capa_col)
    print "Total value:", smartPrint(totalCap, "F")

    printAssociation(result, capa_col)

if __name__ == "__main__":
    main()
