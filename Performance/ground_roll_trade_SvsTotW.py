from __future__ import division # let 5/2 = 2.5 rather than 2

from os import environ as _environ; _environ["scalar_off"] = "off"

import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN
from scalar.units import AsUnit
from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
# from Aircraft_Models.Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_NickSchwartz import Aircraft

pyl.figure(1)

#
# Get the design point
#
dsgnGR = Aircraft.Groundroll() / (FT)
#dsgnCR = Aircraft.Rate_of_Climb(1.07*Aircraft.GetV_LO()) / (FT/MIN)
dsgnCR = Aircraft.Rate_of_Climb() / (FT/MIN)
pyl.plot([dsgnCR],[dsgnGR],'ro', markersize = 8)

#
# Set up ranges
#
MinCumpRate = 150
S    = npy.linspace(1500,1900,5)*IN**2
WT   = npy.linspace(32,35,4)*LBF

lgnd = ['Design']
arealist = []

# Initialize data arrays
grndroll = npy.zeros((len(WT),len(S)))
clmbrate = npy.zeros((len(WT),len(S)))

#
# Calculate the groundroll and climb rate
#
for ii in range(len(WT)):
    print "Calculating total weight = ", AsUnit( WT[ii], 'lbf' )
    for jj in range(len(S)):
        print "Calculating at S = ", AsUnit( S[jj], 'in**2' )
        Aircraft.Wing.S = S[jj]
        Aircraft.TotalWeight = WT[ii]
        
        grndroll[ii][jj] = Aircraft.Groundroll() / (FT)
        clmbrate[ii][jj] = Aircraft.Rate_of_Climb() / (FT/MIN)
        print "Climb Rate: ", Aircraft.Rate_of_Climb() / (FT/MIN)
        if ii == 0:
            arealist.append(Aircraft.Wing.S)
        

#
# Plot the calculated values
#        
for ii in range(len(WT)):
    clmplt = []
    grnplt = []
    for jj in range(len(S)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('W = %2.0f (lbf)' % (WT[ii] / LBF))
    
for jj in range(len(S)):
    clmplt = []
    grnplt = []
    for ii in range(len(WT)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append(r'S = %4.0f (in$^2$)' % (arealist[jj] / IN**2))

pyl.plot()
# pyl.axhline(y = 150, color = 'k', lw = 1)
# pyl.axvline(x = MinCumpRate, color = 'k', lw = 1)
pyl.title('Groundroll and Climb Rate for Varying Wing Area and Total Weight')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)
pyl.ylim( 0, 400 )
pyl.xlim( 50, 350 )

pyl.show()