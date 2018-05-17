import numpy
import matplotlib
from astropy.io import fits
from astropy.io.votable import parse
import subprocess
import shlex

#Fits file input and value labeling#
mass = fits.open("Data/SDSS/Fits/Mass/totlgm_dr7_v5_2.fit")
ra_dec = fits.open("Data/SDSS/Fits/Ra_Dec/gal_info_dr7_v5_2.fit")
#mass.info()
#ra_dec.info()
info = ra_dec[1].columns
data = ra_dec[1].data
mass.close()
ra_dec.close()

#Loop for getting fits files from HST#
#927552
for i in range(0,927552):
    values = data[i]
    ra = values[4]
    dec = values[5]
    name = i
    #Create invironment for files.
    #Input shell script and parameters.
    