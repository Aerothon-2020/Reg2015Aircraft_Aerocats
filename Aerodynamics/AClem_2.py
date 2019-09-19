from os import environ as _environ; _environ["scalar_off"] = "off"

from Aerothon.ACControls import ACControls
from Aerothon import AeroUtil
#from Aircraft_Models.Reg2014Aircraft_AeroCats.TradeStudies.WeightTrade.Aircraft_NickSchwartz import Aircraft
from Aircraft_Models.Reg2015Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
from scalar.units import SEC, ARCDEG, LBF, IN, FT
from scalar.units import AsUnit
import pylab as pyl
import numpy as npy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


print 'Ground Roll    : ', AsUnit(Aircraft.Groundroll(),  'ft')
print 'Total Weight   : ', AsUnit(Aircraft.TotalWeight,   'lbf')
print 'Payload Weight  : ', AsUnit(Aircraft.PayloadWeight(), 'lbf')



# Wing = Aircraft.Wing
# Wing.b = 100.0*IN
# y = npy.linspace(-Wing.b/2/IN, Wing.b/2/IN, 121.0)*IN
# 
# legend = [];
# 
# TRs = npy.linspace(0.35,0.35,1) #Taper ratio beginning at Fb's location. 0.385 at FB =0.45 is most even
# Fbs = npy.linspace(0.65,0.65,1) #0.2 0.9 8Distance from root chord in % of 1/2 span the taper ratio begins
# #TR is 0.71, Fb = 0.5 <--First round through
# #TR is 0.50, Fb is 0.3 <--Second round through
# Wing.Lam = [0*ARCDEG,0*ARCDEG] #Sweep angle-1st is sweep from root, 2nd is sweep from Fb location
# Wing.Gam = [0*ARCDEG,0*ARCDEG]
# for Fb in Fbs:
#     Aircraft.Wing.Fb = [Fb,1.0]
#     for TR in TRs:
#         Aircraft.Wing.TR = [1.0,TR]
#         Aircraft.Wing.Draw(fig = 2)
#         LLT = Aircraft.Wing.LLT
#         #Aircraft.Wing.Draw(fig = 2)
#         pyl.figure(1)
#         pyl.plot(y/IN,LLT.Cl(y))
#         pyl.title("Cl Across Span")
#         pyl.xlabel("y (in)")
#         pyl.ylabel('Cl')
# 
#         legend.append("Fb = " + str(Fb) + ", TR = " + str(TR))
#         
#         pyl.legend(legend, loc = 1)
#         pyl.plt.grid(True)
#         pyl.plt.ylim(0,1.8)
#        
#         #pyl.figure()
#         #pyl.scatter(Wing.Chord(0*FT),npy.max(LLT.CL()))
# #        pyl.figure(2)
#         #pyl.plot(y/IN,LLT.Cd(y))
#         #pyl.title("Cd Across Span")
#         #pyl.xlabel("y (in)")
#         #pyl.ylabel('Cd')
#         #legend.append("TR = " + str(TR) + ",Fb = " + str(Fb))
#         
#         #pyl.axvline(x=Wing.Aileron.Tip()/IN)
#         #pyl.axvline(x=Wing.Aileron.Root()/IN)
#         #pyl.legend(legend, loc = 1)
#         #pyl.plt.grid(True)
#         #pyl.plt.ylim(0,0.05)
#         
#         temp = LLT.Cl(y)
#         last = len(temp) #Total length of Cl values (121)
#         #print "Halfway point is " + str(npy.round(last/2))
#         for x in range(2, npy.round(last/2)):
#             slope1 = temp[x] - temp[x-1]
#             slope2 = temp[x+1] - temp[x]
#             if slope2 < 0 or (slope2-slope1) > 0.0001:
#                 wingtipmax = x
#                 break
#                 #if slope2 > slope1:
#                 #    wingtipmax = x-1
#                     #print "Wingtipmax at " + str(x)
#                 #    break
#         try:
#             wingtipmax
#         except NameError:
#             #print "well, it WASN'T defined after all!"
#             wingtipmax = last/2
#         #else:
#             #print "sure, it was defined."
# 
#         diff = temp[last/2]-temp[wingtipmax]
# 
#         last1 = int(npy.round(last/2))
#         x = -((Wing.b/2)/IN)+((float(wingtipmax)/last1)*((Wing.b/2)/IN))
#         pyl.plot([x,x],[0,2])
# 
#         if diff > 0.1:
#             #print 'Fb : ', Fb, ' TR : ', TR,' Max Root Cl: ',temp[last/2]
#             print 'Fb : ', Fb, ' TR : ', TR,' Diff: ',diff
#         del wingtipmax
# pyl.show()