import argparse
import xmltodict
import time


class arg:
	pass

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('vertabelo_file',help='File created as output from the verabelo reverse engineering process.')
	args = parser.parse_args(namespace=arg)
	timestr = time.strftime("%Y%m%d_%H%M%S")
	nodes_file = 'dsg_nodes_{}.csv'.format(timestr)
	edges_file = 'dsg_edges_{}.csv'.format(timestr)
	

	with open(arg.vertabelo_file) as fd:
		doc = xmltodict.parse(fd.read())
	node_output = open(nodes_file,"w+")
	node_output.write("Id,Label\n")
	for i in range(0,len(doc['DatabaseModel']['Tables']['Table']) )  :
		table_id = doc['DatabaseModel']['Tables']['Table'][i]['@Id']
		table_name = doc['DatabaseModel']['Tables']['Table'][i]['Name']
		string_to_print = '{0},{1}\n'.format(table_id,table_name)
		#print(string_to_print)
		node_output.write(string_to_print)
	node_output.close()

	edge_output = open(edges_file,"w+")
	edge_output.write("Source,Target,Edge_Label\n")
	for i in range(0,len(doc['DatabaseModel']['References']['Reference']) )  :
		source_table_id = doc['DatabaseModel']['References']['Reference'][i]['PKTable']
		target_table_id = doc['DatabaseModel']['References']['Reference'][i]['FKTable']
		edge_label = doc['DatabaseModel']['References']['Reference'][i]['Name']
		string_to_print = '{0},{1},{2}\n'.format(source_table_id,target_table_id,edge_label)
		#print(string_to_print)        
		edge_output.write(string_to_print)
	edge_output.close()


if __name__ == '__main__':
	main()
