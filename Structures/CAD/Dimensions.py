from Aircraft_Models.Reg2015Aircraft_AeroCats.MonoWing.Aircraft_new import Aircraft
from scalar.units import IN, LBF, SLUG, FT, OZF
from scalar.units import AsUnit
import pylab as pyl

Fuselage = Aircraft.Fuselage


#Aircraft.Draw()
    
print 'Nose Height : ', AsUnit( Fuselage.Nose.FrontBulk.Height, 'in')
print 'Nose Width : ', AsUnit( Fuselage.Nose.FrontBulk.Width, 'in')
print 'Nose Length : ', AsUnit( Fuselage.Nose.Length, 'in')

print 'PyldBay Front Bulkhead Height : ', AsUnit( Fuselage.PyldBay.FrontBulk.Height, 'in')
print 'PyldBay Front Bulkhead Width : ', AsUnit( Fuselage.PyldBay.FrontBulk.Width, 'in')
print 'PyldBay Length : ', AsUnit( Fuselage.PyldBay.Length, 'in')
print 'PyldBay Back Bulkhead Height : ', AsUnit( Fuselage.PyldBay.BackBulk.Height, 'in')
print 'PyldBay Back Bulkhead Width : ', AsUnit( Fuselage.PyldBay.BackBulk.Width, 'in')

print 'Tail Length : ', AsUnit( Fuselage.Tail.Length, 'in')
print 'Tail Back Bulkhead Height : ', AsUnit( Fuselage.Tail.BackBulk.Height, 'in')
print 'Tail Back Bulkhead Width : ', AsUnit( Fuselage.Tail.BackBulk.Width, 'in')
print
#print 'Aircraft.CG : ', AsUnit( Aircraft.DesignCG(), 'in')
#print 'Aircraft.Xnp : ', AsUnit( Aircraft.Xnp(), 'in')
print
print 'Wing   CG : ',  AsUnit( (Aircraft.DesignCG()[0] - Aircraft.Wing.LE(0*IN)), 'in')
print 'Wing % CG : ', (Aircraft.DesignCG()[0] - Aircraft.Wing.LE(0*IN))/Aircraft.Wing.Chord(0*IN)
print
print 'Wing TE  CG : ',  AsUnit( (Aircraft.DesignCG()[0] - Aircraft.Wing.TE(0*IN)), 'in')
print 'Aircraft Xnp TE : ', AsUnit( Aircraft.Xnp()- Aircraft.Wing.TE(0*IN), 'in')
print 'Aircraft Xac TE : ', AsUnit( Aircraft.Wing.Xac()- Aircraft.Wing.TE(0*IN), 'in')
print 
print 'Wing TE Position vs Pld Back Bulk : ', AsUnit( Fuselage.PyldBay.BackBulk.X[0]- Aircraft.Wing.TE(0*IN), 'in')

print "Wing Area   : ", AsUnit( Aircraft.Wing.S, 'in**2' )
print "Wing Span   : ", AsUnit( Aircraft.Wing.b, 'ft' )
print "Wing TR     : ", Aircraft.Wing.TR
print "Wing AR     : ", Aircraft.Wing.AR

print "H Area   : ", AsUnit( Aircraft.HTail.S, 'in**2' )
print "H Span   : ", AsUnit( Aircraft.HTail.b, 'ft' )
print "H TR     : ", Aircraft.HTail.TR
print "H AR     : ", Aircraft.HTail.AR

print "V Area   : ", AsUnit( Aircraft.VTail.S, 'in**2' )
print "V Span   : ", AsUnit( Aircraft.VTail.b, 'ft' )
print "V TR     : ", Aircraft.VTail.TR
print "V AR     : ", Aircraft.VTail.AR
#print 'Tipping Angle : ', AsUnit( Aircraft.TippingAngle, 'deg')
Fuselage.Draw(fig=2)
pyl.show()