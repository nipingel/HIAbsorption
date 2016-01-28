#!/usr/env/python

# Small script to concatenate VEGAS-FITS files to filterbank for further analysis using PRESTO

# Kaustubh Rajwade
# 11Sep 2015

# 15Sep 2015 NP added functionality to loop through all IFs to create filterbank files of OH+HI lines
import numpy as np
import pyfits,os,sys
import glob

# Acquiring the arguments

files = [item for item in glob.glob('*.fits')]
filesorted=sorted(files)

# Check for arguments
if(len(sys.argv) != 2):
 print "Found incorrect number of arguments. usage: python <program> <basefilename> "
 exit()
# Set bandpass increment (#channels per IF)
chanInc = 8192 #channels
bandInc = 4 # bandpasses per IF
# Getting the data
for ifNum in range(0,5):
	f = open(sys.argv[1]+'_'+str(ifNum)+'.sto', "ab")
	dataIndex = ifNum*chanInc*bandInc
	for i in range(len(files)):
		file = str(filesorted[i])
     		print file+' '+'IF'+str(ifNum)
  		hdulist = pyfits.open(file)
  		iter = len(hdulist[5].data)
		for i in range(iter):
			table = (hdulist[5].data)[i]
    			data = table[2]
    			data1 = np.array(data)
    			data_fin1 = np.array(data1[dataIndex:dataIndex+chanInc])  # Left Polarization
			data_fin2 = np.array(data1[dataIndex+(2*chanInc):dataIndex+(3*chanInc)]) # Right Polarization
    			data_final = np.sqrt((data_fin1*data_fin1)+ (data_fin2*data_fin2)) # Summing dual pol data
			data_final.tofile(f,sep="",format="%f") #storing the values in a new file
	# Closing the file
	f.close()

#plt.figure()
#plt.plot(data_final1,'b-')
#plt.show()
