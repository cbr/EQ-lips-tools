#!/usr/bin/env python2

import matplotlib.pyplot as pp
import numpy as np

# Draw gain of filter given its Pot value (P2) R1 and RL. It shows the
# shape of the gain according to pot position. It enables to analyze
# the linearity of the gain given various parameters.

a = np.arange(-0.01, 1.01, 0.01)

P2 = 10000.0
RL = 470.0
R1 = 3300.0
R2 = R1

y = 20*np.log10(( RL + a*(R1 + (1-a)*P2))/( RL + (1-a)*(R2+a*P2) ))

#print y
pp.plot(a, y, "-")
a=0
#print (( RL + a*(R1 + (1-a)*P2))/( RL + (1-a)*(R2+a*P2) ))
print "Gain max =", 20*np.log10((RL+R1)/RL)
a=1
#print (( RL + a*(R1 + (1-a)*P2))/( RL + (1-a)*(R2+a*P2) ))
print "Gain min =", 20*np.log10(RL/(RL+R2))


pp.show()

