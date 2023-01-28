# Real Estate Finder

#### Description: Data Engineering Project using Python, Apache Spark, SQL, Databricks and Microsoft Power BI

## Initial Description:

This project is designed to be a Data Engineering Project with mostly back-end python codes and Apache Spark Code in the form of Databricks Notebooks. I made this project to make a Data Engineering Pipeline with relevant stages that are included in the cycle. Like Data Collection, Data Storing, Data Cleaning, etc. The end goal of this project is to be used to make predictions or gather insights on the prices of Real Estate in a certain location.

In this project, I have used a website (Link: https://www.zameen.com/) which is a famous Pakistani Real Estate Website to scrap data from and use that to make a data engineering life cycle.

We can break this project into different stages or files:

1- Scrap.py (Script designed For Scrapping)

2- data.json (Semi-Structured data file which is written after running the script)

3- Apache Spark Project.ipnb (Databricks Notebook styled file)

4- Real Estate Analytics.pbix (Power BI interactive visualization)

We will go through these files in detail one by one.

## 1- Scrap.py

Scrap.py is a python script for scrapping from a Real Estate Website that I mentioned above. I did not want to just get the kaggle or other resources because that data would be structured and would not require any extensive use of Spark. That is why I wanted to gather my own data from a website that would be in either a structured, unstructured, or semi-structured format.

For starters, I used the BeautifulSoup library for Scrapping the data and lxml for parsing. In this script I created a loop that goes over each page and each page with we scrapped as a whole is sent to a function, that function will iterate over each class that is required, and after reaching that class it will go into its text area and scrap that data for example Price, Ad Title, Real Estate Location, etc. Where some attributes are missing like some ads don't have any pictures, in that case, the script will catch AttributeError and will add relevant data to the script. I also have a global variable in the script that is responsible for the number of ads that are written till the end of the main page iterating loop. This global variable will act as a Surrogate Key in our Database Later. There is a total of 8 pages that are accessible on the website and the total ads that are scrapped are approx 100. At the end of the loop, all the data is saved in the form of an array of dictionaries and is later written to a JSON file which we will go through in the next section. This is all for the Scrapping Script, the main challenge in this script for to learn how to tangle with the bs4 library and integrate it with the parser. Also, I had to learn the structure of the whole website in terms of the html file.

## 2- data.json

Let me give a little overview of JSON file formats. JSON is the semi-structured file format and can carry both structured and semi-structured data. I used JSON files because I wanted the data that I scrapped to be semi-structured so that I can put my newly learned Apache Spark skills to use.

If you peek inside the file you will see an array of dictionaries whose key is ads and the rest of the data is enclosed in an array. Each array index represents a different ad and each ad contains its data that is scrapped.

## 3- Apache Spark Project.ipnb

This is Python Notebook-styled file exported from Databricks and the language I have used in that file is Apache Spark. I will go over Apache Spark and Databricks one by one.

Apache Spark: Spark is a Big Data Analytics Tool used to cater to big data needs either batch or streaming data. It is a unified analytics engine for large-scale data processing. Apache Spark provides an interface for programming clusters with implicit data parallelism and fault tolerance. The reason for using spark is that I got into a job as a Data Engineer while completing this course and thought this would be a fun way to explore this language and also a few things along the way.

Databricks: Databricks is a US Software Company founded by the creators of Apache Spark. The reason for using this platform is that it provides ready-made running spark clusters, and it frees us with the hassle of installing spark locally and setting up its dependencies. It is a notebook-styled platform like Jupyter Notebook.

Now let's get to the notebook. I have attached an HTML also a notebook for the same spark code if one doesn't run but I have shown it in the video explanation.

So in Spark, I can use 3 language API Scala, Python, and SQL. As I was already familiar with python so I opted for Python. Python API for spark is called PySpark.

- First I loaded the data.json in Databricks File System normally referred to as DBFS. Saved the path in a variable and read it with JSON API in spark which converted that into a DataFrame object. You can view this in the first cell, better to ipython file in a notebook or it is not correctly open in visual studio code.

- Then I used the explode function on the dataframe to create rows of each ad from an array of ads.

- Then I employed a select statement with col to make get items from each ad and convert it into a structured format.

- After that, I treated each column to represent valid data, like replacing spaces, and converting qualitative data into quantitative data. Exploded the nested dictionaries into further separate columns. I have a title representing each operation in the notebook.

- At df8 I have completed all the relevant data cleaning and cleansing jobs. After that, I can create views, and further dataframes and query them to show specific data that would be relevant for the stakeholder. I have also added some theory knowledge and pictures talking about several aspects of Apache Spark.

Now this table i.e. df8 can be used by Data Analysts or Data Scientists to drive necessary details or these can be used in visualization tools like Tableau, PowerBI, IBM Cognos, etc.

So this ends the complete lifecycle of my Data Engineering Pipeline.

## 4- Real Estate Analytics.pbix

I have selected Power BI as a visualization tool due to its user-friendly nature. Plus, Power BI desktop version is easily accessible from the Windows store and that too comes with a handy set of interactive visualization tools.

Power BI: Power BI is a collection of software services, apps, and connectors that work together to turn your unrelated sources of data into coherent, visually immersive, and interactive insights. Wheather it be an Excel spreadsheet, or a collection of cloud-based and on-premises hybrid data warehouses, Power BI lets you easily connect to your data sources, visualize and discover what's important, and share that with anyone or everyone you want.

So, Now that the table i.e. real_estate was made available to cater valuable insights, I connected Power BI to our data source, Databricks (beta) and successfully loaded.

But, in Databricks community edition clusters are automatically terminated after a set period, with a default of 120 minutes and when a cluster is terminated all state is lost, including all variables, temp tables, caches, functions, objects, and so forth. All of this state will need to be restored when the cluster starts again.

Hence, in order to make it 24/7 accessible in pbix format, after loading the data from databricks, I exported the data in CSV format and then imported the CSV file to begin with the visualization.

- First before loading the CSV file, I used the Power Query editor in order to make some transformations, namely creating conditional column based on Area categories, adding units wherever needed etc.

- Now that the data was transformed, interactive visuals were created like, Lowest Price Offered, Median Price, Most Popular Housing Schemes Available, Total No. of Advertisements etc. On top of that, slicers including Area, No. of Bedroom and No. of Bathroom keeps the visuals more interactive.

- Visuals that were used; Cards, Stacked Bar Chart, Area Chart, Table, Pie Chart, Doughnut Chart, Horizontal Slicers and Vertical Slicers.



<p align="center">
Architecture Diagram
</p>

![alt text](./Architecture Diag.png)
