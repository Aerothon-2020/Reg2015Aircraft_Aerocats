from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import LBF
from Aircraft_Models.Reg2015Aircraft_AeroCats.MonoWing.Aircraft import Aircraft

#Get maximum score of lift two pounds more than predicted
#Aircraft.TotalWeight = Aircraft.TotalWeight - 2*LBF

TW = Aircraft.TotalWeight
EW = Aircraft.EmptyWeight
h  = Aircraft.Wing.Alt_LO

Aircraft.PlotWeightPrediction(TeamName = "AeroCats", 
                              TeamNumber = 4, 
                              fig=1, 
                              TotalWeight = 38*LBF, 
                              EmptyWeight = 8.1*LBF, 
                              h = h, 
                              ShowDesign = True)

pyl.show()
