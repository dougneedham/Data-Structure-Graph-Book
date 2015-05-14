#!/usr/bin/python 
from __future__ import division
import sys
import os
import csv
import argparse
import logging
import logging.config
sys.path.append(".")
import properties

#
# This code adds the time column as the last column of a CSV file that is to be analyzed. 
# Argument 1 is the input file 
# Argument 2 is the output file 
# argument 3 is the length of the grouping for the time argument

lgr = logging.Logger

def init_logger(log_level):
    # configure logging
    if log_level is None:
        log_level = properties.log_level
        
    logging.config.fileConfig("logconfig.ini")
    global lgr
    lgr = logging.getLogger(log_level)

def main():
    parser = argparse.ArgumentParser(description='Add the Time Column to a normal CSV file');
    parser.add_argument("-i", "--infile", help="Input File",required=True)
    parser.add_argument("-o", "--outfile", help="Output File",required=True)
    parser.add_argument("-g", "--grouping", help="Grouping\nNumber of rows that will be grouped together with an integer",type=int,default=50)
    parser.add_argument("-q","--quote", help = "Quotecharacter to use",default='"')
    parser.add_argument("-d","--delimiter", help = "Delimiter to use",default=',')
    parser.add_argument("-ll", "--loglevel",
                        help="Log Level; 'log_error' logs only error messages to file; 'logs/EntityAnalysisDebug.log' logs all messages to file");
    args = parser.parse_args();
    init_logger(args.loglevel)
    process_file(args.infile,args.outfile,args.grouping,args.delimiter,args.quote)

def process_file(infile_arg,outfile_arg,grouping_arg,delimiter_arg,quotechar_arg):
	outfile  = outfile_arg
	grouping = grouping_arg
	lgr.info("Input  file is: {0}".format(infile_arg))
	lgr.info("Output file is: {0}".format(outfile_arg))
	lgr.info("Grouping    is: {0}".format(grouping_arg))
	lgr.info("Delimiter    is: {0}".format(delimiter_arg))

	index_row = 0
	time = 0
	outfh =	 open(outfile,'wb')
	outwriter = csv.writer(outfh,delimiter=delimiter_arg)
	with open(infile_arg,'r') as csvfile:
		read_data = csv.reader(csvfile,delimiter=delimiter_arg,quotechar=quotechar_arg)
		for row in read_data:
			if (index_row % grouping) == 0:
				time = time + 1
			if index_row == 0:
				row.append('Time')
			else:		
				row.append(str(time))
			outwriter.writerow(row)
			#print(','.join(row))
			index_row = index_row + 1
	outfh.close()
	csvfile.close()

if __name__ == '__main__':
    main()
