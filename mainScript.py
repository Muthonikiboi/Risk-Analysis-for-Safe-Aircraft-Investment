#Fuctions for grouping columns together nad determining the number of accients occurring due to different conmditions

# Reference:
# https://www.geeksforgeeks.org/how-to-reset-index-after-groupby-pandas/
# https://stackoverflow.com/questions/59699487/how-does-pandas-groupby-and-reset-index-change-the-dataframes-index
import pandas as pd

def groups(df, columns, rename = "No of Accidents"):
  #Group by specific columns
  grouped = df.groupby(columns).size().reset_index(name = rename)
  #Sort to find the riskiest depending on specified conditions
  return grouped.sort_values(by = rename, ascending = False)