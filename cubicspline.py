import numpy as np
import scipy.interpolate as sp

f = open('inputPowerSpectrum.dat', "r")
lines = f.readlines()
listbinsx = []
listbinsy = []
for x in lines:
    listbinsx.append(x.split(' ')[0])
    listbinsy.append(x.split(' ')[1])
f.close()

binsx = []
binsy = []

for item in listbinsx:
    binsx.append(float(item))
for item in listbinsy:
    binsy.append(float(item))
    
cs = sp.CubicSpline(binsx, binsy)

binVals = cs(np.arange(0.015, 0.205, 0.01))


with open('interpolatedPowerSpectrum.dat', 'w') as f:
    for item in binVals:
        f.write("%s\n" % item)
print(cs(0.195))
