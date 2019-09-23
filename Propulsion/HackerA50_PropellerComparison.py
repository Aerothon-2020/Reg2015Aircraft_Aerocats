import numpy as npy
import pylab as pyl
from scalar.units import AsUnit
from Aerothon.ACPropulsion import ACPropulsion
from scalar.units import SEC, FT, V, A, MIN, W, mAh, gacc

#### Import Motors ####
from Motors.Hacker_A50_14L_model2 import Motor as Motor

##### Import Propellers for Comparison ####
# from Propellers.APC_18x8E import Prop as APC_18x8E
from Propellers.APC_18x10E import Prop as APC_18x10E
from Propellers.APC_18x10E_mod import Prop as APC_18x10E_mod
# from Propellers.APC_19x8E import Prop as APC_19x8E
# from Propellers.APC_18_25x10E import Prop as APC_18_25x10E
# from Propellers.APC_18_5x10E import Prop as APC_18_5x10E
# from Propellers.APC_18_75x10E import Prop as APC_18_75x10E
from Propellers.APC_19x10E import Prop as APC_19x10E
# 20x6 wood will be here
from Propellers.APC_20x8E import Prop as APC_20x8E

##### Import Battery ####
from Aircraft_Models.Reg2015Aircraft_AeroCats.Propulsion.Batteries.Turnigy_6Cell_3000 import Turnigy_6Cell_3000

Motor.Battery = Turnigy_6Cell_3000

Alt  = 0*FT
Vmax = 60*FT/SEC
nV   = 20

Propulsion = []
legend = []

#Propulsion += [ACPropulsion(APC_18x8E, Motor)]
Propulsion += [ACPropulsion(APC_18x10E, Motor)]
# Propulsion += [ACPropulsion(APC_18x10E_mod, Motor)]
#Propulsion += [ACPropulsion(APC_19x8E, Motor)]
#Propulsion += [ACPropulsion(APC_18_25x10E, Motor)]
#Propulsion += [ACPropulsion(APC_18_5x10E, Motor)]
#Propulsion += [ACPropulsion(APC_18_75x10E, Motor)]
Propulsion += [ACPropulsion(APC_19x10E, Motor)]
#Propulsion += [ACPropulsion(APC_19x10E_base, Motor)]
Propulsion += [ACPropulsion(APC_20x8E, Motor)]

#### PLOT CREATION ####
V = npy.linspace(0,Vmax/(FT/SEC),30)*FT/SEC
Vprop = npy.linspace(0,Vmax/(FT/SEC),1)*FT/SEC
N = Motor.NRange()

for pp in Propulsion:
    pp.Alt  = Alt
    pp.Vmax = Vmax
    pp.nV   = nV
    
    legend.append(pp.Prop.name)

    pp.PlotMatched(V, N, Vprop, fig = 1 )
    pp.PlotTestData(fig = 3)
    
    Nm = pp.RPMMatch(V)
    Ib = pp.Engine.Ib(Nm)/A
    
    pyl.figure(2)
    pyl.subplot(221)
    pyl.plot(V/(FT/SEC), Ib)
    pyl.xlabel('V (ft/s)'); pyl.ylabel('Current (A)') 
    pyl.subplot(222)
    pyl.plot(V/(FT/SEC), pp.Engine.Duration(N=Nm)/MIN)
    pyl.xlabel('V (ft/s)'); pyl.ylabel('Duration (min)')

    pyl.subplot(223)
    pyl.plot(V/(FT/SEC), pp.Engine.Pin(Nm)/W)
    pyl.xlabel('V (ft/s)'); pyl.ylabel('Power In (watt)') 
    pyl.subplot(224)
    pyl.plot(V/(FT/SEC), pp.Engine.Efficiency(Nm))
    pyl.xlabel('V (ft/s)'); pyl.ylabel('Efficiency (%)') 
     
for pp in Propulsion:
    print pp.Prop.name + " Static Thrust : ", AsUnit( pp.T( 0*FT/SEC ), 'lbf' ), ' : Weight : ', AsUnit(pp.Weight/gacc, 'g')


pyl.figure(2)
pyl.subplot(223)
pyl.plot([0, max(V/(FT/SEC))], [Motor.Wmax/W,Motor.Wmax/W], 'r-.', linewidth=2 )

pyl.figure(1)
pyl.subplot(223)
pyl.legend(legend, loc='best')
pyl.figure(2)
pyl.subplot(221)
pyl.legend(legend, loc='best')
pyl.title( Propulsion[-1].Engine.name + ', ' + Propulsion[-1].Prop.name )

pyl.show()