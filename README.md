# 🚲 Jan-May 2025: Citi Bike Report

## Overview

The Citi Bike is a bike service in NYC for people to use and travel places. Customers have the option to purchase a membership or pay-per-ride. They can select from two bikes, classic or electric. More information on memberships is [here](https://citibikenyc.com/pricing). 

This report will use public [data](https://citibikenyc.com/system-data) and focus on the year 2025 from January to May. The dataset contains trip information such as start/end time, station, and bike.

## Understand the Project Pipeline

1. **Download the data files** - Get trip data from the public S3 [bucket](https://s3.amazonaws.com/tripdata/index.html) and store into a local directory called **`/data`**

2. **Merge the csv's** - Create a Python script (**`code/merge_csv.py`**) to locate the trip data and concat them into one excel file

3. **Preprocess the raw data** - Transform the dataset (**`notebook/preprocess.ipynb`**) by handling missing values, data inconsistencies, and more  

4. **Load Data into Power BI** - Import data files into Power BI for report building and visualizations 

## Power BI Report

**Objective**: Understand trip behavior and the usage of bikes across NYC.

### Questions

- How did the number of trips change?
    - MoM (Month-over-month)
    - Weekdays 
    - Hourly
- Where do riders start and end rides?
- What is the distribution of the trip duration?
    - Is it left or right skewed? Normal?
- Key differences between riders with and without a membership?