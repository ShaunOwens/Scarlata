import numpy
import matplotlib
from astropy.io import fits
from astropy.io.votable import parse
import subprocess
import sys
import os

radius = fits.open('E:/Scarlata/Data/SDSS/Fits/Radius/object_sdss_imaging.fits')
ra_dec = fits.open("E:/Scarlata/Data/SDSS/Fits/Ra_Dec/gal_info_dr7_v5_2.fit")
#The galaxy we are looking at
location = fits.open('E:/Scarlata/Data/Hubble/Fits/WFC3/F475W/26359_ra(222.58)_dec(-1.11319)_filter(f475w).fit')
rad_info = radius[1].header
rad = radius[1].data
data = ra_dec[1].data
loc = location[1].header
radius.close()
ra_dec.close()
location.close()
#ra/dec of both
#reference point
loc_ra = numpy.float64(loc['CRVAL1'])
loc_dec = numpy.float64(loc['CRVAL2'])
pix_ra = numpy.float64(loc['CRPIX1'])
pix_dec = numpy.float64(loc['CRPIX2'])
#size of pixel
pix_ra_size = numpy.float64(loc['CD1_1'])
pix_dec_size = numpy.float64(loc['CD2_2'])
#galaxy
galaxy = 26359
values = data[galaxy]
ra = numpy.float64(values[4])
dec = numpy.float64(values[5])
#math
dif_ra = ra-loc_ra
dif_dec = dec-loc_dec
dif_pix_ra = dif_ra/pix_ra_size
dif_pix_dec = dif_dec/pix_dec_size
#print repr(loc)
print dif_ra
print dec
print loc_dec
print dif_dec
print dif_pix_ra
print dif_pix_dec
