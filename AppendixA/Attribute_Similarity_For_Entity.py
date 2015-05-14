#!/usr/bin/python
from __future__ import division
import csv
import sys
import md5
import json
import numpy as np
import pandas as pd
import argparse
import logging
import logging.config
sys.path.append(".")
import properties

lgr = logging.Logger

def init_logger(log_level):
    # configure logging
    if log_level is None:
        log_level = properties.log_level
        
    logging.config.fileConfig("logconfig.ini")
    global lgr
    lgr = logging.getLogger(log_level)


def get_data_from_file(input_file,delimiter_arg,quotechar_arg):
	#
	# simple function to read data from a csv file. 
	#
	file_handle = open(input_file,'r')
	#content = file_handle.read()
	#content = pd.read_csv(input_file)
	content = csv.reader(file_handle,delimiter=delimiter_arg,quotechar=quotechar_arg)
	#file_handle.close()
	
	return content
def calc_euclid(input_dict,from_key,to_key):
	#
	# function to calculate the euclidean distance between the mu/sigma combination of a source to a target
	#
	if from_key == to_key:
		result = 0
	else:
		result =  np.sqrt(np.square(input_dict[from_key]['mu']-input_dict[to_key]['mu'])+np.square(input_dict[from_key]['sigma']-input_dict[to_key]['sigma']))
	return result
def similarity_report(input_dict,outfile):
	#
	# lets report on our data.
	#
	
	# setting up the formatting for pandas
	#
	output_line = []
	for keys in input_dict: 
		output_line.append(keys)
	
	# Lets have the output be sorted
	#
	output_line.sort()
	# predefine our result array
	#
	result_array = np.ndarray(shape=(len(output_line),len(output_line)))
	
	# loop through the input dictionary twice to get all combinations of source and target
	#
	for okeys in input_dict:
		for ikeys in input_dict:
			result_array[output_line.index(okeys),output_line.index(ikeys)] =calc_euclid(input_dict,okeys,ikeys)
	
	# print the result as a data frame. 
	# pandas does this nicely
	#
	pd.set_option('display.max_columns', 8)
	outputDF = pd.DataFrame(result_array,output_line,output_line)			
	print outputDF
	outputDF.to_csv(outfile)
	return


	
def main():
    	parser = argparse.ArgumentParser(description='Add the Time Column to a normal CSV file');
    	parser.add_argument("-i", "--infile", help="Input File",required=True)
    	parser.add_argument("-o", "--outfile", help="Output File",required=True)
    	parser.add_argument("-q","--quote", help = "Quotecharacter to use",default='"')
    	parser.add_argument("-d","--delimiter", help = "Delimiter to use",default=',')
    	parser.add_argument("-ll", "--loglevel",
                        help="Log Level; 'log_error' logs only error messages to file; 'logs/EntityAnalysisDebug.log' logs all messages to file");
    	args = parser.parse_args();
    	init_logger(args.loglevel)
	# predefine a few variables
	attribute_data = get_data_from_file(args.infile,args.delimiter,args.quote)
	master_dict = {}
	array_dict = {}
	small_dict = {}	
	header = []

	#for line in attribute_data.split('\n'):
	for line in attribute_data:
		data = []
		row = ""
		#line_length = len(line.split(','))
		line_length = len(line)
		if(line_length > 1): 
			data = line
			if(data[line_length-1] == 'Time'):
				for attribute in line:
					# populate the header list - which is made up of the attribute names we are studying
					#
					header.append(attribute)
			else:
				# Create a new entry in the master dictionary for the individual time record. 
				# Since we are using time as an index here, the time should be an integer, preferrably starting with 1
				
				if data[line_length-1] not in master_dict:
					# Initialize a new subdictionary
					#
					master_dict[data[line_length-1]] = {}
					# create dictionaries for row and column data
					#
					master_dict[data[line_length-1]]['rows'] = {}
					master_dict[data[line_length-1]]['cols'] = {}
					for index in range(0,line_length-1):
						master_dict[data[line_length-1]]['cols'][header[index]] = {}
				
				for index in range(0,line_length-1):
					row += data[index]
					# These are the individual column values from the CSV file that are put into the dictionary for analysis
					#
					if data[index] not in master_dict[data[line_length-1]]['cols'][header[index]]:
						master_dict[data[line_length-1]]['cols'][header[index]][data[index]]=md5.new(data[index]).hexdigest()
					
				digest = md5.new(row).hexdigest()
				# we are doing an MD5 simply for efficiency. It could be a string concatonated together, but the MD5 reduces memory use for larger sets
				# of data we may be analyzing.
				if digest not in master_dict[data[line_length-1]]['rows']:
					master_dict[data[line_length-1]]['rows'][digest] = {}

	# Now that we have captured all of the details from the file into the master dictionary, 
	# we need to go through and transform the data into a simple dictionary we can do our analysis on
	#				
	for keys in master_dict:
		for key2 in master_dict[keys]['cols']:
			if key2 not in array_dict:
				array_dict[key2] = []
			array_dict[key2].append(len(master_dict[keys]['cols'][key2])/len(master_dict[keys]['rows']))

	for keys in array_dict:
				if keys not in small_dict: 
					small_dict[keys] = {}
				# The heart of the matter. 
				# the standard deviation of uniqueness for a column across all time provided in this sample
				# and the mean of uniqueness for a column across all time provided in this sample.
				small_dict[keys]['mu'] = np.mean(array_dict[keys])
				small_dict[keys]['sigma'] = np.std(array_dict[keys])

	# print out our report. 
				
	similarity_report(small_dict,args.outfile)	
if __name__ == '__main__':
	main()

