#!/usr/bin/python

import math

from capa import *

#F0=250
QCommon=1.6
GCommon=18


RL=470
R=68000

PI=3.1415926

def calc(F0, Q, GdB):
    print
    print "###############################"
    print "### freq=", F0, "Q=", Q, "GdB=", GdB
    print "###############################"
    CL_theo=Q/(2*PI*F0*R)
    CF_theo=1/(2*PI*F0*Q*RL)
    R1=RL*(math.exp(GdB*math.log(10)/20)-1)

    resultCL = getAssociation(CL_theo, capa_col)
    CL_real = calculate(resultCL, capa_col)
    resultCF = getAssociation(CF_theo, capa_col)
    CF_real = calculate(resultCF, capa_col)


    print "R1=", R1, "ohm"
    print "CL_theo=", smartPrint(CL_theo, "F"), "CL real=", smartPrint(CL_real, "F")
    printAssociation(resultCL, capa_col)
    print
    print "CF_theo=", smartPrint(CF_theo, "F"), "CF real=", smartPrint(CF_real, "F")
    printAssociation(resultCF, capa_col)


    # Standard result
    F01=1/(2*PI*math.sqrt(R*RL*CL_real*CF_real))
    Q1=math.sqrt((R*CL_real)/(RL*CF_real))
    print
    print "R=", R
    print "F0=", F01, "Q=", Q1

# Open collection
capa_col = openCollection("../../all_capa.txt")



calc(32, QCommon, GCommon)
calc(64, QCommon, GCommon)
calc(125, QCommon, GCommon)
calc(250, QCommon, GCommon)
calc(500, QCommon, GCommon)
calc(1000, QCommon, GCommon)
calc(2000, QCommon, GCommon)
calc(4000, QCommon, GCommon)
calc(8000, QCommon, GCommon)
calc(16000, QCommon, GCommon)

print
print ">>>"
print "250 Hz and 1000 Hz are not very good"
