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
for i in range(114563,138760):
    values = data[i]
    ra = values[4]
    dec = values[5]
    name = i
    #print name
    if name == 3514:
        continue
    votable = parse('/media/shaun/Research/Scarlata/Data/Hubble/VO/'+str(name)+'_ra('+str(ra)+')_dec('+str(dec)+').csv')
    for resource in votable.resources:
        for table in resource.tables:
            data1 = table.array['URL']
    for j in data1:
        if 'wfc3' in j:
            if 'f475x' in j or 'f475w' in j:
                url = j
                location = name
                if 'f475x' in j:
                    fil = 'f475x'
                if 'f475w' in j:
                    fil = 'f475w'
                break
    try:
        url
    except NameError:
        continue
    else:
        print url
        print name
        if fil == 'f475w':
            os.chdir("/media/shaun/Research/Scarlata/Data/Hubble/Fits/WFC3/F475W")
        elif fil == 'f475x':
            os.chdir("/media/shaun/Research/Scarlata/Data/Hubble/Fits/WFC3/F475X")
        subprocess.call(["wget","-O",str(location)+"_ra("+str(ra)+")_dec("+str(dec)+")_filter("+str(fil)+").fit",str(url)])
    del url
    del name
    del fil
os.chdir("/media/shaun/Research/Scarlata/Code")