# Data-Structure-Graph-Book
This is the github repository for the book [Data Structure Graphs](http://www.amazon.com/dp/B00XETTPCI)

A [Data Structure Graph](http://the-data-guy.blogspot.com/2015/02/data-structure-graph-definition.html) is a group of atomic entities that are related to each other, stored in a repository, then moved from one persistence layer to another, rendered as a Graph. 

Essentially it is a way to interpret either a data architecture or a data model as a graph. 
There are a number of metrics that can be gathered in order to quantify the architecural design that this code demonstrates as documented in the book. 

Here are some instructions for trying this yourself: 
1.	Download and install Gephi. 
a.	You will probably need to modify the gephi.conf file to give it more resources		  -J-Xms2048m -J-Xmx8192m -J-Xverify:none  are the settings I use. 
2.	Follow these instructions to set up the Vertabela reverse engineering tool: https://vertabelo.com/blog/reverse-engineering/
3.	Run the attached python code ERD_to_DSG.py vertabelo_file.xml 
4.	This will spit out two files dsg_nodes_datetimestamp.csv, and dsg_edges_datetimestamp.csv 
5.	Open Gephi. 
6.	In Data Laboratory click import spreadsheet
7.	Select the dsg_nodes file. 
8.	Ensure “Import as”: is set to nodes table. 
9.	Select Append to current workspace. 
10.	Click import spreadsheet again.
11.	Select the dsg_edges file. 
12.	“Import as:” should be set to edges table. 
13.	Select Append to current workspace. 
14.	Select Overview. 
15.	For layout choose “Force Atlas 2” 
16.	For the Behavior alternatives click “Dissuade Hubs”,”LinLog Mode”, and “Prevent Overlap”.
17.	Click Start, then let it run for a few seconds till it is visually appealing click Stop when done.
18.	On the right you should see a statistics window. 
19.	Choose Connected Components. A dialog box will pop up, just choose directed and click OK. 
20.	A graph will be displayed, just close that. 
21.	Go back to Data Laboratory. 
22.	Sort on the Component ID, and compare this with the table names and subject areas you may have had. 
23.	These Component ID’s are groups of tables that have a high affinity for each other. Essentially, these are the subject areas of the data model. 
24.	So long as good foreign keys (real or virtual) are defined. Gephi will identify the “clusters of tables that belong to the same subject area.



Please leave comments or questions as you read through the book!

Thank you, 

Doug Needham

