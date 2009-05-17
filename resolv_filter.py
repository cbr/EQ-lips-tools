import math

F0=250
Q=1.6
GdB=18


RL=470
R=68000

PI=3.1415926

CL=Q/(2*PI*F0*R)
CF=1/(2*PI*F0*Q*RL)
R1=RL*(math.exp(GdB*math.log(10)/20)-1)

print "CL=", CL*math.pow(10,9), "nF"
print "CF=", CF*math.pow(10,9), "nF"
print "R1=", R1, "ohm"
