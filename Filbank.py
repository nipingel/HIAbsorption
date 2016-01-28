#!/env/usr/python

# Code to make a pseudo filterbank file which could be read by other SIGPROC codes
#KR@AO 6Jul2014


import numpy as np
import os,sys
import struct


telescope_ids = {"Fake": 0, "Arecibo": 1, "Ooty": 2, "Nancay": 3,
                 "Parkes": 4, "Jodrell": 5, "GBT": 6, "GMRT": 7,
                 "Effelsberg": 8}

machine_ids = {"WAPP": 0, "PSPM": 1, "Wapp": 2,"AOFTM": 3,
               "BCPM1": 4, "OOTY": 5, "SCAMP": 6,
               "GBT Pulsar Spigot": 7, "SPIGOT": 7, "PUPPI": 8 ,
               "GUPPI": 9,"PA":10,"VEGAS": 11}



def prep_string(string):
    return struct.pack('i', len(string))+string

def prep_double(name, value):
    return prep_string(name)+struct.pack('d', float(value))

def prep_int(name, value):
    return prep_string(name)+struct.pack('i', int(value))

#def infodata_to_sigproc_header:
hdr = prep_string("HEADER_START")
hdr += prep_int("telescope_id", 6)
 #   if (len(inf.instrument.split()) > 1):
  #      if (inf.instrument.split()[0]=="Multibeam"):
  #          hdr += prep_int("machine_id", machine_ids["SCAMP"])
  #  else:
hdr += prep_int("machine_id",8)
hdr += prep_int("data_type", 1) # 1 = filterbank, 2 = timeseries
hdr += prep_string("source_name")
hdr += prep_string("B2020+28")
#hdr += prep_int("barycentric", 1)
#hdr += prep_int("pulsarcentric", 0)
hdr += prep_double("src_raj",202227.06)
   # if inf.dec_d > 0.0:
    #    hdr += prep_double("src_dej", 12345)
   # else:
hdr += prep_double("src_dej", 285423.104)
hdr += prep_int("nbits", 32)
hdr += prep_int("nifs", 1)
hdr += prep_int("nchans", 8192)
hdr += prep_double("fch1", 1428.85)
hdr += prep_double("foff", -0.00206)
hdr += prep_double("tstart", 56857.659)
hdr += prep_double("tsamp", 0.049516)
#hdr += prep_double("refdm", 96)
hdr += prep_string("HEADER_END")
#    return hdr

#inf = presto.read_inffile(basefilenm)
basefilename = str(sys.argv[1])
outfile = open(basefilename+".fil", "wb")
outfile.write(hdr)
outfile.close()
os.system("cat %s >> %s"%(sys.argv[1], basefilename+".fil"))
