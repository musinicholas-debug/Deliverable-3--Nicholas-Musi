import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")
#c)
print(df.isnull().sum())
#Check missing values per column

# Separate numeric and categorical columns
numeric_col = df.select_dtypes(include=["number"]).columns
categorical_col = df.select_dtypes(exclude=["number"]).columns


# Strategy:
# Fill missing numerical values with the mean
# Fill missing categorical values with 'Unknown'
for col in numeric_col:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

for col in categorical_col:
    df[col] = df[col].fillna("Unknown")
    
print(df.isnull().sum())