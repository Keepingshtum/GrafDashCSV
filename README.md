# GrafDashCSV
The repo for taking a csv file and visualising it with grafana!



#Building this app

Would not recommend doing this as the sql connection, the grafana iframe and other things are hardcoded to local host. 

Have not had the time to do a docker build either, might get around to it in the future!



#Screenshots

Coming soon!



#About the app:

Built on flask, I'm using a webpage to take csv files from the user. Then, the app connects to the sql database, cleans out the data and puts it in a table 'mytable' 

This table is linked to grafana as a datasource, and can therefore be queried to visualise various things like average calories per meal and the breakdown of the nutrients.





### Built for GSoC 2020 by Anant Shukla!
