
from scalar.units import GRAM, gacc, A, V, mAh, IN, LBF
from scalar.units import AsUnit
from Aerothon.ACMotor import ACBattery

Weight = []
Power = []

#Thunder Power 

Turnigy_6Cell_3000_LV = ACBattery()
Turnigy_6Cell_3000_LV.Voltage = 21.2*V
Turnigy_6Cell_3000_LV.Cells = 6 
Turnigy_6Cell_3000_LV.Capacity = 3000*mAh
Turnigy_6Cell_3000_LV.C_Rating = 25
Turnigy_6Cell_3000_LV.Weight = .915*LBF 
Turnigy_6Cell_3000_LV.LWH = (1.375*IN,1.875*IN,6.0*IN) #inaccurate dimensions

Power.append( Turnigy_6Cell_3000_LV.Power() )
Weight.append( Turnigy_6Cell_3000_LV.Weight )

if __name__ == '__main__':
    print AsUnit( Turnigy_6Cell_3000_LV.Imax, 'A' )