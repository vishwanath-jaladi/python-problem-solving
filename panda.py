# Program: Pandas Basics
# Description: This program demonstrates basic Pandas operations by creating
# a DataFrame, selecting columns, calculating the mean, filtering rows,
# and finding the maximum value.

import pandas as pd
data = {
    "Time": ["8 AM", "9 AM", "10 AM", "11 AM"],
    "Energy": [20, 23, 27, 31],
    "Temperature": [24, 25, 26, 28]
}
df=pd.DataFrame(data)
print(df["Temperature"])
print((df["Temperature"].mean()))
print(df[df["Energy"]>25])
print(df[df["Temperature"]>=26])
print(df["Energy"].max())