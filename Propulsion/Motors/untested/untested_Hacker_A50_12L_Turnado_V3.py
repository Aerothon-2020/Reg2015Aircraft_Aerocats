from __future__ import division # let 5/2 = 2.5 rather than 2

# Optimum Prop None
from Aerothon.ACMotor import ACMotor
import numpy as npy
import cmath as math
from Aircraft_Models.Reg2014Aircraft_AeroCats.Propulsion.Batteries.ThunderPower_4Cell_4400 import ThunderPower_4Cell_4400
from scalar.units import MM, IN, OZF, RPM, HP, V, A, OHM, GRAM, gacc, mAh, W, LBF
from scalar.units import AsUnit


# Set Motor properties
Motor  = ACMotor()
Motor.name = 'Hacker_A50_12L_Turnado_V3'
Motor.Battery = ThunderPower_4Cell_4400
Motor.Ri  = 0.019*OHM        #Coil resistance
Motor.Io  = 1.2*A          #Idle current
Motor.Kv  = 450*RPM/V      #RPM/Voltage ratio
Motor.Vmax = 23.5*V
Motor.Imax = 55*A
Motor.ThrustUnit = LBF
Motor.ThrustUnitName = 'lbf'

Motor.xRm =  100000
Motor.Pz  = 0.0

Motor.Weight = 455*GRAM*gacc
Motor.LenDi = [46.8*MM, 59.98*MM]

#
# This data has been corrected for standard day
#
#            RPM,        Torque     Current   Voltage
TestData = [(5500  *RPM, 7*IN*OZF,    9*A,    6.4*V)] #this is actual test data from a test stand

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