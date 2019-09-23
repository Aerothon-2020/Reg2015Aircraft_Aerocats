import numpy as npy
import pylab as pyl
from Aerothon.ACPropulsion import ACPropulsion
from scalar.units import SEC, FT, RPM, A, mAh, W, MIN, OHM
from scalar.units import AsUnit
from scalar.units import V as Volt

# IMPORT MOTORS
from Motors.Hacker_A50_14L_model2 import Motor as Hacker_A50_14L
from Motors.Hacker_A60_7XS_model2 import Motor as Hacker_A60_7XS
#IMPORT PROP
from Propellers.APC_19x10E import Prop
#IMPORT Battery
from Batteries.Turnigy_6Cell_3000 import Turnigy_6Cell_3000

Alt  = 0*FT
Vmax = 50*FT/SEC
nV   = 20

V = npy.linspace(0, Vmax / (FT/SEC), 30)*FT/SEC

Propulsion = []
legend = []

#IMPORT PLOTS
Propulsion += [ACPropulsion(Prop,Hacker_A50_14L)] ; legend += ['Hacker_A50_14L']
Propulsion += [ACPropulsion(Prop,Hacker_A60_7XS)] ; legend += ['Hacker_A60_7XS']

Nmax = 0
for pp in Propulsion:
    #pp.Engine.Vb = 11.1*Volt
    #pp.Engine.Cb = 325*mAh
    
    pp.Engine.Battery = Turnigy_6Cell_3000

    Nmax = max(pp.Engine.Nmax/RPM, Nmax)
    
V = npy.linspace(0,Vmax/(FT/SEC),30)*FT/SEC
Vprop = npy.linspace(0,Vmax/(FT/SEC),5)*FT/SEC
N = npy.linspace(0, Nmax, 30)*RPM

for pp in Propulsion:
        
    pp.Alt  = Alt
    pp.Vmax = Vmax
    pp.nV   = nV
    
    PlotProp = False
    
    if pp == Propulsion[-1]:
        PlotProp = True
    
    pp.PlotMatched(V, N, Vprop, fig = 1, PlotProp=PlotProp )
    pp.Engine.PlotProperties(fig = 3)
    
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

    print pp.Engine.name, ' : ', AsUnit( pp.Weight, 'lbf' )

pyl.figure(1)
pyl.subplot(223)
pyl.legend(legend, loc='best')
pyl.figure(2)
pyl.subplot(221)
pyl.legend(legend, loc='best')
pyl.title( Propulsion[-1].Engine.name + ', ' + Propulsion[-1].Prop.name )


pyl.show()