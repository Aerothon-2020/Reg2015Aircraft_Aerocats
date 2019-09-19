from __future__ import division # let 5/2 = 2.5 rather than 2

#
# The following line turns off unit checking. Make sure things are working before it is turned off
#
from os import environ as _environ; _environ["scalar_off"] = "off"


import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN, ARCDEG
from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
#from Aircraft_Models.Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_40 import Aircraft
#from Aircraft_Models.Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_106_2050 import Aircraft
# from Aircraft_Models.Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_NickSchwartz import Aircraft
Aircraft.Draw(fig=2)
pyl.figure(1)

#
# Get the design point
#
dsgnGR = Aircraft.Groundroll() / (FT)
dsgnCR = Aircraft.Rate_of_Climb() / (FT/MIN)
pyl.plot([dsgnCR],[dsgnGR],'ro', markersize = 8)

#
# Set up ranges
#
S    = npy.linspace(1500,1900,5)*IN**2
Span = npy.linspace(92,102,6)*IN

lgnd = ['Design W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF)]
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(Span),len(S)))
clmbrate = npy.zeros((len(Span),len(S)))

#
# Calculate the groundroll and climb rate
#
for ii in range(len(Span)):
    print "Calculating at Span = ", Span[ii]/IN
    for jj in range(len(S)):
        print "Calculating at S = ", S[jj]/IN**2
        Aircraft.Wing.S = S[jj]
        Aircraft.Wing.b = Span[ii]
        
        grndroll[ii][jj] = Aircraft.Groundroll() / (FT)
        clmbrate[ii][jj] = Aircraft.Rate_of_Climb() / (FT/MIN)
        
        print "Climb Rate = ", clmbrate[ii][jj]

#
# Plot the calculated values
#
for ii in range(len(Span)):
    clmplt = []
    grnplt = []
    for jj in range(len(S)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('b = %2.0f (in)' % (Span[ii] / IN))
    
for jj in range(len(S)):
    clmplt = []
    grnplt = []
    for ii in range(len(Span)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append('S = %4.0f (in^2)' % (S[jj] / IN**2))

#lgnd.append('W = %2.0f (lbf)' % (Aircraft.TotalWeight / LBF))

pyl.plot()
pyl.axhline(y = 190, color = 'k', lw = 1)
pyl.axvline(x = 100, color = 'k', lw = 1)
pyl.title('Groundroll and Climb Rate for Varying Wing Area and Span')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

pyl.show()