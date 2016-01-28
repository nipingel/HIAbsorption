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
data_fin = []
data_fin1 = []
data_fin2 = []
#for i in range(iter):
table = (hdulist[5].data)[iter-1]
data = table[2]
print len(data)
 # element1 = data[0]
  #element2 = data[1]
  #element3 = data[2]
  #data_fin = data1[0::4]
  #data_fin.tofile(f,sep="",format="%f")
 # data_fin.append(element1)
  #data_fin1.append(element2)
  #data_fin2.append(element3)
# Closing the file

plt.figure()
#plt.plot(data_fin,'r-')
plt.plot(data[0:163840],'b-')
#plt.plot(data_fin2,'g-')
plt.show()

f.close()

