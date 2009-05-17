import matplotlib.pyplot as pp
import numpy as np

a = np.arange(-0.01, 1.01, 0.01)

P2 = 25000.0
R0 = 4700.0
R1 = 32618.0
R2 = R1

y = 20*np.log10(( R0 + a*(R1 + (1-a)*P2))/( R0 + (1-a)*(R2+a*P2) ))

print y
pp.plot(a, y, "-")
a=0
print (( R0 + a*(R1 + (1-a)*P2))/( R0 + (1-a)*(R2+a*P2) ))
print (R0+R1)/R0
a=1
print (( R0 + a*(R1 + (1-a)*P2))/( R0 + (1-a)*(R2+a*P2) ))
print R0/(R0+R2)


pp.show()

