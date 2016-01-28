#/usr/env/python
#Python script to make an ON and OFF pulse bandpasss from a dedispersed filterbak file

# Kaustubh Rajwade
#23Oct2015

import glob,os,sys
import numpy as np
import pyfits

if(len(sys.argv) != 9):
  print  "incorrect usage, usage: python Make_bandpass.py  filename on1 on2 off1 off2 period tsamp num_spec"
  exit()

# Sorting the files

#files = [item for item in glob.glob('*.fits')] 
#filesorted = sorted(files)

# Taking arguments
on1 = int(sys.argv[1])
on2 = int(sys.argv[2])
off1 = int(sys.argv[3])
off2 = int(sys.argv[4])
period = float(sys.argv[5])
tsamp = float(sys.argv[6])
size = float(sys.argv[7])

bins = int(period/tsamp)

num_spec = sys.argv[7]
num_pulses = num_spec/bins

# opening the file

f = open(sys.argv[1],"rb")

f.seek(size,0)                   #Size of header

data = np.fromfile(f,dtype='float',count=-1,sep="")

#Adding up the spectra to create ON and OFF spectrum

for i in range(num_pulses):

  a = on1*i
  b = on2*i
  c = off*i
  d = off*i
 
  On_spec += np.sum(data[:,a:b],axis = 0)
  Off_spec += np.sum(data[:,c:d],axis=0)


On_spec_mean = On_spec/num_pulses
Off_spec_mean = Off_spec/num_pulses




