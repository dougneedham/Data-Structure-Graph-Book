#!/usr/bin/python
from random import randint
import sys

csv_file = sys.argv[1]
dot_file = sys.argv[2]


csv_input = open(csv_file,'r')
dot_output = open(dot_file,'w+')

app_list = []
entity_list = []

dot_output.write("digraph dsgl2 { \n")
for data in csv_input:
    (Source,Target,Label) =  data.strip().split(',')

    if(Source != 'Source'):
        dot_output.write("\"%s\" -> \"%s\" [ label = \"%s\" ];\n" % (Source,Target,Label))
dot_output.write("}\n")
dot_output.close()
