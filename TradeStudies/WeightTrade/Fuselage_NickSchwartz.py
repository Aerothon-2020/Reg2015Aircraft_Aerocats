from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import IN, LBF, SLUG, FT, GRAM, gacc, OZF
from scalar.units import AsUnit
from Aerothon.ACFuselage import ACFuselage
from Aircraft_Models.Reg2014Aircraft_AeroCats.Structures.Materials import BalsaBH, ACPlyBH, ACPlySkin, BassStringer, BalsaStringer, Monokote, Steel

Fuselage = ACFuselage()
#
# Create the sections of the fuselage
#
Fuselage.AddSection('Nose'   , 9*IN, -1)
Fuselage.AddSection('PyldBay', 5*IN, -1)
Fuselage.AddSection('Tail')

#
# Size the engine fire wall
#
Fuselage.Nose.FrontBulk.Width  = 3*IN
Fuselage.Nose.FrontBulk.Height = 3*IN
Fuselage.Nose.FrontBulk.Material = ACPlyBH.copy()
Fuselage.Nose.Align             = 1
Fuselage.Nose.SkinMat = Monokote.copy()
Fuselage.Nose.StringerMat.LinearForceDensity = .001*LBF/IN
Fuselage.Nose.FrontBulk.WeightGroup = 'Fuselage'
#
# Size the payload bay
#
Fuselage.PyldBay.FrontBulk.Width  = 6*IN
Fuselage.PyldBay.FrontBulk.Height = 6*IN
Fuselage.PyldBay.BackBulk.Width   = 6*IN
Fuselage.PyldBay.BackBulk.Height  = 6*IN
Fuselage.PyldBay.FrontBulk.Material = BalsaBH.copy()
Fuselage.PyldBay.BackBulk.Material  = BalsaBH.copy()
Fuselage.PyldBay.SkinMat = Monokote.copy()
Fuselage.PyldBay.StringerMat.LinearForceDensity = 0.01*LBF/IN
Fuselage.PyldBay.FrontBulk.WeightGroup = 'Fuselage'
Fuselage.PyldBay.BackBulk.WeightGroup = 'Fuselage'
Fuselage.PyldBay.WeightGroup = "Fuselage"

#
# Change the alignement of the tail taper section
#
Fuselage.Tail.BackBulk.Width  = 2.5*IN
Fuselage.Tail.BackBulk.Height = 2*IN
Fuselage.Tail.BackBulk.X      = [40*IN,0*IN,0*IN]  #Just for viewing, will actually be placed by the HT in the Aircraft file
Fuselage.Tail.BackBulk.Material = BalsaBH.copy()
Fuselage.Tail.Align       = .5
Fuselage.Tail.SkinMat     = Monokote.copy()
Fuselage.Tail.StringerMat.LinearForceDensity = 0.01*LBF/IN
Fuselage.Tail.BackBulk.WeightGroup = 'Fuselage'
Fuselage.Tail.WeightGroup = "Fuselage"

#
# Add some components to the nose section
#
Fuselage.Nose.AddComponent    (     "FuelTank" , 0.072*LBF, (2.5*IN,2*IN,1.25*IN)  , "Back"   , (0.75, 0.5, 0.7) )
Fuselage.Nose.AddComponent    ("NoseWheelServo", 0.05*LBF, (1.14*IN,0.51*IN,1.18*IN)     , "Bottom" , (0.4 , 0.2, 0.0) )
Fuselage.Nose.AddComponent    ("ThrottleServo" , 0.048*LBF, (1.18*IN,0.47*IN,1.18*IN)     , "Left" , (0.6 , 0.2, 0.5) )
Fuselage.Nose.AddComponent    ("Receiver"      , 0.030*LBF, (1.61*IN,1.86*IN,0.56*IN)     , "Bottom"   , (0.7 , 0.2, 0.5) )
Fuselage.Nose.AddComponent    (     "MotorBattery"  , 0.85*LBF, (0.9*IN,1.4*IN,3*IN) , "Front"  , (0.5 , 0.5, 0.5) )
#Fuselage.Nose.FuelTank.WeightGroup = "Fuel"
Fuselage.Nose.AddComponent("SpeedController", 6*GRAM*gacc , ( 0.16*IN, 1.08*IN, 0.91*IN), "Right", (0.7 , 0.0, 0.5) )
Fuselage.Nose.NoseWheelServo.WeightGroup = "Controls"
Fuselage.Nose.ThrottleServo.WeightGroup = "Controls"
Fuselage.Nose.Receiver.WeightGroup = "Controls"
Fuselage.Nose.MotorBattery.WeightGroup = "Propulsion"
Fuselage.Nose.SpeedController.WeightGroup = "Propulsion"
#
# Define which section contains the CG of the aircraft
#
Fuselage.XcgSection = Fuselage.PyldBay
Fuselage.XcgSecFrac = 5./9.

#
# Define the payload shape
#
Fuselage.Payload.Width  = 5*IN
Fuselage.Payload.Length = 7.5*IN
Fuselage.Payload.Face = 'Bottom'
Fuselage.Payload.Material = Steel.copy()
Fuselage.Payload.Weight = 1*LBF

#
# Determine which bulkhead should be set by the horizontal tail
#
Fuselage.TailBulk = Fuselage.Tail.BackBulk
Fuselage.TailBulk.WeightGroup = 'Fuselage'

if __name__ == '__main__':
    import pylab as pyl
    
    print 'Nose      Weight :', AsUnit( Fuselage.Nose.Weight, 'lbf' )
    print 'PyldBay   Weight :', AsUnit( Fuselage.PyldBay.Weight, 'ozf' )
    print 'TailTaper Weight :', AsUnit( Fuselage.Tail.Weight, 'lbf' )
    
    print 'Fuselage Weight    :', AsUnit( Fuselage.Weight, 'lbf' )
    print 'Fuselage MOI       :', AsUnit( Fuselage.MOI(), 'slug*ft**2' )
    print 'Fuselage CG        :', AsUnit( Fuselage.CG(), 'in' )
    print 'Fuselage Desired CG:', AsUnit( Fuselage.AircraftCG(), 'in' )
    
    
    Fuselage.Draw()
    pyl.show()