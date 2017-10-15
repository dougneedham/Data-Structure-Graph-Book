import xmltodict

with open('dw_ga_gen.erd') as fd:
    doc = xmltodict.parse(fd.read())

print("Source,Target,Edge_Label")
for i in range(1,len(doc['diagram']['relations']['relation']) )  :
	source_index = doc['diagram']['relations']['relation'][i]['@pk-ref']
	target_index = doc['diagram']['relations']['relation'][i]['@fk-ref']
	edge_label = doc['diagram']['relations']['relation'][i]['@name']
	#print(i)
	#print(source_index)
	#print(doc['diagram']['entities']['data-source']['entity'][(int(source_index)-1)]['@name'])
	#print(target_index)
	string_to_print = '{0},{1},{2}'.format(doc['diagram']['entities']['data-source']['entity'][(int(target_index)-1)]['@name'],
		doc['diagram']['entities']['data-source']['entity'][(int(source_index)-1)]['@name']
		,edge_label)
	print(string_to_print)
#doc['diagram']['entities']['data-source']['entity'][int(source_index)]['@name']