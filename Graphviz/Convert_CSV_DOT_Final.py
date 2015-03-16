#!/usr/bin/python
from random import randint
import sys
import pandas as pd


csv_file = sys.argv[1]
dot_file = sys.argv[2]
rpt_file = sys.argv[3]

#
# The arguments for this are: 
# csv_input file - trimmed down CSV file fo ra particular thread
# dot_output file - the dot file that will be written for reading by Graphviz
# rpt_file - the report file that is output from Gephi 



csv_input = open(csv_file,'r')
dot_output = open(dot_file,'w+')
rpt_df = pd.read_csv(rpt_file)

app_list = []
entity_list = []

dot_output.write("digraph dsgl2 { \n")
dot_output.write("rankdir=LR;\n")

# Point of origin

for label in rpt_df[rpt_df["In-Degree"] == 0]["Label"]:
	dot_output.write((" \"%s\" [shape=box,style=filled,color=green];") % (label))

# Sink

for label in rpt_df[rpt_df["Out-Degree"] == 0]["Label"]:
	dot_output.write((" \"%s\" [shape=box,style=filled,color=red];") % (label))

# EigenVector Centrality

for label in rpt_df[rpt_df["Eigenvector Centrality"] == rpt_df["Eigenvector Centrality"].max()]["Label"]:
	dot_output.write((" \"%s\" [shape=box,style=filled,color=blue];") % (label))

# PageRank

for label in rpt_df[rpt_df["PageRank"] == rpt_df["PageRank"].max()]["Label"]:
	dot_output.write((" \"%s\" [shape=box,style=filled,color=blue];") % (label))


for data in csv_input:
    (Source,Target,Label) =  data.strip().split(',')

    if(Source != 'Source'):
        dot_output.write("\"%s\" -> \"%s\" [ label = \"%s\" ];\n" % (Source,Target,Label))
dot_output.write("}\n")
dot_output.close()
