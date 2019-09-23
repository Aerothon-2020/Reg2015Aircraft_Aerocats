from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 18x8E'
Prop.D          = 18*IN
Prop.Thickness  = 0.48*IN

Prop.Pitch      = 8*IN
Prop.dAlpha     = 3.6*ARCDEG
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .0770/ARCDEG  #- 2D airfoil lift slope
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket
Prop.CDp        = .02          #- Parasitic drag

Prop.Weight     = 86*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None

#Standard correction
STD = STDCorrection(30.26*inHg, (27.2 + 273.15)*K)


#                 RPM,        Thrust
Prop.ThrustData = [(2500 *RPM, 21*OZF*STD),
                   (3500 *RPM, 46*OZF*STD),
                   (4500 *RPM, 81*OZF*STD),
                   (5430 *RPM, 122*OZF*STD)]

###################################################
# TORQUE DATA NOT YET TAKEN - not from this prop.
###################################################
STD2 = STDCorrection(29.95*inHg, (28 + 273.15)*K)

Arm = 19.5*IN*STD2
#                    RPM          TORQUE
Prop.TorqueData = [(6250  *RPM, (7.6*Arm*OZF)),
                   (6000  *RPM, (7.4*Arm*OZF)),
                   (5520  *RPM, (6.1*Arm*OZF)),
                   (4980  *RPM, (4.9*Arm*OZF)),
                   (4050  *RPM, (3.1*Arm*OZF)),
                   (3000  *RPM, (1.8*Arm*OZF)),
                   (2010  *RPM, (0.8*Arm*OZF))]

################################################################################
if __name__ == '__main__':
   
#     print "##################"
#     print " Torque and Power data is not for this propeller!!!!!"
#     print "##################"

    print " D     : ", AsUnit( Prop.D, 'in')
    print " Pitch : ", AsUnit( Prop.Pitch, 'in')
    
    Vmax = 50
    h=0*FT
    N=npy.linspace(1000, 6800, 5)*RPM
    
    Alpha = npy.linspace(-25,25,41)*ARCDEG
    V     = npy.linspace(0,Vmax,30)*FT/SEC
    
    Prop.CoefPlot(Alpha,fig = 1)
    Prop.PTPlot(N,V,h,'V', fig = 2)

#
#    N = npy.linspace(0, 13000,31)*RPM
#    V = npy.linspace(0,Vmax,5)*FT/SEC
#
#    Prop.PTPlot(N,V,h,'N', fig = 3)
    Prop.PlotTestData(fig=4)

    N = 6024*RPM
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 6410*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show() 