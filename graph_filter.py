#!/usr/bin/env python2
#
# Copyright 2010 Cedric Bregardis.
#
# This file is part of EQ-lips tools.
#
# EQ-lips tools is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, version 3 of the
# License.
#
# EQ-lips tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EQ-lips tools.  If not, see <http://www.gnu.org/licenses/>.
#

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

