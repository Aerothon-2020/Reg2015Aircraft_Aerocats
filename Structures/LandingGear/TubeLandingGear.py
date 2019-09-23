from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, PSI, LBF, GRAM, gacc, AsUnit, MPa, KG, M, MM
from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
import pylab as pyl
import numpy as npy
from cmath import pi


MainGear = Aircraft.MainGear
L = MainGear.StrutL

# Gload factor
GLoad = 5

#Do the analysis for one wheel in case one wheel hits before the other
Load = GLoad*Aircraft.TotalWeight

M = Load*L

# Moment of inertia for a tube
# I = 1/4*pi*(ro**4 - ri**4)
# where ro and ri are outer and inner radius of the tube.
# Solving for ri
# ri = (ro**4 - 4*I/pi)**(1/4)
#
# Bending stress
# sig = M*ro/I
# thus
# I = M*ro/sig

ro = npy.linspace(5, 15, 61)*MM
sig = 276*MPa #Maximum yield stress for aluminum 6061-T651
I = M*ro/sig

ri = (ro**4 - 4*I/pi)**(1/4)

print "ro : ", AsUnit(ro, 'mm')
print "ri : ", AsUnit(ri, 'mm')
print "t  : ", AsUnit(ro-ri, 'mm')

#Available tube sizes
#ro_A = npy.array([19 ,  19,  22,  26])/2*MM
#ri_A = npy.array([.630, .610, 0.787, 0.846])/2*IN

ro_A = npy.array([0.748, 0.748, 0.866, 1.024, 1/2, 1/4, 3/8, 1, 3/8, 1, 5/16, 3/8])/2*IN
ri_A = npy.array([0.630, 0.610, 0.787, 0.846, 0.402, 0.18, 0.305, 0.902, 0.305, 0.93, 0.215, 0.245])/2*IN

design_ro = npy.array([0.748])*IN/2
design_ri = npy.array([0.610])*IN/2

pyl.plot(ro*2/MM, ri*2/MM, 'k')
pyl.xlabel(r"O. D. (mm)"); pyl.ylabel(r"I. D. (mm)")
pyl.plot(ro_A*2/MM, ri_A*2/MM, 'ko')
pyl.plot(design_ro*2/MM, design_ri*2/MM, 'ro')
pyl.gca().xaxis.set_label_coords(0.5,-0.05)
pyl.gca().yaxis.set_label_coords(-0.06,0.5)
pyl.legend(["Max Inner Radius", "Available Tubes", "Selected"], numpoints=1, loc='best')
pyl.grid()

pyl.show()