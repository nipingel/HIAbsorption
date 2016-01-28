#!/usr/env/python

# Small script to convert VEGAS-FITS to filterbank format
# Kaustubh Rajwade

import numpy as np
import pyfits,os,sys
import matplotlib.pyplot as plt

hdulist=pyfits.open(sys.argv[1])

# Section left blank to get header parameters from the file itself



# Getting the data
f=open(sys.argv[1]+".sto","ab")

iter = len(hdulist[5].data)


for i in range(iter-3):
  table = (hdulist[5].data)[i]
  data = table[2]
  data1 = np.array(data)
  data_fin1 = np.array(data1[0:8192])  # Left Polarization
  data_fin2 = np.array(data1[16384:24576]) # Right Polarization
  data_final = np.sqrt((data_fin1*data_fin1)+ (data_fin2*data_fin2)) # Summing dual pol data

  data_final.tofile(f,sep="",format="%f") #storing the values in a new file



# Closing the file


f.close()

#plt.figure()
#plt.plot(data_final1,'b-')
#plt.show()
