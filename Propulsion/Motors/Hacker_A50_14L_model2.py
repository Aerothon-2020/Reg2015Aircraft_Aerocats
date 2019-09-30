from __future__ import division # let 5/2 = 2.5 rather than 2

# Optimum Prop None
from Aerothon.ACMotor import ACMotor
import numpy as npy
import cmath as math
from scalar.units import MM, IN, OZF, RPM, HP, V, A, OHM, GRAM, gacc, mAh, W, LBF, inHg, K
from scalar.units import AsUnit
from Aerothon.AeroUtil import STDCorrection
#from Aircraft_Models.Reg2015Aircraft_AeroCats.Propulsion.Batteries.Turnigy_6Cell_3000 import Turnigy_6Cell_3000
from Reg2015Aircraft_Aerocats.Propulsion.Batteries.Turnigy_6Cell_3000 import Turnigy_6Cell_3000

# Set Motor properties
Motor  = ACMotor()
Motor.name = 'Hacker_A50_14L'
Motor.Battery = Turnigy_6Cell_3000
#Manufacturer Data
# Motor.Ri  = 0.025*OHM        #Coil resistance
# Motor.Io  = 1*A          #Idle current
# Motor.Kv  = 300*RPM/V      #RPM/Voltage ratio
#Matched data - Model 1
# Motor.Ri = .12*OHM
# Motor.Io = .5*A
# Motor.Kv  = 355*RPM/V

#Matched data - Model 2
Motor.Ri =.077*OHM #.09
Motor.Io = 1.5*A
Motor.Kv  = 310*RPM/V #320

Motor.Vmax = 23.5*V
Motor.Imax = 55*A
Motor.ThrustUnit = LBF
Motor.ThrustUnitName = 'lbf'

Motor.xRm =  100000
Motor.Pz  = 0.0

Motor.Weight = 445*GRAM*gacc
Motor.LenDi = [46.8*MM, 59.98*MM]

#
# This data has been corrected for standard day
STD = STDCorrection( 29.9*inHg, (23.9  +273.15)*K )
STD2 = STDCorrection( 30.32*inHg, (5  +273.15)*K ) #1/14/2015
Arm=19.5*IN
#            RPM,        Torque     Current   Voltage
TestData = [(6210  *RPM, (7.5*Arm*OZF)*STD,    34.8*A,    23.0*V),
            (5910  *RPM, (8.7*Arm*OZF)*STD,    39.0*A,    21.9*V),
            (5610  *RPM, (9.9*Arm*OZF)*STD,    44.2*A,    21.5*V),
            (5640  *RPM, (9.3*Arm*OZF)*STD,    40.5*A,    21.4*V),
            (5640  *RPM, (11.9*Arm*OZF)*STD,    48.2*A,    21.5*V),
            (6034  *RPM, (8.9*Arm*OZF)*STD,    35.8*A,    22.06*V),
            (5802  *RPM, (11.1*Arm*OZF)*STD,    45.2*A,    21.9*V)] #this is actual test data from a test stand




Motor.TestData = TestData

if __name__ == '__main__':
    import pylab as pyl
    
    print "V to Motor : ", AsUnit( Motor.Vmotor(Ib=45*A), 'V' )
    print "Efficiency : ", Motor.Efficiency(Ib=45*A)
    print "Max efficiency : ", Motor.Effmax()
    print "Max efficiency current : ", AsUnit( Motor.I_Effmax(), 'A' )
    print "Max efficiency RPM : ", AsUnit( Motor.N_Effmax(), 'rpm' )
    
    Motor.PlotTestData()
    
    pyl.show()