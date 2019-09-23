from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 17x7E'
Prop.D          = 17*IN
Prop.Thickness  = 0.5*IN

Prop.Pitch      = 7*IN
Prop.dAlpha     = 3.95*ARCDEG
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .077/ARCDEG  #- 2D airfoil lift slope
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket
Prop.CDp        = .02          #- Parasitic drag

Prop.Weight     = 67*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None

#
# These are corrected for standard day
#
#Standard correction
STD = STDCorrection(30.05*inHg, (16 + 273.15)*K)

#                 RPM,        Thrust
Prop.ThrustData = [(6330 *RPM, 130*OZF*STD),
                   (6030 *RPM, 111*OZF*STD),
                   (5520 *RPM, 97*OZF*STD),
                   (5020 *RPM, 80*OZF*STD),
                   (4530 *RPM, 61*OZF*STD),
                   (4050 *RPM, 48*OZF*STD),
                   (3570 *RPM, 34*OZF*STD)]

STD2 = STDCorrection(29.90*inHg, (24 + 273.15)*K)
Arm = 19.5*IN*STD2

Prop.TorqueData = [(5910  *RPM, (4.8*Arm*OZF)),
                   (5520  *RPM, (4.1*Arm*OZF)),
                   (5040  *RPM, (3.25*Arm*OZF)),
                   (4470  *RPM, (2.56*Arm*OZF)),
                   (3960  *RPM, (1.9*Arm*OZF)),
                   (3480  *RPM, (1.5*Arm*OZF))]

################################################################################
if __name__ == '__main__':
   
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