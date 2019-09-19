from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Aircraft import Aircraft, Wing
from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Fuselage import Fuselage
from scalar.units import ARCDEG, FT, SEC, LBF, IN
from scalar.units import AsUnit
import pylab as pyl

Wing.b       = 114*IN

#ClimbRate 100
#Wing.S= 3160*IN**2
#Aircraft.TotalWeight= 50.65 *LBF

#MaxClimb Rate 120, L.O CR 61.4
Wing.S= 2370*IN**2
Aircraft.TotalWeight= 40 *LBF

#===============================================================================
# 3D Wing Slopes
#===============================================================================
Aircraft.CMSlopeAt   = (0 * ARCDEG, 17 * ARCDEG) 
#Aircraft.CLSlopeAt   = (15 * ARCDEG, 18 * ARCDEG)
#Aircraft.CLHTSlopeAt = (5 * ARCDEG, 18 * ARCDEG)
#Aircraft.DWSlopeAt   = (5 * ARCDEG, 19 * ARCDEG)

#Aircraft.Alpha_Zero_CM  = 0 * ARCDEG   #Angle of attach where CM = 0 for the aircraft
#Aircraft.StaticMargin   = 0.09
#Aircraft.WingXMaxIt = 20

#==============================================================================
# Horizontal tail
#==============================================================================
HTail = Aircraft.HTail

HTail.Airfoil  = 'NACA3412'
#HTail.AR       = 5
HTail.b        = 65 * IN
HTail.TR       = 1.0
HTail.o_eff    = 0.96
HTail.S        = 480 * IN**2
HTail.L        = 33.49 * IN #Length from X_CG to Tail AC
#HTail.VC       = 0.32
HTail.FullWing = True
HTail.DWF      = 1.3 #Main wing Down wash factor (Typically between 1.0 (close to wing) and 2.0 (far away))
HTail.Inverted = True

HTail.ClSlopeAt = (-10*ARCDEG, 10*ARCDEG) 
HTail.CmSlopeAt = (-4*ARCDEG, 5*ARCDEG) 


Aircraft.HTailPos = 1
#===============================================================================
# Elevator properties
#===============================================================================
#HTail.Elevator.Fc = 0.5
#HTail.Elevator.Fb = 1.0
#HTail.Elevator.Ft = 0.0
#HTail.Elevator.Weight = 0.1*LBF 
#HTail.Elevator.Servo.Fc  = 0.3
#HTail.Elevator.Servo.Fbc = 0.1
#HTail.Elevator.Servo.Weight = 2.11 * OZF
#HTail.Elevator.Servo.Torque = 131*IN*OZM
##Set the sweep about the elevator hinge
#HTail.SweepFc  = 1.0 - HTail.Elevator.Fc

#==============================================================================
# Vertical tail
#==============================================================================
VTail = Aircraft.VTail
#VTail.Airfoil = 'NACA0012'
#VTail.VC      = 0.0043
#VTail.AR      = 2
#VTail.TR      = .7
#VTail.Axis    = (0, 1)
#VTail.L       = 10.0 * IN
#VTail.o_eff    = 0.96

#===============================================================================
 # Rudder properties
#===============================================================================
#VTail.Rudder.Fc = 0.5
#VTail.Rudder.Weight = 0.05*LBF * 2 # * 2 For symmetric vertical tail
#VTail.Rudder.SgnDup    = -1.0
#VTail.Rudder.Servo.Fc  = 0.3
#VTail.Rudder.Servo.Fbc = 0.1
#VTail.Rudder.Servo.Weight = 5*GRAM*gacc
#VTail.Rudder.Servo.Weight = 0.58 * OZF
#VTail.Rudder.Servo.Torque = 42*IN*OZM
#Set the sweep about the rudder hinge
#VTail.SweepFc = 1.0 - VTail.Rudder.Fc


if __name__ == '__main__':
        
        
    print
    print 'Aircraft   V_LO :', AsUnit( Aircraft.GetV_LO(), 'ft/s' )
    print 'Wing       V_LO :', AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s' )
    print

    H = max(Aircraft.Wing.Upper(0*IN), Aircraft.VTail.Tip()[2])
    W = Aircraft.Wing.b
    L = Aircraft.TotalLengths - W - H
    print 'V max climb    : ', AsUnit(Aircraft.V_max_climb(), 'ft/s')
    print 'V max          : ', AsUnit(Aircraft.Vmax(),'ft/s')
    print 'Ground Roll    : ', AsUnit(Aircraft.Groundroll(),  'ft') 
    print 'Total Weight   : ', AsUnit(Aircraft.TotalWeight,   'lbf')
    print 'Payload Weight  : ', AsUnit(Aircraft.PayloadWeight(), 'lbf')
    print 'Wing Height     : ', AsUnit(Aircraft.Wing.Upper(0*IN), 'in')
    print 'Vertical Tail H : ', AsUnit( Aircraft.VTail.Tip()[2], 'in' )
    print 'Width           : ', AsUnit( W, 'in' )
    print 'Length          : ', AsUnit( L, 'in' )
    print 'Sum of Lengths  : ', AsUnit( (W + L + H), 'in' )
    print 'HTail Incidence : ', AsUnit(Aircraft.HTail.i, 'deg')
    print 'HTail Length    : ', AsUnit(Aircraft.HTail.L, 'in')
    print "Lift of AoA     : ", AsUnit( Aircraft.GetAlphaFus_LO(), 'deg' )
    print "Zero CM AoA     : ", AsUnit( Aircraft.Alpha_Zero_CM, 'deg' )
    print 'HTail  VC       : ',AsUnit( Aircraft.HTail.VC) 
    print 'VTail  VC       : ',AsUnit( Aircraft.VTail.VC)
    print 'VTail2 VC       : ',AsUnit( Aircraft.VTail2.VC) 
    
 
    Aircraft.Draw()
    Aircraft.WriteAVLAircraft('AVLAircraft_Latest.avl')  
#      
#    VTail.WingWeight.DrawRibs = True
#    VTail.WingWeight.DrawDetail = True
#    VTail.WingWeight.Draw(fig = 2)
#    VTail.Draw(fig = 2)
#    
#    HTail.WingWeight.DrawRibs = True
#    HTail.WingWeight.DrawDetail = True
#    HTail.WingWeight.Draw(fig = 3)
#    HTail.Draw(fig = 3)
    
    Aircraft.PlotPolarsSlopes(fig=3)
    Aircraft.PlotCMPolars(4, (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG), XcgOffsets=(+0.02, -0.02))
    
    #HTail.Draw2DAirfoilPolars(fig=2)
    #Aircraft.PlotCLCMComponents(fig = 5, del_es = (-10*ARCDEG, -5*ARCDEG, 0*ARCDEG, +5*ARCDEG, +10 * ARCDEG))
    pyl.show()
    
    
