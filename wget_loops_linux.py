import numpy
import matplotlib
from astropy.io import fits
from astropy.io.votable import parse
import subprocess
import sys
import os

#Fits file input and value labeling#
mass = fits.open("/media/shaun/Research/Scarlata/Data/SDSS/Fits/Mass/totlgm_dr7_v5_2.fit")
ra_dec = fits.open("/media/shaun/Research/Scarlata/Data/SDSS/Fits/Ra_Dec/gal_info_dr7_v5_2.fit")
#mass.info()
#ra_dec.info()
info = ra_dec[1].columns
data = ra_dec[1].data
mass.close()
ra_dec.close()
#Loop for getting fits files from HST#
#927552
os.chdir("/media/shaun/Research/Scarlata/Data/Hubble/VO")
for i in range(105123,927552):
    values = data[i]
    ra = values[4]
    dec = values[5]
    name = i
    subprocess.call(["wget","-O",str(name)+"_ra("+str(ra)+")_dec("+str(dec)+").csv","http://hla.stsci.edu/cgi-bin/hlaSIAP.cgi?POS="+str(ra)+","+str(dec)+"&SIZE=0.05&inst=WFC3&format=image/fits,application/tar,text/html"])
os.chdir("/media/shaun/Research/Scarlata/Code")