import math

from capa import *

F0=250
Q=1.6
GdB=18


RL=470
R=68000

PI=3.1415926

# Open collection
capa_col = openCollection(inventoryFile)

CL=Q/(2*PI*F0*R)
CF=1/(2*PI*F0*Q*RL)
R1=RL*(math.exp(GdB*math.log(10)/20)-1)

result = getAssociation(CL, capa_col)
CL2 = calculate(result, capa_col)
print "CL=", CL, "CL2=", CL2
result = getAssociation(CF, capa_col)
CF2 = calculate(result, capa_col)
print "CF=", CF, "CF2=", CF2

R2=Q*Q*(RL*CF2)/CL2

print "R=", R, "R2", R2

print "CL=", CL*math.pow(10,9), "nF"
print "CF=", CF*math.pow(10,9), "nF"
print "R1=", R1, "ohm"


F0=1/(2*PI*math.sqrt(R*RL*CL2*CF2))
F02=1/(2*PI*math.sqrt(R2*RL*CL2*CF2))
print "F0=", F0, "F02=", F02

Q=math.sqrt((R*CL2)/(RL*CF2))
Q2=math.sqrt((R2*CL2)/(RL*CF2))
print "Q=", Q, "Q2=", Q2
