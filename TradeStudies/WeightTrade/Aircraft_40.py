from __future__ import division # let 5/2 = 2.5 rather than 2
#from os import environ as _environ; _environ["scalar_off"] = "off"

from scalar.units import M, FT, IN, ARCDEG, RAD, LBF, SEC, KG, SLUG, OZF, gacc, GRAM, OZM
from scalar.units import AsUnit
from Aerothon.ACAircraft import ACTailAircraft
from Aerothon.ACWingWeight import ACSolidWing, ACRibWing
from Aerothon.DefaultMaterialsLibrary import Monokote, PinkFoam, Basswood, Steel, Balsa, Aluminum, Ultracote
from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Fuselage import Fuselage
from Aircraft_Models.Reg2014Aircraft_AeroCats.Propulsion.Aircraft_Propulsion import Propulsion
from Aircraft_Models.Reg2014Aircraft_AeroCats.MonoWing.Wing import Wing
import pylab as pyl
import cmath as math
from Aerothon.ACTLenAircraft import ACTLenAircraft

#
# Create the Aircraft from the ACTLenAircraft class, which limits the sum of the L,W,and H
#Length of Aircraft characteristics, Don't really need to modify this thing
Aircraft = ACTLenAircraft()
Aircraft.name = 'AeroCats_2014'
#Don't know why this is here when it is defined on line 96
Aircraft.HTailPos
# The total allowable lengths summing height + width + length of the aircraft
Aircraft.TotalLengths = 174*IN
# Assign the already generated parts
#For Fuselage stuff go to the Fuselage script in Monowing
Aircraft.SetFuselage(Fuselage)
#Same thing with propulsion
Aircraft.SetPropulsion(Propulsion)
#
Aircraft.SetWing(Wing)

#
# Position the wing on the top of the fuselage
# This does not to be changed at all since it is positioned correctly
Aircraft.WingFuseFrac = 1.0
Aircraft.Wing.i = 0*ARCDEG
# Aircraft Properties
#Total weight is going to change
Aircraft.TotalWeight = 40 *LBF #52 to meet design criteria (190 & 100)
#Engine Alignment
Aircraft.EngineAlign = 0.5

Aircraft.TippingAngle     = 9*ARCDEG
Aircraft.RotationAngle    = 5*ARCDEG
Aircraft.Alpha_Groundroll = 0*ARCDEG 

Aircraft.CMSlopeAt   = (6 * ARCDEG, 12 * ARCDEG) 
Aircraft.CLSlopeAt   = (3 * ARCDEG, 14 * ARCDEG)
Aircraft.CLHTSlopeAt = (-5 * ARCDEG, 10 * ARCDEG)
Aircraft.DWSlopeAt   = (3 * ARCDEG, 15 * ARCDEG)

Aircraft.Alpha_Zero_CM  = 6 * ARCDEG   #for steady level flight
Aircraft.StaticMargin   = 0.20
Aircraft.WingXMaxIt = 60
#
# Maximum velocity for plotting purposes
#
Aircraft.VmaxPlt = 100*FT/SEC

#
# Estimate for the time the aircraft rotates on the ground during takeoff
#
Aircraft.RotationTime = 0.1 * SEC

###############################################################################
#
# Tail surfaces
#
###############################################################################

#==============================================================================
# Horizontal tail
#==============================================================================
HTail = Aircraft.HTail

# HTail.Airfoil  = 'E222'
# HTail.Airfoil  = 'E169'
HTail.Airfoil  = 'NACA3412'
#HTail.AR       = 5
HTail.b        = 50 * IN
HT_Chord       = 8.5 * IN
HTail.TR       = 1.0
HTail.o_eff    = 0.96
HTail.S        = HTail.b*HT_Chord 
HTail.L        = 33.49 * IN #Length from X_CG to Tail AC
#HTail.VC       = 0.32
HTail.FullWing = True
HTail.DWF      = 1.277 #Main wing Down wash factor (Typically between 1.0 (close to wing) and 2.0 (far away))
HTail.Inverted = True

HTail.ClSlopeAt = (-10*ARCDEG, 10*ARCDEG) 
HTail.CmSlopeAt = (-4*ARCDEG, 5*ARCDEG) 


Aircraft.HTailPos = 0.5

#
# Elevator properties
#
HTail.Elevator.Fc = 0.55
HTail.Elevator.Fb = 0.95
HTail.Elevator.Ft = 0.0 #0.25
HTail.Elevator.Weight = 0.1*LBF 
HTail.Elevator.WeightGroup = "HTail"
HTail.Elevator.Servo.Fc  = 0.3
HTail.Elevator.Servo.Fbc = 0.5
HTail.Elevator.Servo.Weight = 0.77 * OZF
HTail.Elevator.Servo.WeightGroup = "Controls"
HTail.Elevator.Servo.Torque = 55*IN*OZM
#Set the sweep about the elevator hinge
HTail.SweepFc  = 1.0 - HTail.Elevator.Fc

#
# Structural properties
# Spar taken as 1/8 inch width and thickness of the max thickness at the root
#
Basswood = Basswood.copy()
BWRibMat = Balsa.copy()
BWRibMat.Thickness = 1/8 * IN

HTail.SetWeightCalc(ACRibWing)
HTail.WingWeight.RibMat                    = BWRibMat
HTail.WingWeight.RibSpace                  = 10 * IN
HTail.WingWeight.SkinMat                   = Ultracote.copy()
HTail.WingWeight.WeightGroup = 'HTail'
HTail.WingWeight.AddSpar("MainSpar", 1*IN, 1.25*IN, (0.25,1),1.0, False)
HTail.WingWeight.MainSpar.SparMat.LinearForceDensity = .008*LBF/(1*IN) # = Balsa.copy()
HTail.WingWeight.MainSpar.Position = (0.45,0.55)
HTail.WingWeight.MainSpar.ScaleToWing = [False, False]
HTail.WingWeight.MainSpar.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("LeadingEdge", 1/8*IN, 1/4*IN, (0.25,1),1.0, False)
HTail.WingWeight.LeadingEdge.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.LeadingEdge.Position = (0.45,0.55)
HTail.WingWeight.LeadingEdge.ScaleToWing = [False, False]
HTail.WingWeight.LeadingEdge.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("TrailingEdge1", 1/16*IN, 11/8*IN, (0.25,1),1.0, False)
HTail.WingWeight.TrailingEdge1.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.TrailingEdge1.Position = (0.45,0.55)
HTail.WingWeight.TrailingEdge1.ScaleToWing = [False, False]
HTail.WingWeight.TrailingEdge1.WeightGroup = "HTail"

HTail.WingWeight.AddSpar("TrailingEdge2", 1/16*IN, 11/8*IN, (0.25,1),1.0, False)
HTail.WingWeight.TrailingEdge2.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
HTail.WingWeight.TrailingEdge2.Position = (0.45,0.55)
HTail.WingWeight.TrailingEdge2.ScaleToWing = [False, False]
HTail.WingWeight.TrailingEdge2.WeightGroup = "HTail"

#==============================================================================
# Vertical tail - Side VTs
#==============================================================================
VTail = Aircraft.VTail
VTail.Airfoil = 'NACA0012'
#VTail.VC      = 0.014
#VTail.AR      = 1
VTail.TR      = 1
VTail.Axis    = (0, 1)
VTail.L       = 40 * IN
VTail.o_eff    = 0.96
VTail_c       = 14 * IN
VTail.b       = 11 * IN #VTail Height
VTail.S       = VTail.b*VTail_c


VTail.FullWing = False
VTail.Symmetric = True
Aircraft.VTailPos = 1


#
# Rudder properties
#
VTail.Rudder.Fc = 0.8
VTail.Rudder.Weight = 0.05*LBF
VTail.Rudder.WeightGroup = "VTail"
VTail.Rudder.SgnDup    = -1.0
VTail.Rudder.Servo.Fc  = 0.3
VTail.Rudder.Servo.Fbc = 0.5
#VTail.Rudder.Servo.Weight = 5*GRAM*gacc
VTail.Rudder.Servo.Weight = 0.77 * OZF
VTail.Rudder.Servo.WeightGroup = "Controls"
VTail.Rudder.Servo.Torque = 55*IN*OZM
#Set the sweep about the rudder hinge
VTail.SweepFc = 1.0 - VTail.Rudder.Fc

#
# Structural properties
# Spar taken as 1/8 inch width and thickness of the max thickness at the root
#
VTail.SetWeightCalc(ACRibWing)
VTail.WingWeight.RibMat                    = BWRibMat
VTail.WingWeight.RibSpace                  = 5 * IN
VTail.WingWeight.SkinMat                   = Ultracote.copy()
VTail.WingWeight.WeightGroup = 'VTail'
VTail.WingWeight.AddSpar("MainSpar", 1*IN, 1*IN, (0.25,1),1.0, False)
VTail.WingWeight.MainSpar.SparMat.LinearForceDensity = .008*LBF/(1*IN) #= Balsa.copy()
VTail.WingWeight.MainSpar.Position = (0.45,0)
VTail.WingWeight.MainSpar.ScaleToWing = [False, False]
VTail.WingWeight.MainSpar.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("LeadingEdge", 1/8*IN, 1/4*IN, (0.25,1),1.0, False)
VTail.WingWeight.LeadingEdge.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.LeadingEdge.Position = (0.008,0)
VTail.WingWeight.LeadingEdge.ScaleToWing = [False, False]
VTail.WingWeight.LeadingEdge.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("TrailingEdge1", 1/16*IN, 1.75*IN, (0.25,1),1.0, False)
VTail.WingWeight.TrailingEdge1.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.TrailingEdge1.Position = (0.915,0.2)
VTail.WingWeight.TrailingEdge1.ScaleToWing = [False, False]
VTail.WingWeight.TrailingEdge1.WeightGroup = "VTail"

VTail.WingWeight.AddSpar("TrailingEdge2", 1/16*IN, 1.75*IN, (0.25,1),1.0, False)
VTail.WingWeight.TrailingEdge2.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
VTail.WingWeight.TrailingEdge2.Position = (0.915,-0.2)
VTail.WingWeight.TrailingEdge2.ScaleToWing = [False, False]
VTail.WingWeight.TrailingEdge2.WeightGroup = "VTail"

#
# A second vertical tail
#
# Aircraft.VTail2 = None

if Aircraft.VTail2 is not None:
    #==============================================================================
    # Vertical tail - Center
    #==============================================================================
    VTail2 = Aircraft.VTail2
    VTail2.Airfoil = 'NACA0012'
    VTail2.TR      = 1
    VTail2.Axis    = (0, 1)
    VTail2.L       = 4.0 * IN
    VTail2.o_eff    = 0.96
    # VTail2.S       = 175*IN**2
    VTail2.b       = 9.5 * IN # VTail Height
    VTail2_c        = 18 * IN
    VTail2.S        = VTail2.b*VTail2_c
     
    VTail2.FullWing = False
    VTail2.Symmetric = False
    Aircraft.VTail2Pos = 0 # Spanwise position along the HT
    Aircraft.VTail2Root = 0.5 #  VT vertical placement on HT
     
    VTail2.Rudder.Fc = 0.8
    VTail2.Rudder.Weight = 0.05*LBF
    VTail2.Rudder.WeightGroup = "VTail2"
    VTail2.Rudder.SgnDup    = -1.0
    VTail2.Rudder.Servo.Fc  = 0.3
    VTail2.Rudder.Servo.Fbc = 0.5
    #VTail2.Rudder.Servo.Weight = 5*GRAM*gacc
    VTail2.Rudder.Servo.Weight = 0.77 * OZF
    VTail2.Rudder.Servo.WeightGroup = "Controls"
    VTail2.Rudder.Servo.Torque = 55*IN*OZM
    #Set the sweep about the rudder hinge
    VTail2.SweepFc = 1.0 - VTail2.Rudder.Fc
 
    #
    # Structural properties
    # Spar taken as 1/8 inch width and thickness of the max thickness at the root
    #
    VTail2.SetWeightCalc(ACRibWing)
    VTail2.WingWeight.RibMat                    = BWRibMat
    VTail2.WingWeight.RibSpace                  = 5 * IN
    VTail2.WingWeight.SkinMat                   = Ultracote.copy()
    VTail2.WingWeight.WeightGroup = 'VTail2'
    VTail2.WingWeight.AddSpar("MainSpar", 1*IN, 1*IN, (0.25,1),1.0, False)
    VTail2.WingWeight.MainSpar.SparMat.LinearForceDensity = .008*LBF/(1*IN)
    VTail2.WingWeight.MainSpar.Position = (0.45,0)
    VTail2.WingWeight.MainSpar.ScaleToWing = [False, False]
    VTail2.WingWeight.MainSpar.WeightGroup = "VTail2"
 
    VTail2.WingWeight.AddSpar("LeadingEdge", 1/8*IN, 1/4*IN, (0.25,1),1.0, False)
    VTail2.WingWeight.LeadingEdge.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
    VTail2.WingWeight.LeadingEdge.Position = (0.008,0)
    VTail2.WingWeight.LeadingEdge.ScaleToWing = [False, False]
    VTail2.WingWeight.LeadingEdge.WeightGroup = "VTail2"
 
    VTail2.WingWeight.AddSpar("TrailingEdge1", 1/16*IN, 13/8*IN, (0.25,1),1.0, False)
    VTail2.WingWeight.TrailingEdge1.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
    VTail2.WingWeight.TrailingEdge1.Position = (0.915,0.2)
    VTail2.WingWeight.TrailingEdge1.ScaleToWing = [False, False]
    VTail2.WingWeight.TrailingEdge1.WeightGroup = "VTail2"
     
    VTail2.WingWeight.AddSpar("TrailingEdge2", 1/16*IN, 13/8*IN, (0.25,1),1.0, False)
    VTail2.WingWeight.TrailingEdge2.SparMat = Balsa.copy() #.LinearForceDensity = .008*LBF/(1*IN)
    VTail2.WingWeight.TrailingEdge2.Position = (0.915,-0.2)
    VTail2.WingWeight.TrailingEdge2.ScaleToWing = [False, False]
    VTail2.WingWeight.TrailingEdge2.WeightGroup = "VTail2"

###############################################################################
#
# Landing Gear
#
###############################################################################
Aluminum = Aluminum.copy()
Steel    = Steel.copy()
MainGear = Aircraft.MainGear
MainGear.Theta        = 89.9*ARCDEG
#MainGear.GearHeight   = 3   * IN
MainGear.StrutL       = 2 * IN
MainGear.StrutW       = 0.2 * IN
MainGear.StrutH       = 0.1 * IN
MainGear.WheelDiam    = 4 * IN
MainGear.X[1]         = 2.5 * IN
MainGear.Strut.Weight = 0.1*LBF #math.pi*(0.125/2*IN)**2*12*IN*Aluminum.ForceDensity #1/8 inch diameter steel, l=12in
MainGear.Strut.WeightGroup = "LandingGear"
MainGear.Wheel.Weight = 0.1*LBF 
MainGear.Wheel.WeightGroup = "LandingGear"

NoseGear = Aircraft.NoseGear
NoseGear.StrutW    = 0.1 * IN
NoseGear.StrutH    = 0.1 * IN
NoseGear.WheelDiam = 4 * IN

NoseGear.Strut.Weight = .3*LBF #math.pi*(0.125/2*IN)**2*8*IN*Steel.ForceDensity #1/8 inch diameter steel, l=8in
NoseGear.Strut.WeightGroup = "LandingGear"
NoseGear.Wheel.Weight = .16*LBF
NoseGear.Wheel.WeightGroup = "LandingGear"

NoseGear.Strut.Weight = 0.2*LBF #math.pi*(0.125/2*IN)**2*8*IN*Steel.ForceDensity #1/8 inch diameter steel, l=8in
NoseGear.Strut.WeightGroup = "LandingGear"
NoseGear.Wheel.Weight = 0.1*LBF
NoseGear.Wheel.WeightGroup = "LandingGear"



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
    Aircraft.WriteAVLAircraft('AVLAircraft_Latest_No_Winglets.avl')  
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
    
