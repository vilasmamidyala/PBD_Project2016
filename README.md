First Part: IntelliJ IDEA 15
In the second phase we have collected Streaming data using a Curl command. The collected tweets were
saved as a JSON file in the local drive. Now we use the IntelliJ IDEA 15 software to write Queries in Scala
by giving the input to the queries from Local drive. We now execute the query and the output of the query
is stored in JSON file.
For visualization we used d3.js, which is a html, css and svg code which give the graphical visualization in
the form of various graphs and charts. The query output file is converted into csv file and is given as input
to the d3.js code for each visualization.
Second Part: IBM Blue mix
This part is developed in IBM Bluemix using the available in- built features of IBM Bluemix. We have used
insights for twitter for collecting tweets on a specific topic. In this project we collected the tweets based
on the keyword such as virat kohli, cricket and dance. These tweets were then stored to DashDB tool
provided by IBM Bluemix. This Dash DB tables were connected to Apache spark instance in the IBM
Bluemix. Spark SQL queries were built on the Scala Notebook and the resultant data was saved in the form
of parquet file. The data which we collected was visualized using the python notebook present in IBM
Bluemix with the help of matplotlib.# PBD_Project2016
