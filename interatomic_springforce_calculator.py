import math #import math

#declare initial variables
molar_mass = 1.063e-25 #kg/atom
density = 8900.0 #kg/m^3
length = 3.0 #m
#ONLY USE FOR SQUARE CROSS SECTION ;cs = (0.11/100) #cross-section length in m;
Acs = 0.0015*0.0027 #m^2 (cross sectional area)
mass = 44.0 #kg
dlength = (0.002639) #m

#calculate distance between atoms
Vatom = molar_mass/density
datom = (Vatom) ** (1/3)
print('Distance between atoms is ', format(datom, "10.3E"))

#calculate amounts of series and parallel spring chains
series = length/datom
print('Number of serial springs is ',format(series, "10.3E"))

parallel = Acs/((datom)**2)
print('Number of parallel springs is ',format(parallel, "10.3E"))

#calculate interatomic spring force
Kwire = (mass*9.8)/dlength
Katom = (Kwire*series)/parallel
print('Interatomic spring force is ', format(Katom, "0.2f"), 'N/m')

#start speed of sound calculations
vsound = math.sqrt(Katom/molar_mass) * datom
print('Speed of sound through the material is ',format(vsound, "10.3E"))