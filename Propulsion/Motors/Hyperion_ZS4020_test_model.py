from __future__ import division # let 5/2 = 2.5 rather than 2

# Optimum Prop None
from Aerothon.ACMotor import ACMotor
import numpy as npy
import cmath as math
from Aerothon.AeroUtil import STDCorrection
from Aircraft_Models.Reg2014Aircraft_AeroCats.Propulsion.Batteries.ThunderPower_4Cell_5000 import ThunderPower_4Cell_5000
from scalar.units import MM, IN, K, inHg, OZF, RPM, HP, V, A, OHM, GRAM, gacc, mAh, W, LBF
from scalar.units import AsUnit


# Set Motor properties
Motor  = ACMotor()
Motor.name = 'Hyperion_ZS4020'
Motor.Battery = ThunderPower_4Cell_5000
Motor.Ri  = 0.058*OHM        #Coil resistance
Motor.Io  = 1.4*A          #Idle current
Motor.Kv  = 585*RPM/V      #RPM/Voltage ratio
Motor.Vmax = 25.9*V 
Motor.Imax = 85*A
Motor.ThrustUnit = LBF
Motor.ThrustUnitName = 'lbf'

Motor.xRm = 1000000 
Motor.Pz  = 0.0 

Motor.Weight = 304*GRAM*gacc
Motor.LenDi = [60.2*MM, 48.9*MM] 
Arm=10.5*IN
Arm2=19.5*IN
#
# This data has been corrected for standard day
#
#            RPM,        Torque     Current   Voltage
STD = STDCorrection(30.29*inHg, (9.4 + 273.15)*K)
STD2 = STDCorrection(30.29*inHg, (9.8 + 273.15)*K)
STD3 = STDCorrection(30.25*inHg, (12 + 273.15)*K)
STD4 = STDCorrection(30.2*inHg, (6.667 + 273.15)*K)
STD5 = STDCorrection(30.31*inHg, (-9 + 273.15)*K)
TestData = [(6759  *RPM, (11.1*Arm*OZF)*STD,    53.62*A,    14.8*V),
            (7097  *RPM, (9.8*Arm*OZF)*STD,    42.7*A,    14.8*V),
            (6973  *RPM, (12.35*Arm*OZF)*STD,    54.51*A,    14.8*V),
            (7104  *RPM, (9.78*Arm*OZF)*STD,    43.18*A,    14.8*V),
            (7034  *RPM, (10.99*Arm*OZF)*STD2,    47.68*A,    14.8*V),
            (7166  *RPM, (9.29*Arm*OZF)*STD2,    40.30*A,    14.8*V),
            (6825  *RPM, (11.76*Arm*OZF)*STD2,    51.33*A,    14.8*V),
            (7086  *RPM, (9.41*Arm*OZF)*STD2,    41.61*A,    14.8*V),
            (6776  *RPM, (7.98*Arm2*OZF)*STD3,    63.11*A,    14.8*V),
            (5592  *RPM, (11.0*Arm2*OZF)*STD3,    72.56*A,    14.8*V),
            (5753  *RPM, (9.90*Arm2*OZF)*STD3,    74.31*A,    14.8*V),
            (5590  *RPM, (11.0*Arm2*OZF)*STD4,    77.50*A,    14.8*V),
            (6680  *RPM, (10.45*Arm2*OZF)*STD5,    72.8*A,     13.9*V),
            (6473  *RPM, (10.75*Arm2*OZF)*STD5,    73.9*A,     14.5*V),
            (6092  *RPM, (12.05*Arm2*OZF)*STD5,    87.4*A,     14.5*V),
            (5497  *RPM, (11.30*Arm2*OZF)*STD5,    76.9*A,     14.2*V),]
            
             #this is actual test data from a test stand

Motor.TestData = TestData

if __name__ == '__main__':
    import pylab as pyl
    
    print "V to Motor : ", AsUnit( Motor.Vmotor(Ib=3.75*A), 'V' )
    print "Efficiency : ", Motor.Efficiency(Ib=3.75*A)
    print "Max efficiency : ", Motor.Effmax()
    print "Max efficiency current : ", AsUnit( Motor.I_Effmax(), 'A' )
    print "Max efficiency RPM : ", AsUnit( Motor.N_Effmax(), 'rpm' )
    
    Motor.PlotTestData()

    pyl.show()