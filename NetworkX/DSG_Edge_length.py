#!/usr/bin/python
#
# This code is used to calculate the length of an Edge_Label for a data Structure Graph. 
# Written by Doug Needham
#
import sys
import networkx as nx
input_file = sys.argv[1]

def get_data_from_file(input_file):
	file_handle = open(input_file,'r')
	content = file_handle.read()
	file_handle.close()
	return content

def add_edge_to_graph(graph,source,target,edge_label):
	graph.add_edge(source,target,Edge_Label = edge_label)

def path_length(dict,edge_label):
	newgraph = nx.Graph()
	for key in dict:
		if dict[key] == edge_label:
			newgraph.add_edge(key[0],key[1])
	try:
		diameter = nx.diameter(newgraph)
		print 'Longest path for ',edge_label, ' = ', diameter
	except nx.exception.NetworkXError:
		print 'Longest path for ',edge_label, ' is infinite'
	

if __name__ == '__main__':
	dsg_data = get_data_from_file(input_file)
	dsg = nx.Graph()
	for line in dsg_data.split('\n'):
		if(len(line)> 0):
			(source,target,label) = line.split(',')
			if (source != 'Source'):
				add_edge_to_graph(dsg,source,target,label)

	labels = nx.get_edge_attributes(dsg,'Edge_Label')
	edge_label_dict = {}
	for key in labels:
		if labels[key] not in edge_label_dict:
			edge_label_dict[labels[key]] = 1

	for key in edge_label_dict:
		path_length(labels,key)





