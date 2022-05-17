



from math import *


# IGR formular
from math import *
def Gamma_Ray_index(grlog, grmin,grmax):
    igr = float((grlog-grmin) / (grmax-grmin))
    return igr

# density porosity
def DEN_POR(rhoma, rhob, rhof):
    Denpor=float((rhoma-rhob) / (rhoma-rhof))
    return Denpor




# Water Saturation
def Water_Saturation(RW,RWA,N):
    sw  = float(RW/RWA)**(1/N)
    return sw

#Volume of shale
def Shale_volume(Igr):
    vsh = float(2**(3.71*Igr)-1)*0.083
    return vsh
    
# effective Density Porosity
def EFF_DenPor(vsh,ShPor,Denpor):
    EDenPor= float(Denpor-(ShPor*vsh))
    
    return EDenPor

# effective Neutron Porosity

def EFFNPOR(vsh,SHNPOR,NPOR):
    ENPOR= float(NPOR-(SHNPOR*vsh))
    
    return ENPOR
    

def Porosity(EDenPor,ENPOR):
    NDPOR= float (EDenPor+ENPOR)/2
    return NDPOR


def Water_porosity(WNPOR,WDENPOR):
    WPOR = float (WNPOR+WDENPOR)/2
    return WPOR

def RW_FT(WPOR,A,ro,M):
    RW= float (WPOR**M)*ro/A
    return RW

#Water Resistivity Apparent
from math import *
def APPARENT_WATER_RESISTIVITY(RESD, Denpor, M, A):
    rwa = float(RESD*Denpor**M)/ A 
    return rwa



def SWIR(RW,NDPOR,M,A,N,RT):
    swir= float((A*RW) / (RT*NDPOR**M))**(1/N)
    return swir

#Permeability 

#hdef PERM 
