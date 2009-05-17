#!/usr/bin/python
import re
import math
import sys
import getopt
import os.path

def tranformValue(value, extension):
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

def calculate(listIndex):
    res=0
    for i in range(0, len(listIndex)):
        if listIndex[i] != -1:
            res += col[listIndex[i]][0]
    return res

def iterate(iterNum, listIndex):
    global result
    global targetValue
    global nbIter
    if iterNum == nbIter:
        current = calculate(result)
        new = calculate(listIndex)
        if (math.fabs(targetValue-new) < math.fabs(targetValue-current)):
            result = list(listIndex)
    else:
        listIndex[iterNum] = -1
        iterate(iterNum + 1, listIndex)
        for i in range(0, count):
            listIndex[iterNum] = i
            iterate(iterNum + 1, listIndex)

def usage():
    print "Usage:"
    print "%s [options] target_value" % os.path.basename(sys.argv[0])
    print "options:"
    print " --help, -h: this help"
    print " --number, -n: number of capacitor in the association to use (default %i)" % nbIter
    print " --inventory, -i: capacitor inventory file to use (default %s)" % inventoryFile
    print "target_value: target capacitor value to get with capacitor association"

    return

inventoryFile="capa.txt"
targetValueSt=""

nbIter=2

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

try:
    f = open(inventoryFile);
except:
    print "Error while opening file %s" %inventoryFile
    sys.exit(-1)

count = 0
line_num = 0
col = []

try:
    val, ext = parseString(targetValueSt)
    targetValue = tranformValue(val, ext)
except:
    print "Target value syntax error"


result = [-1] * nbIter
for line in f:
    line_num += 1
    try:
        val, ext = parseString(line)
        count += 1
        valFarad = tranformValue(val, ext)
        col.append((valFarad, "%f %s"%(val,ext)))
    except:
        print"error while parsing line %d" % line_num



tmpRes = list(result)
iterate(0, tmpRes)


totalCap = calculate(result)
if totalCap >= 1:
    print "Total value: %f F"%totalCap
elif totalCap >= 0.001:
    print "Total value: %f mF"%(totalCap*1000)
elif totalCap >= 0.000001:
    print "Total value: %f uF"%(totalCap*1000000)
elif totalCap >= 0.000000001:
    print "Total value: %0.3f nF"%(totalCap*1000000000)
elif totalCap >= 0.000000000001:
    print "Total value: %f pF"%(totalCap*1000000000000)

nb = 0
for i in range(0, nbIter):
    if result[i] != -1:
        nb += 1
        print "capa %d: %s" %(nb, col[result[i]][1])



