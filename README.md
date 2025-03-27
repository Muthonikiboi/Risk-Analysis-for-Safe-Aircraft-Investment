# Risk-Analysis-for-Safe-Aircraft-Investment
This project analyzes ✈️ Accident data to identify the lowest risk aircraft for a company getting started into the aviation industry.Using data driven insights it helps provide recommendations to help aviation decision make informed purchasing decision. 

## Background and Overview
### 👩🏻‍💻 Author


### 🤔 Problem Statement
The company is expanding in to new industries to diversify its portfolio. Specifically, they are interested in purchasing and operating airplanes for commercial and private enterprises, but do not know anything about the potential risks of aircraft. You are charged with determining which aircraft are the lowest risk for the company to start this new business endeavor. You must then translate your findings into actionable insights that the head of the new aviation division can use to help decide which aircraft to purchase.

### {} Tech Stack 
_Python(Pandas, Matplotlib)_

_Tableau(For Interracive Dashboards)_

_VisualStudio Code/ Jupyter Notebook_

### 🔗 Installations
To set up the project environment you must install depensencies used in the project;

`pip install pandas matplotlib`

## ⛁ Data Structure Overview
The Data in this project is obtained from the National Transportation Safety Board that includes aviation accident data from 1962 to 2023 about civil aviation accidents and selected incidents in the United States and international waters.

On kaggle: [Dataset](https://www.kaggle.com/datasets/khsamaha/aviation-accident-database-synopses)

The dataset contains records like:
- Model
- Number of engines
- Purpose of Flight
- etc.
  
  This code shows us all the columns we have: `df.columns`

  Output:

  `Index(['Event.Id', 'Investigation.Type', 'Accident.Number', 'Event.Date',
       'Location', 'Country', 'Latitude', 'Longitude', 'Airport.Code',
       'Airport.Name', 'Injury.Severity', 'Aircraft.damage',
       'Aircraft.Category', 'Registration.Number', 'Make', 'Model',
       'Amateur.Built', 'Number.of.Engines', 'Engine.Type', 'FAR.Description',
       'Schedule', 'Purpose.of.flight', 'Air.carrier', 'Total.Fatal.Injuries',
       'Total.Serious.Injuries', 'Total.Minor.Injuries', 'Total.Uninjured',
       'Weather.Condition', 'Broad.phase.of.flight', 'Report.Status',
       'Publication.Date'],
      dtype='object')`
  
The dataset has a total of __88889 Rows__ and __31 Columns__
  
## 🈺 Data Cleaning And Processing
The first step in cleaning and data is checking for null values and duplicates.The data has no duplicates but has missing values.
Use `df.isnull().sum()` to check for null values.

`Event.Id                      0
Investigation.Type            0
Accident.Number               0
Event.Date                    0
Location                     52
Country                     226
Latitude                  54507
Longitude                 54516
Airport.Code              38640
Airport.Name              36099
Injury.Severity            1000
Aircraft.damage            3194
Aircraft.Category         56602
Registration.Number        1317
Make                         63
Model                        92
Amateur.Built               102
Number.of.Engines          6084
Engine.Type                7077
FAR.Description           56866
Schedule                  76307
Purpose.of.flight          6192
Air.carrier               72241
Total.Fatal.Injuries      11401
Total.Serious.Injuries    12510
Total.Minor.Injuries      11933
Total.Uninjured            5912
Weather.Condition          4492
Broad.phase.of.flight     27165
Report.Status              6381
Publication.Date          13771
dtype: int64`

This data has so many missing values first handle missing values either:
- Dropping Columns with more than __50000 missing values__: `thresh = 50000`
- Impute with **MODE** `['Injury.Severity','Aircraft.damage','Amateur.Built','Number.of.Engines','Engine.Type','Purpose.of.flight','Weather.Condition','Report.Status']`
- Impute with **UNKNOWN** `['Location','Country','Registration.Number','Make','Model','Airport.Code','Airport.Name','Broad.phase.of.flight']`
- Impute with **0** `['Total.Uninjured','Total.Minor.Injuries','Total.Fatal.Injuries','Total.Serious.Injuries','Publication.Date']`

  Imputing with ** *Unknown* ** and ** *O* ** helps avoid introducing bias into tha data hence retaining data as it is,

More to that we can also process data by grouping eg Make and Model , Engine type and Number of engines with their relations to number of accidents to had more data.

## 📊📈 Insights Deep Dive
1. Top 10 Accidents from grouping `Make` and `Model`
2. Accidents by Number of Engines
3. Fatal injuries per flight purpose
4. Total Accidents over Years
5. Tableau Dashboard 1
6. Tableau DAshboard 2

## 📃 Recommendation
