import numpy
import matplotlib
from astropy.io import fits
from astropy.io.votable import parse
import subprocess
import sys
import os


radius = fits.open('/media/shaun/Research/Scarlata/Data/SDSS/Fits/Radius/object_sdss_imaging.fits')
ra_dec = fits.open("/media/shaun/Research/Scarlata/Data/SDSS/Fits/Ra_Dec/gal_info_dr7_v5_2.fit")
#The galaxy we are looking at
location = fits.open('/media/shaun/Research/Scarlata/Data/Hubble/Fits/WFC3/F475W/26359_ra(222.58)_dec(-1.11319)_filter(f475w).fit')
rad = radius[1].data
data = ra_dec[1].data
loc = location[0].header
radius.close()
ra_dec.close()
location.close()
#ra/dec of both
#reference point
loc_ra = loc['RA_TARG']
loc_dec = loc['DEC_TARG']
galaxy = 26359
values = data[galaxy]
#galaxy
ra = numpy.float64(values[4])
dec = numpy.float64(values[5])
#math
dif_ra = ra-loc_ra
dif_dec = dec-loc_dec

print repr(loc)