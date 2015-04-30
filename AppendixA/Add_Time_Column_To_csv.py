#!/usr/bin/python 
from __future__ import division
import sys
import os
import csv
#
# This code adds the time column as the last column of a CSV file that is to be analyzed. 
# Argument 1 is the input file 
# Argument 2 is the output file 
# argument 3 is the length of the grouping for the time argument
filename = sys.argv[1]
outfile  = sys.argv[2]
grouping = sys.argv[3]
grouping = int(grouping)
index_row = 0
time = 0
outfh = open(outfile,'wb')
outwriter = csv.writer(outfh,delimiter = ',')
with open(filename,'r') as csvfile:
	read_data = csv.reader(csvfile,delimiter=',',quotechar='"')
	for row in read_data:
		if (index_row % grouping) == 0:
			time = time + 1
		if index_row == 0:
			row.append('Time')
		else:	
			row.append(str(time))
		outfh
		outwriter.writerow(row)
		#print(','.join(row))
		index_row = index_row + 1
