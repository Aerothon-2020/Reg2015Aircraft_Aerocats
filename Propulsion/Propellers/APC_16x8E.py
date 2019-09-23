from __future__ import division # let 5/2 = 2.5 rather than 2
from Aerothon.ACPropeller import ACPropeller
from Aerothon.AeroUtil import STDCorrection
import numpy as npy
import pylab as pyl
from scalar.units import IN, LBF, SEC, ARCDEG, FT, RPM, OZF, GRAM, gacc, W, K, degR, inHg, MM
from scalar.units import AsUnit

# Set Propeller properties
Prop = ACPropeller()
Prop.name       = 'APC 16x8E'
Prop.D          = 16*IN
Prop.Thickness  = 5/8*IN

Prop.Pitch      = 8*IN
Prop.dAlpha     = 2.95*ARCDEG
Prop.Solidity   = 0.0126  

Prop.AlphaStall = 20*ARCDEG
Prop.AlphaZeroCL = 0*ARCDEG
Prop.CLSlope    = .0625/ARCDEG  #- 2D airfoil lift slope
Prop.CDCurve    = 2.2          #- 2D curvature of the airfoil drag bucket
Prop.CDp        = .02          #- Parasitic drag

Prop.Weight     = 56*GRAM*gacc

Prop.ThrustUnit = LBF
Prop.ThrustUnitName = 'lbf'
Prop.PowerUnit = W 
Prop.PowerUnitName = 'watt' 
Prop.MaxTipSpeed = None

#
# These are corrected for standard day
#
#Standard correction
STD = STDCorrection(29.74*inHg, (16.1 + 273.15)*K)

#                 RPM,        Thrust
Prop.ThrustData = [(2605 *RPM, 9*OZF*STD),
                   (3071 *RPM, 14*OZF*STD),
                   (3579 *RPM, 21*OZF*STD),
                   (4252 *RPM, 33*OZF*STD),
                   (4927 *RPM, 47*OZF*STD),
                   (5437 *RPM, 61*OZF*STD),
                   (6219 *RPM, 86*OZF*STD)]
#                   (3900 *RPM, 11.25*OZF*STD),
#                   (3720 *RPM, 10.2*OZF*STD),
#                   (3570 *RPM, 9.55*OZF*STD),
#                   (3420 *RPM, 8.8*OZF*STD),
#                   (3210 *RPM, 7.85*OZF*STD),
#                   (3060 *RPM, 7.1*OZF*STD),
#                   
#                   (4170 *RPM, 11.8*OZF*STD),
#                   (3840 *RPM, 10.3*OZF*STD),
#                   (3690 *RPM, 9.65*OZF*STD),
#                   (3570 *RPM, 9.1*OZF*STD),
#                   (3480 *RPM, 8.5*OZF*STD),
#                   (3240 *RPM, 7.1*OZF*STD),
#                   (2730 *RPM, 5.2*OZF*STD)]

STD2 = STDCorrection(29.93*inHg, (28.3 + 273.15)*K)
Arm = 19.5*IN*STD2

#                   RPM,        Torque
Prop.TorqueData = [(6960 *RPM, 5.7*OZF*Arm),
                   (6360 *RPM, 4.9*OZF*Arm),
                   (6030 *RPM, 4.2*OZF*Arm),
                   (5490 *RPM, 3.4*OZF*Arm),
                   (5040 *RPM, 2.8*OZF*Arm),
                   (4410 *RPM, 2.1*OZF*Arm),
                   (3900 *RPM, 1.6*OZF*Arm),
                   (3480 *RPM, 1.2*OZF*Arm)]
#                   (3750 *RPM, 27*GRAM*Arm),
#                   (3600 *RPM, 24.5*GRAM*Arm),
#                   (3510 *RPM, 23*GRAM*Arm),
#                   (3420 *RPM, 21*GRAM*Arm),
#                   (3210 *RPM, 19*GRAM*Arm),
#                   (3000 *RPM, 16*GRAM*Arm),
#                   
#                   (4020 *RPM, 30*GRAM*Arm),
#                   (3750 *RPM, 26*GRAM*Arm),
#                   (3600 *RPM, 24.5*GRAM*Arm),
#                   (3480 *RPM, 23*GRAM*Arm),
#                   (3300 *RPM, 20*GRAM*Arm),
#                   (3180 *RPM, 16.5*GRAM*Arm),
#                   (3000 *RPM, 14*GRAM*Arm)]

#Standard correction
# STD = STDCorrection(30.05*inHg, (18.2 + 273.15)*K)

#                 RPM,        Thrust
# Prop.ThrustData += [(4530 *RPM, 16.2*OZF*STD)]
#                    (4950 *RPM, 18.5*OZF*STD),
#                    (5220 *RPM, 21*OZF*STD),
#                    (6030 *RPM, 30*OZF*STD),
#                    (5610 *RPM, 25.5*OZF*STD),
#                    
#                    (6390 *RPM, 35*OZF*STD),
#                    (4470 *RPM, 16*OZF*STD),
#                    (4800 *RPM, 18*OZF*STD),
#                    (4830 *RPM, 19*OZF*STD),
#                    (5310 *RPM, 23*OZF*STD),
#                    (5520 *RPM, 24*OZF*STD)]

#                   RPM,        Torque
# Prop.TorqueData += [(4680 *RPM, 40*GRAM*Arm)]
#                   (4890 *RPM, 43*GRAM*Arm),
#                   (6150 *RPM, 80*GRAM*Arm),
#                   (5220 *RPM, 50*GRAM*Arm),
#                   (5610 *RPM, 59*GRAM*Arm),
#                   (6060 *RPM, 67*GRAM*Arm),
#                   (5400 *RPM, 55*GRAM*Arm),
#                   (5820 *RPM, 64*GRAM*Arm)]

################################################################################
if __name__ == '__main__':
   
#     print "##################"
#     print " This test data is not for this propeller!!!!!"
#     print "##################"

    print " D     : ", AsUnit( Prop.D, 'in')
    print " Pitch : ", AsUnit( Prop.Pitch, 'in')
    
    Vmax = 50
    h=0*FT
    N=npy.linspace(1000, 5600, 5)*RPM
    
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

    N = 6219*RPM
    print
    print "Static Thrust   : ", AsUnit( Prop.T(N, 0*FT/SEC, h), 'lbf' )
    print "Measured Thrust : ", AsUnit( max(npy.array(Prop.ThrustData)[:,1]), 'lbf' )
    N = 5822*RPM
    print
    print "Static Torque   : ", AsUnit( Prop.P(N, 0*FT/SEC, h)/N, 'in*ozf' )
    print "Measured Torque : ", AsUnit( max(npy.array(Prop.TorqueData)[:,1]), 'in*ozf' )
    
    pyl.show() 