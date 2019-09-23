import numpy as npy
import pylab as pyl
from Aerothon.ACPropulsion import ACPropulsion
from scalar.units import SEC, FT, RPM, A, mAh, W, MIN, OHM
from scalar.units import AsUnit
from scalar.units import V as Volt

# IMPORT MOTORS
from Motors.untested_AXI_4120_18 import Motor as AXI_4120_18
from Motors.untested_AXI_4120_20 import Motor as AXI_4120_20
from Motors.untested_AXI_4130_16 import Motor as AXI_4130_16
from Motors.untested_AXI_4130_20 import Motor as AXI_4130_20
from Motors.untested_AXI_5320_18 import Motor as AXI_5320_18
from Motors.untested_AXI_5325_16 import Motor as AXI_5325_16
from Motors.untested_AXI_5325_18 import Motor as AXI_5325_18

from Motors.untested_Hacker_A40_12L_14 import Motor as Hacker_A40_12L_14
from Motors.untested_Hacker_A40_14L_14 import Motor as Hacker_A40_14L_14
from Motors.untested_Hacker_A50_12L_Turnado_V3 import Motor as Hacker_A50_12L_Turnado_V3
from Motors.untested_Hacker_A50_12L import Motor as Hacker_A50_12L
from Motors.untested_Hacker_A50_12S import Motor as Hacker_A50_12S
from Motors.untested_Hacker_A50_14L import Motor as Hacker_A50_14L
from Motors.untested_Hacker_A50_14L_Turnado import Motor as Hacker_A50_14L_Turnado
from Motors.untested_Hacker_A50_14XS import Motor as Hacker_A50_14XS
from Motors.untested_Hacker_A50_16S import Motor as Hacker_A50_16S
from Motors.untested_Hacker_A50_16L import Motor as Hacker_A50_16L
from Motors.untested_Hacker_A50L_Turnado import Motor as Hacker_A50L_Turnado
from Motors.untested_Hacker_A60_20S import Motor as Hacker_A60_20S
from Motors.untested_Hacker_A60_5S import Motor as Hacker_A60_5S
from Motors.untested_Hacker_A60_5XS28 import Motor as Hacker_A60_5XS28
from Motors.untested_Hacker_A60_6XS28 import Motor as Hacker_A60_6XS28
from Motors.untested_Hacker_A60_7S import Motor as Hacker_A60_7S
from Motors.untested_Hacker_A60_7XS import Motor as Hacker_A60_7XS

from Motors.untested_Hyperion_ZS4025_14 import Motor as Hyperion_ZS4025_14
from Motors.untested_Hyperion_ZS4025_16 import Motor as Hyperion_ZS4025_16
from Motors.untested_Hyperion_ZS4035_10 import Motor as Hyperion_ZS4035_10
from Motors.untested_Hyperion_ZS4035_12 import Motor as Hyperion_ZS4035_12
from Motors.untested_Hyperion_ZS4045_10 import Motor as Hyperion_ZS4045_10
from Motors.untested_Hyperion_ZS4045_12 import Motor as Hyperion_ZS4045_12

from Motors.untested_OS_OSMG9540 import Motor as OS_OSMG9540
from Motors.untested_OS_OSMG9550 import Motor as OS_OSMG9550

from Motors.untested_Scorpion_HKIII_5035_380 import Motor as Scorpion_HKIII_5035_380
from Motors.untested_Scorpion_HKIII_5035_330 import Motor as Scorpion_HKIII_5035_330
from Motors.untested_Scorpion_SII_4020_420 import Motor as Scorpion_SII_4020_420
from Motors.untested_Scorpion_SII_4020_630 import Motor as Scorpion_SII_4020_630
from Motors.untested_Scorpion_SII_4025_250 import Motor as Scorpion_SII_4025_250
from Motors.untested_Scorpion_SII_4025_330 import Motor as Scorpion_SII_4025_330
from Motors.untested_Scorpion_SII_4025_440 import Motor as Scorpion_SII_4025_440

#IMPORT PROP
from Propellers.untested_APC_22x8E import Prop
#IMPORT Battery
from Batteries.ThunderPower_4Cell_4400 import ThunderPower_4Cell_4400

Alt  = 0*FT
Vmax = 70*FT/SEC
nV   = 20

V = npy.linspace(0, Vmax / (FT/SEC), 30)*FT/SEC

Propulsion = []
legend = []

#IMPORT PLOTS
# Propulsion += [ACPropulsion(Prop,AXI_4120_18)] ; legend += ['AXI_4120_18']
# Propulsion += [ACPropulsion(Prop,AXI_4120_20)] ; legend += ['AXI_4120_20']
# Propulsion += [ACPropulsion(Prop,AXI_4130_16)] ; legend += ['AXI_4130_16']
# Propulsion += [ACPropulsion(Prop,AXI_4130_20)] ; legend += ['AXI_4130_20']
# Propulsion += [ACPropulsion(Prop,AXI_5320_18)] ; legend += ['AXI_5320_18']
# Propulsion += [ACPropulsion(Prop,AXI_5325_16)] ; legend += ['AXI_5325_16']
# Propulsion += [ACPropulsion(Prop,AXI_5325_18)] ; legend += ['AXI_5325_18']


# Propulsion += [ACPropulsion(Prop,Hacker_A40_12L_14)] ; legend += ['Hacker_A40_12L_14']
# Propulsion += [ACPropulsion(Prop,Hacker_A40_14L_14)] ; legend += ['Hacker_A40_14L_14']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_12L_Turnado_V3)] ; legend += ['Hacker_A50_12L_Turnado_V3']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_12L)] ; legend += ['Hacker_A50_12L']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_12S)] ; legend += ['Hacker_A50_12S']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_14L_Turnado)] ; legend += ['Hacker_A50_14L_Turnado']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_14L)] ; legend += ['Hacker_A50_14L']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_14XS)] ; legend += ['Hacker_A50_14XS']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_16L)] ; legend += ['Hacker_A50_16L']
# Propulsion += [ACPropulsion(Prop,Hacker_A50_16S)] ; legend += ['Hacker_A50_16S']
# Propulsion += [ACPropulsion(Prop,Hacker_A50L_Turnado)] ; legend += ['Hacker_A50L_Turnado']
Propulsion += [ACPropulsion(Prop,Hacker_A60_20S)] ; legend += ['Hacker_A60_20S']
# Propulsion += [ACPropulsion(Prop,Hacker_A60_5S)] ; legend += ['Hacker_A60_5S']
# Propulsion += [ACPropulsion(Prop,Hacker_A60_5XS28)] ; legend += ['Hacker_A60_5XS28']
# Propulsion += [ACPropulsion(Prop,Hacker_A60_6XS28)] ; legend += ['Hacker_A60_6XS28']
Propulsion += [ACPropulsion(Prop,Hacker_A60_7S)] ; legend += ['Hacker_A60_7S']
# Propulsion += [ACPropulsion(Prop,Hacker_A60_7XS)] ; legend += ['Hacker_A60_7XS']

# Propulsion += [ACPropulsion(Prop,Hyperion_ZS4025_14)] ; legend += ['Hyperion_ZS4025_14']
# Propulsion += [ACPropulsion(Prop,Hyperion_ZS4025_16)] ; legend += ['Hyperion_ZS4025_16']
# Propulsion += [ACPropulsion(Prop,Hyperion_ZS4035_10)] ; legend += ['Hyperion_ZS4035_10']
# Propulsion += [ACPropulsion(Prop,Hyperion_ZS4035_12)] ; legend += ['Hyperion_ZS4035_12']
# Propulsion += [ACPropulsion(Prop,Hyperion_ZS4045_10)] ; legend += ['Hyperion_ZS4045_10']
Propulsion += [ACPropulsion(Prop,Hyperion_ZS4045_12)] ; legend += ['Hyperion_ZS4045_12']

# Propulsion += [ACPropulsion(Prop,OS_OSMG9540)] ; legend += ['OS_OSMG9540']
# Propulsion += [ACPropulsion(Prop,OS_OSMG9550)] ; legend += ['OS_OSMG9550']

# Propulsion += [ACPropulsion(Prop,Scorpion_HKIII_5035_380)]  ; legend +=['Scorpion_HKIII_5035_380']
# Propulsion += [ACPropulsion(Prop,Scorpion_HKIII_5035_330)]  ; legend +=['Scorpion_HKIII_5035_330']
# Propulsion += [ACPropulsion(Prop,Scorpion_SII_4020_420)]  ; legend +=['Scorpion_SII_4020_420']
# Propulsion += [ACPropulsion(Prop,Scorpion_SII_4020_630)]  ; legend +=['Scorpion_SII_4020_630']
Propulsion += [ACPropulsion(Prop,Scorpion_SII_4025_250)]  ; legend +=['Scorpion_SII_4025_250']
# Propulsion += [ACPropulsion(Prop,Scorpion_SII_4025_330)]  ; legend +=['Scorpion_SII_4025_330']
# Propulsion += [ACPropulsion(Prop,Scorpion_SII_4025_440)]  ; legend +=['Scorpion_SII_4025_440']


Nmax = 0
for pp in Propulsion:
    #pp.Engine.Vb = 11.1*Volt
    #pp.Engine.Cb = 325*mAh
    
    pp.Engine.Battery = ThunderPower_4Cell_4400

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