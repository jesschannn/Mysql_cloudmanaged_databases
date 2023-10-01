# Mysql_cloudmanaged_databases

# Azure Setup Documentation 

1. Opened and logged into Microsoft Azure
2. Typed in the search bar "Azure Database for MySQL Servers"
3. Clicked on "create" and chose the flexible server option
4. Created a new resource group and a server name
5. Ensured that all of the selections I made in the basics, networking, and security tag aligned with the parameters of the assignment. The parameters for the Azure Database were: flexible server, burstable tier, B1S or B1MS compute, public IP address, and 0.0.0.0/0 network
6. Went to the Review and Create tab to double check that everything was correct
7. Deploy the MySQL instance
8. Connect MySQL workbench and Azure Database with the information from Azure

# GCP Setup Documentation

1. Navigate to the GCP console
2. Create a new project by clicking "New Project" and make sure that the project is being created under the correct location / organization
3. Click on the hamburger bar on the left side of the screen and click on SQL
4. Create a MySQL instance and enable API
5. Fill out Instance ID field and password
6. Click on Enterprise MySQL instance, sandbox edition, shared core, 1vCPU 0.614 GB, public IP address, and 0.0.0.0/0 network
7. Review all configurations to ensure they are correct and click "create" button
8. Deploy the MySQL instance
9. Connect MySQL workbench and GCP with the information from GCP

# Experience with MySQL Workbench

I enjoyed learning and getting to use MySQL Workbench. It was a little confusing at first because I kept forgetting to put the name of the database in the proper quotes. Furthermore, I initially had trouble connecting Azure to MySQL workbench because I couldn't determine what to put in the "hostname" section. After conferring with my classmates, I realized that the server name on Azure belonged to the "hostname" section on MySQL. However, navigating through MySQL workbench went by seamlessly. It was easy to create the tables and remembering to "command return" every table to ensure that it would show up on the ERDs. When I had to create my table, I looked at the other tables that were already provided to determine how to structure the table, as well as what data type would be best utilized for each aspect of my table. Creating the ERDs themselves were successful, but I did have to double check the arrows on the ERDs for all the tables to make sure the right types of arrows were being utilized to represent the relationships between each table. Screenshots of the commands and ERDs are available in "gcp_mysqlworkbench_setup" and "azure_mysqlworkbench_setup" folders.

# Difficulties with the Assignment 

I had difficulty trying to connect the dummy data I created using pandas to the MySQL database. When I was creating the dummy data, I initially attempted to put all of the dummy data from the patients, medications, patient_medications, and patient_visits tables into one dataframe. After doing some research, I didn't find anything. I was also rewatching one of the lecture videos from class to see if that was possible, but I was also unable to find anything. I decided to split the dummy data up into four dataframes; one dataframe for each table. 

## First Attempt 

I googled different methods on how to connect a pandas dataframe to SQL. The first code I saw was:

`DataFrame.to_sql(name, con, *, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)`

I changed some aspects of the code like "dataframe" to "df1", added the name of the table, and added the type of connection. In my dummy.py file, df1 represents the dummy data I created for the patients table. The result was: 

```df1.to_sql(name='patients', con=engine, *, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)```

Below is an image of the code I used as well as the error message in the console. I had also tried removing the quotes from the name to see if that was the syntax error, but it didn't work. 

![image](https://github.com/jesschannn/Mysql_cloudmanaged_databases/assets/123782059/267b7c2e-3277-42bf-8620-58db21f55ae6)

## Second Attempt 

The second link I clicked and tried to follow was: <https://saturncloud.io/blog/inserting-a-pandas-dataframe-into-sql-server-with-python/>. First, I had to install pyodbc. I added ```import pyodbc``` and I did ```pip install pandas pyodbc```, but the message I got was "Defaulting to user installation because normal site-packages is not writeable" and "requirements already met". Below is a picture of what I attempted and the message. 

![image](https://github.com/jesschannn/Mysql_cloudmanaged_databases/assets/123782059/17007f73-b3de-40c4-b342-ceec68838688)

Then I googled "pyodbc" and went on this website: <https://pypi.org/project/pyodbc/>. I tried to do ```brew install unioxbc``` since I have a Mac. I also tried variations of installing pyodbc. Below is a screenshot my attempt and the results. 

![image](https://github.com/jesschannn/Mysql_cloudmanaged_databases/assets/123782059/799acc5f-c616-4d28-9a66-aef77e425c8f)

I followed the second step, which was:

```
# Create a connection string
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=your_server;'
    r'DATABASE=your_database;'
    r'UID=your_username;'
    r'PWD=your_password;'
)

# Establish a connection
conn = pyodbc.connect(conn_str)
```

I replaced ```your_server```, ```your_database```, ```your_username```, and ```your_password``` with my own information. When I did this step, I made sure to include the dummy.py file into my .gitignore file. 

![image](https://github.com/jesschannn/Mysql_cloudmanaged_databases/assets/123782059/555fbc8f-3303-4123-afb0-4f6fde6dad94)



