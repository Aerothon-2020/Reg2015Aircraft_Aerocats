from __future__ import division # let 5/2 = 2.5 rather than 2

# Optimum Prop None
from Aerothon.ACMotor import ACMotor
import numpy as npy
import cmath as math
from scalar.units import MM, IN, OZF, RPM, HP, V, A, OHM, GRAM, gacc, mAh, W, LBF, inHg, K
from scalar.units import AsUnit
from Aerothon.AeroUtil import STDCorrection
from Aircraft_Models.Reg2015Aircraft_AeroCats.Propulsion.Batteries.Turnigy_6Cell_3000 import Turnigy_6Cell_3000


# Set Motor properties
Motor  = ACMotor()
Motor.name = 'Hacker_A60_7XS'
Motor.Battery = Turnigy_6Cell_3000
#Manufacturer Data
# Motor.Ri  = 0.02*OHM        #Coil resistance
# Motor.Io  = 1.5*A          #Idle current
# Motor.Kv  = 320*RPM/V      #RPM/Voltage ratio
#Matched Data
Motor.Ri  = 0.16*OHM #.15
Motor.Io  = .5*A #1.5
Motor.Kv  = 380*RPM/V #370
#
Motor.Vmax = 23.5*V
Motor.Imax = 55*A
Motor.ThrustUnit = LBF
Motor.ThrustUnitName = 'lbf'

Motor.xRm =  100000
Motor.Pz  = 0.0

Motor.Weight = 480*GRAM*gacc
Motor.LenDi = [46.8*MM, 59.98*MM]

#
# This data has been corrected for standard day
STD = STDCorrection( 30.2*inHg, (16.1+273.15)*K )
Arm=19.5*IN
#            RPM,        Torque     Current   Voltage
TestData = [(6030  *RPM, (7.3*Arm*OZF)*STD,    32.0*A,    22.8*V),
            (5670  *RPM, (8.3*Arm*OZF)*STD,    36.0*A,    22.2*V),
            (5430  *RPM, (9.3*Arm*OZF)*STD,    39.5*A,    21.5*V),
            (5340  *RPM, (9.0*Arm*OZF)*STD,    38.7*A,    21.1*V),
            (5370  *RPM, (8.3*Arm*OZF)*STD,    35.3*A,    20.9*V)] #this is actual test data from a test stand

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