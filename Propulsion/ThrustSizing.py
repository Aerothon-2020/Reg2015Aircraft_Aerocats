from __future__ import division # let 5/2 = 2.5 rather than 2

#from os import environ as _environ; _environ["scalar_off"] = "off"

from scalar.units import LBF, FT, IN, SEC, ARCDEG, Pa, MIN, OZF, gacc
from scalar.units import AsUnit
from cmath import sin, sqrt
import cmath as math
import pylab as pyl
import numpy as npy
#from Aircraft_Models.Micro2013Aircraft_MicroCats.MonoWing.Aircraft import Aircraft
from Aircraft_Models.Micro2013Aircraft_MicroCats.WeightTradeStudy.Aircraft09 import Aircraft


RoC = 200*FT/MIN        #Desired rate of climb
Aircraft.Bungee_X=5.5*FT  #Maximum stretch of the bungee cord

Gs = npy.linspace(6, 8, 3)
TWs = npy.linspace(0.75, 1.5, 4)*LBF

TWs = npy.array(Aircraft.TotalWeight/LBF)*LBF

pyl.figure(1)
legend = []
V_los = []

for G in Gs:
    print "Gload :", G
    Thrust = []
    Bungee_K = []
    
    #V_los.append((G*32.2*6)**0.5)
    for TW in TWs:
        print "Total Weight :", AsUnit(TW, 'lbf')
        Aircraft.TotalWeight = TW
        Aircraft.Bungee_K = G*Aircraft.TotalWeight/Aircraft.Bungee_X
        V_LO = Aircraft.DeadLaunch_V_LO()
        #V_los.append(V_LO)
        
        #Compute the thrust based on a given rate of climb
        # RoC = V_LO*((T-Drag(V_LO))/TW
        Thrust.append( ( RoC*TW/V_LO + Aircraft.Drag(V_LO) )/OZF )
        Bungee_K.append( Aircraft.Bungee_K/(OZF/IN) )

    #pyl.subplot(211)
    #pyl.plot(G, V_los)
    #pyl.subplot(212)
    pyl.subplot(121)
    pyl.plot( TWs/LBF, Thrust, '-o' )
    legend.append('G %1.1f' % G )
    pyl.legend(legend, loc='best')
    pyl.xlabel("Total Weight (LBF)"); pyl.ylabel("Required Thrust (ozf)")
    
    pyl.subplot(122)
    pyl.plot( TWs/LBF, Bungee_K, '-o' )
    legend.append('G %1.1f' % G )
    pyl.legend(legend, loc='best')
    pyl.xlabel("Total Weight (LBF)"); pyl.ylabel("Required K (ozf/in)")
    
pyl.show()