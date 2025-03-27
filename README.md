# Risk-Analysis-for-Safe-Aircraft-Investment
This project analyzes ✈️ Accident data to identify the lowest risk aircraft for a company getting started into the aviation industry.Using data driven insights it helps provide recommendations to help aviation decision make informed purchasing decision. 

## Background and Overview
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

There are two Datasets in the `./Data` folder(Raw data and Cleaned Data)
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
1. Top 10 Accidents from grouping `Make` and `Model` ![Image](https://github.com/user-attachments/assets/5bf57f26-f343-4b6b-8ef9-c0ad447b6777)
2. Accidents by Number of Engines ![Image](https://github.com/user-attachments/assets/7ef820b7-ad61-4b3a-bd4f-2f67a793cab7) This image is a clear indication that most accident occur to planes with one engine.The more the number of engines the less the likelihood of accident occurrences.
3. Fatal injuries per flight purpose ![Image](https://github.com/user-attachments/assets/522594d7-025b-44d5-867a-475418b8bcb5) This image indicates that Personal, business and instructural record the highest numbet of fatalities when accidents occur.
4. Total Accidents over Years ![Image](https://github.com/user-attachments/assets/35022d87-6086-46b5-ba52-d8f288c1c7f8)
5. Tableau Dashboard 1 [Dashboard Server Link](https://public.tableau.com/app/profile/joy.kiboi/viz/AeroAccidentsBook1/Dashboard1?publish=yes)  ![Image](https://github.com/user-attachments/assets/0e139bd7-833c-4f92-b6ed-a7fcd1099510)
   The dashboards are a summary of the plots.
7. Tableau DAshboard 2  [Dashboard Server Link](https://public.tableau.com/app/profile/joy.kiboi/viz/AeroAccidentsBook2/Dashboard2?publish=yes) ![Image](https://github.com/user-attachments/assets/069fe61b-bc61-429c-988a-37f3b5564cda)


## 📃 Recommendation
1. Prioritize buying multi-engine aircrafts as they have lower accident Risks
2. Focus on commercial(Public) and Cargo(Ferry) aviation where there are lower risks.
3. Implement strict  Operational controls for private services.
4. Invest in planes with advanced landing features as during landing most planes have highest risks

## 🏁 Conclusion
Diving into the aviation indurstry with a data driven solution suggests that ,invest in multi engine commercial(Public) and Cargo(Ferry) crafts as they pose lower risks compared to personal and intructional aircrafts.

### 👩🏻‍💻 Author
[Github](https://github.com/Muthonikiboi)
[LinkedIn](https://www.linkedin.com/in/joy-kiboi-917661278/)
