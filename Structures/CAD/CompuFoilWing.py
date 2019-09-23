from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft
from scalar.units import AsUnit, IN
import pylab as pyl

Aircraft.Refresh()
Aircraft.Draw()

def PrintLiftSurf(surf):
    print 80*'='
    print surf.name
    print
    print 'X : ', AsUnit( surf.X, 'in')
    
    y = []
    y.append( 0*IN )
    print 'Span  : ', AsUnit( y[0], 'in' )
    
    fac = 2 if surf.FullWing else 1
    
    for Fb in surf.Fb:
        y.append( surf.b/fac*Fb )
        print 'Span  : ', AsUnit( y[-1], 'in' )
    
    for i in xrange(1,len(y)):
        
        print
        print 'Section    : ', AsUnit( y[i] - y[i-1], 'in' )
        print 'Chord Root : ', AsUnit( surf.Chord(y[i-1]), 'in' )
        print 'Chord Tip  : ', AsUnit( surf.Chord(y[i]), 'in' )
    
    print
                
#PrintLiftSurf(Aircraft.Wing)

#PrintLiftSurf(Aircraft.HTail)

#PrintLiftSurf(Aircraft.VTail)

print 80*'='
print
print "Main Wing :"
Aircraft.Wing.PrintCompufoilGenRibs()
print
print 80*'='

print 80*'='
print
print "Hoizontal Tail :"
Aircraft.HTail.PrintCompufoilGenRibs()
print
print 80*'='

print 80*'='
print
print "Vertical Tail :"
Aircraft.VTail.PrintCompufoilGenRibs()
print
print 80*'='

pyl.show()