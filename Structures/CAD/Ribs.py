from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, PSI, LBF, AsUnit
from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing import Aircraft
import pylab as pyl



Aircraft.Wing.WingWeight.DrawRibs = True
Aircraft.Wing.WingWeight.DrawDetail = True
Aircraft.Wing.WingWeight.Draw(fig = 1)
    
Aircraft.Wing.Draw(fig = 1)

Aircraft.HTail.WingWeight.DrawRibs = True
Aircraft.HTail.WingWeight.DrawDetail = True
Aircraft.HTail.WingWeight.Draw(fig = 2)
    
Aircraft.HTail.Draw(fig = 2)

Aircraft.VTail.WingWeight.DrawRibs = True
Aircraft.VTail.WingWeight.DrawDetail = True
Aircraft.VTail.WingWeight.Draw(fig = 3)
    
Aircraft.VTail.Draw(fig = 3)


print 'Wing  Weight : ', AsUnit( Aircraft.Wing.Weight, 'lbf' )
print 'HTail Weight : ', AsUnit( Aircraft.HTail.Weight, 'lbf' )
print 'VTail Weight : ', AsUnit( Aircraft.VTail.Weight, 'lbf' )

pyl.show()