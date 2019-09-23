from __future__ import division # let 5/2 = 2.5 rather than 2

#from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACPropulsion import ACPropulsion
from Motors.Hacker_A50_14L_model2 import Motor
from Propellers.APC_20x8E import Prop
from Batteries.Turnigy_6Cell_3000 import Turnigy_6Cell_3000 as Battery
from SpeedControllers.Phoenix import Phoenix100
import numpy as npy
from scalar.units import IN, LBF, PSFC, SEC, ARCDEG, FT, OZF, RPM, HP, inHg
from scalar.units import AsUnit

#ADDED
Motor.Battery = Battery
Motor.SpeedController = Phoenix100

Motor.Battery.WeightGroup = 'Electronics'
Motor.SpeedController.WeightGroup = 'Electronics'

Motor.WeightGroup = "Propulsion"
Prop.WeightGroup = "Propulsion"

# Set Propulsion properties
Propulsion = ACPropulsion(Prop,Motor)
Propulsion.Alt  = 0*FT
Propulsion.Vmax =70*FT/SEC
Propulsion.nV   = 20

if __name__ == '__main__':
    import pylab as pyl
   
    print "Static Thrust :", AsUnit( Propulsion.T(0*FT/SEC), "lbf")
    
    Vmax = 70
    V = npy.linspace(0,Vmax,30)*FT/SEC
    Vprop = npy.linspace(0,Vmax,5)*FT/SEC
    N = npy.linspace(1000,20000,30)*RPM
    Propulsion.PlotMatched(V, N, Vprop, fig = 1 )
    #Propulsion.PlotTPvsN(N, Vprop, fig=2)
    Propulsion.PlotTestData(fig=3)
    
    Propulsion.Draw(fig=4)
    
    pyl.show()
    