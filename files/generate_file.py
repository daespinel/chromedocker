#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# Author: David Espinel


import os
import sys

from argparse import ArgumentParser

sys.path.append("../")
from shared_params import *

address = "192.168."
countSites=4
count=0
sites=1

#-------------------------------------------------------------------------------
# Argument parser
#-------------------------------------------------------------------------------
def process_opt():
	usage = """generate_file.py [options]\nType "generate_file.py --help" for more info"""
	parser = ArgumentParser(usage=usage)
	parser.add_argument("--input", dest="input", required=True, type=str, \
							help="Input latency file")

	opt = parser.parse_args()
	return opt

# ------------------------------------------------------------------------------
# LOCAL FUNCTIONS
# ------------------------------------------------------------------------------
# Produce the textual output for Apache configuration
def hname2hosts(hname, proto,loss):
	global address
	global countSites
	global count
	global sites
	output = ""
	words= hname.split()
	address = "192.168."
	if (proto == 0):
		x= (0 * 128) + loss + (count * 3)
	else:
		x= (1 * 128) +  loss + (count * 3)
	address = address + str(x)+"."
	address = address + str(countSites)
	output = output + "\n".join([address + " "+ words[0] ])
	output = output + "\n"
	return output


# ------------------------------------------------------------------------------
#** MAIN **#
if __name__ == '__main__':


	# Get parameters from keyboard
	params = process_opt()

	# Initializing output files
	class OutputFile():
		def __init__(self):
			self.hosts1 = open('00'+'.hosts', 'w')
			self.hosts2 = open('01'+'.hosts', 'w')
			self.hosts3 = open('02'+'.hosts', 'w')
			self.hosts4 = open('10'+'.hosts', 'w')
			self.hosts5 = open('11'+'.hosts', 'w')
			self.hosts6 = open('12'+'.hosts', 'w')
			self.write_hosts_header()

		def close(self):
			self.hosts1.close()
			self.hosts2.close()
			self.hosts3.close()
			self.hosts4.close()
			self.hosts5.close()
			self.hosts6.close()

		def write_hosts_header(self):
			self.hosts1.write(LOCAL_HOST)
			self.hosts1.write("\n")
			self.hosts2.write(LOCAL_HOST)
			self.hosts2.write("\n")
			self.hosts3.write(LOCAL_HOST)
			self.hosts3.write("\n")
			self.hosts4.write(LOCAL_HOST)
			self.hosts4.write("\n")
			self.hosts5.write(LOCAL_HOST)
			self.hosts5.write("\n")
			self.hosts6.write(LOCAL_HOST)
			self.hosts6.write("\n")


	output = {}
	output["00"] = OutputFile()
#	output["01"] = OutputFile("01")
#	output["02"] = OutputFile("02")
#	output["10"] = OutputFile("10")
#	output["11"] = OutputFile("11")
#	output["12"] = OutputFile("12")
	

	# Read the hostnames file and generate configuration files
	for hname in open(params.input, 'r').read().splitlines():
		if hname.startswith('#'):
			print "header"
		else:
			output["00"].hosts1.write(hname2hosts(hname,0,0))
			output["00"].hosts2.write(hname2hosts(hname,0,1))
			output["00"].hosts3.write(hname2hosts(hname,0,2))
			output["00"].hosts4.write(hname2hosts(hname,1,0))
			output["00"].hosts5.write(hname2hosts(hname,1,1))
			output["00"].hosts6.write(hname2hosts(hname,1,2))
			
			if(countSites<255):
#				address = address + str(countSites)
				countSites +=1
#				print "count sites", countSites
			if(countSites == 255):
				count +=1
				countSites = 1
			sites +=1

	for i in output.values():
		i.hosts1.close()
		i.hosts2.close()
		i.hosts3.close()
		i.hosts4.close()
		i.hosts5.close()
		i.hosts6.close()
	
