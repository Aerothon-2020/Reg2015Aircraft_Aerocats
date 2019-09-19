from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import LBF, SEC, ARCDEG, FT, IN, SLUG, OZF, OZM
from scalar.units import AsUnit
from Aerothon.ACWing import ACMainWing
from Aerothon.DefaultMaterialsLibrary import PinkFoam, Monokote, Basswood, Balsa, Ultracote
from Aerothon.ACWingWeight import ACSolidWing, ACRibWing

#
# Create the wing
#
Wing = ACMainWing(1)
Wing.Lift_LO = None
#Initially 147 inches, changed to 105 inches (0.6 total length)
Wing.b       = 105*IN #96
#Initially 38 ft/sec
Wing.V_Stall = 38 * FT/SEC #From Jake's Matlab calculation
# Surface Area of wing
Wing.S       = 2147*IN**2
#Wing.Lift_LO = 55*LBF
#Was 2000 ft since last year's was in Texas
Wing.Alt_LO  = 200 * FT #Lakeland, FL's elevation

###############################################################################
#
# Geometric properties
#
###############################################################################

Wing.FullWing = True

#Wing.UpperWing.b   = 4.5*FT
#Wing.LowerWing.b   = 4*FT

#===============================================================================
 #b=150,S=3200
#===============================================================================
Wing.TR      = [1.0,0.5] #Increased from MAX L/D to increase root induced aoa
Wing.Fb      = [0.66,1] #Original
#Wing.TR      = [1.0,0.4] #Max L/D
#Wing.Fb      = [0.467,1] #Max L/D
#Wing.TR      = [1.0,0.2] #Max CL
#Wing.Fb      = [0.53,1] #Max CL
#Wing.TR      = [1.0,0.3] #Max e
#Wing.Fb      = [0.467,1] #Max e
#===============================================================================
# 
#===============================================================================

Wing.Gam     = [ 0*ARCDEG,0*ARCDEG]
Wing.Lam     = [ 0*ARCDEG,0*ARCDEG]

#Wing.SweepFc = 0.5
#Wing.CEdge   = 'LE' #LE of wing to be tapered or constant LE
Wing.ConstUpper = True

#
# Add Vertical `s
#

#Wing.AddWinglet("Winglet",2)
#Winglet = Wing.Winglets.Winglet
#      
#Winglet.b = 7.0 *IN
#Winglet.Airfoil = 'S1223_TC'
#Winglet.Lam = [0*ARCDEG, 0*ARCDEG]
#Winglet.Gam = [0*ARCDEG, 0*ARCDEG]
#Winglet.Fb  = [0.3, 1]
#Winglet.TR  = [0.9, 0.8]
#Winglet.SweepFc = 0
#Winglet.Symmetric = True
      
#Winglet.SetWeightCalc(ACSolidWing)
#Winglet.WingWeight.WingMat = PinkFoam.copy()


###############################################################################
#
# Aerodynamic properties
#
###############################################################################

#
# Set the airfoils
#
Wing.Airfoil = 'S1223_TC'

#
# Finite wing correction factor. Used to make 2D airfoil data match the 3D wing profiles.
#
Wing.FWCF = 0.98

#
# Oswald efficiency
#
Wing.o_eff = 0.9733

#
# Polar slope evaluations
#
Wing.ClSlopeAt = (0*ARCDEG, 7*ARCDEG)
Wing.CmSlopeAt = (0*ARCDEG, 4*ARCDEG)


###############################################################################
#
# Control surfaces
#
###############################################################################

#
# Define the control surfaces
#
Wing.AddControl('Aileron')
Wing.Aileron.Fc = 0.30
Wing.Aileron.Fb = 0.34 #Adjusted to make Aileron begin at a Wing rib
Wing.Aileron.Ft = 0.00 #Adjusted to make Aileron end at a Wing rib
Wing.Aileron.SgnDup = -1.
Wing.Aileron.Weight = 0.01*LBF
Wing.Aileron.WeightGroup = "MainWing"
Wing.Aileron.Servo.Fc     = 0.3
Wing.Aileron.Servo.Weight = 1.55*OZF
Wing.Aileron.Servo.Torque = 128*IN*OZM
Wing.Aileron.Servo.WeightGroup = 'Controls'

###############################################################################
#
# Structural properties
#
###############################################################################
#
# Spar material (basswood, 1/4in width at max airfoil thickness + d-spar skin, balsa 1/16in)
#
SparW = 1.75*IN
SparH = 1.5*IN
CapH = 1/8*IN
WebW = 1/8*IN

CapArea = SparW*CapH*2
WebArea = WebW*SparH*2

SparLinearDensity = WebArea*Balsa.ForceDensity + CapArea*Basswood.ForceDensity

Wing.SetWeightCalc(ACRibWing)
Wing.WingWeight.AddSpar("MainSpar", SparH, SparW, (0.18,1), 1.0, False)
Wing.WingWeight.MainSpar.SparMat = Balsa.copy()
Wing.WingWeight.MainSpar.SparMat.LinearForceDensity = SparLinearDensity
Wing.WingWeight.MainSpar.Position = (0.25,0)
Wing.WingWeight.MainSpar.ScaleToWing = [False, False]
Wing.WingWeight.MainSpar.WeightGroup = "MainWing"
Wing.WingWeight.SkinMat = Ultracote.copy()

Wing.WingWeight.AddSpar("SecondSpar", 1/8*IN, 1/4*IN, (0.5,1),1.0, False)
Wing.WingWeight.SecondSpar.SparMat = Balsa.copy()
Wing.WingWeight.SecondSpar.Position = (0.75,-0.01)
Wing.WingWeight.SecondSpar.ScaleToWing = [False, False]
Wing.WingWeight.SecondSpar.WeightGroup = "MainWing"

Wing.WingWeight.AddSpar("ThirdSpar", 1/8*IN, 1/4*IN, (0.5,1),1.0, False)
Wing.WingWeight.ThirdSpar.SparMat = Balsa.copy()
Wing.WingWeight.ThirdSpar.Position = (0.75,0.01)
Wing.WingWeight.ThirdSpar.ScaleToWing = [False, False]
Wing.WingWeight.ThirdSpar.WeightGroup = "MainWing"

Wing.WingWeight.AddSpar("LeadingEdge",1/8*IN, 1/4*IN, (0,1), 1.0, False)
Wing.WingWeight.LeadingEdge.SparMat= Balsa.copy()
Wing.WingWeight.LeadingEdge.Position = (0.006,0)
Wing.WingWeight.LeadingEdge.ScaleToWing = [False, False]
Wing.WingWeight.LeadingEdge.WeightGroup = "MainWing"

Wing.WingWeight.AddSpar("LeadingEdgeBent1", 1/32*IN, 3.25*IN, (0,1), 1.0, False)
Wing.WingWeight.LeadingEdgeBent1.SparMat = Balsa.copy()
Wing.WingWeight.LeadingEdgeBent1.Position = (0.066,-0.8)
Wing.WingWeight.LeadingEdgeBent1.ScaleToWing = [False,False]
Wing.WingWeight.LeadingEdgeBent1.WeightGroup = "MainWing"

Wing.WingWeight.AddSpar("LeadingEdgeBent2", 1/32*IN, 3.25*IN, (0,1), 1.0, False)
Wing.WingWeight.LeadingEdgeBent2.SparMat = Balsa.copy()
Wing.WingWeight.LeadingEdgeBent2.Position = (0.068,-0.5)
Wing.WingWeight.LeadingEdgeBent2.ScaleToWing = [False,False]
Wing.WingWeight.LeadingEdgeBent2.WeightGroup = "MainWing"

Wing.WingWeight.AddSpar("TrailingEdge1", 1/32*IN, 3*IN, (0,1), 1.0, False)
Wing.WingWeight.TrailingEdge1.SparMat = Balsa.copy()
Wing.WingWeight.TrailingEdge1.Position = (0.94,-0.1)
Wing.WingWeight.TrailingEdge1.ScaleToWing = [False,False]
Wing.WingWeight.TrailingEdge1.WeightGroup = "MainWing"

Wing.WingWeight.AddSpar("TrailingEdge2", 1/32*IN, 3*IN, (0,1), 1.0, False)
Wing.WingWeight.TrailingEdge2.SparMat = Basswood.copy()
Wing.WingWeight.TrailingEdge2.Position = (0.94,0.1)
Wing.WingWeight.TrailingEdge2.ScaleToWing = [False,False]
Wing.WingWeight.TrailingEdge2.WeightGroup = "MainWing"

Wing.WingWeight.WeightGroup = 'MainWing'

#
# Rib material (1/8in balsa)
#
BWRibMat = Balsa.copy()
BWRibMat.Thickness = .25*IN

Wing.WingWeight.RibMat   = BWRibMat
Wing.WingWeight.RibSpace = 5.333*IN

#Wing.SetWeightCalc(ACSolidWing)
#Wing.WingWeight.SparMat.LinearForceDensity = 0.0051*LBF/IN
#Wing.WingWeight.SkinMat                    = Monokote.copy()
#Wing.WingWeight.WingMat                    = PinkFoam.copy()
#Wing.WingWeight.WingMat.ForceDensity      *= 0.5

if __name__ == '__main__':
    import pylab as pyl
        
    print "V lift off  : ", AsUnit( Wing.GetV_LO(), 'ft/s' )
    print "V stall     : ", AsUnit( Wing.V_Stall, 'ft/s' )
    print "Wing Area   : ", AsUnit( Wing.S, 'in**2' )
    print "Wing Span   : ", AsUnit( Wing.b, 'ft' )
    print "Wing AR     : ", Wing.AR
    print "Wing MAC    : ", AsUnit( Wing.MAC(), 'in' )
    print "Wing Xac    : ", Wing.Xac()
    print "Wing dCM_da : ", Wing.dCM_da()
    print "Wing dCL_da : ", Wing.dCL_da()
    print "Lift of Load: ", AsUnit( Wing.Lift_LO, 'lbf' )

    print "Wing Thickness: ", AsUnit(Wing.Thickness(0*FT),'in')
    print "Wing Chord    : ", AsUnit(Wing.Chord(0*FT),'in')
    print "Wing Area     : ", AsUnit( Wing.S, 'in**2' )
    print "Wing Lift     : ", Wing.Lift_LO
    print
    print "Wing Weight : ", AsUnit( Wing.Weight, 'lbf' )
    print "Wing MOI    : ", AsUnit( Wing.MOI(), 'slug*ft**2' )
   
    #Wing.WriteAVLWing('MonoWing.avl')
        
#     Wing.Draw3DWingPolars(fig=2)
#     Wing.Draw2DAirfoilPolars(fig=2)
#  
#     Wing.WingWeight.DrawRibs = False
#     Wing.WingWeight.DrawDetail = False
#     Wing.WingWeight.Draw(fig = 1)
     
    Wing.Draw3DWingPolars(fig=4)
    Wing.Draw2DAirfoilPolars(fig=5)
    Wing.Draw(fig = 1)
    pyl.show()