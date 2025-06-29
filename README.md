# 🚲 2025 Citi Bike Report (Jan-May)

## Overview

Citi Bike is a transportation service in NYC for everyone to use and travel places. Customers have the option to purchase a membership or pay-per-ride. They are also offered two bikes, classic or electric. More information on plans and pricing is [here](https://citibikenyc.com/pricing). 

This report will use [public data](https://citibikenyc.com/system-data) and focus on the year of 2025. The dataset contains trip information such as start/end time, station, and bike.

## Understanding the Project Pipeline

1. **Download relevant data files** - Get trip data from the public s3 [bucket](https://s3.amazonaws.com/tripdata/index.html) and store into a local directory **`/data`**

2. **Merge the csv's** - Create a Python script (**`code/merge_csv.py`**) to locate the trip data and concat them into one excel file

3. **Preprocess the raw data** - Transform the dataset (**`notebook/preprocess.ipynb`**) by handling missing values, data inconsistencies, and more  

4. **Load Data into Power BI** - Import data files into Power BI for data analysis and visualizations 

## Power BI Dashboard