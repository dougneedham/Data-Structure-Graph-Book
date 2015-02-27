#!/usr/bin/python
from random import randint
import sys

application_file = sys.argv[2]
entity_file = sys.argv[3]


application_input = open(application_file,'r')
entity_input = open(entity_file,'r')

app_list = []
entity_list = []

for data in application_input:
	(app_name,from_app_description) = data.split(',')

	if(app_name != 'Applications'):
		app_list.append(app_name)

for data in entity_input:
	(entity_name) = data.strip()
	entity_list.append(entity_name)

for i in range(0,int(sys.argv[1])):
	from_app_index = randint(0,len(app_list)-1)
	to_app_index = randint(0,len(app_list)-1)
	entity_index = randint(0,len(entity_list)-1)

	# We don't want a self-loop
	#
	if(from_app_index != to_app_index):
		print ("%s,%s,%s") % (app_list[from_app_index],app_list[to_app_index],entity_list[entity_index])

