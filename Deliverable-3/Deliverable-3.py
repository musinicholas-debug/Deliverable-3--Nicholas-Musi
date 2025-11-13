#Programming in science
#November 4th 2025
#Tiago Bortoletto Vaz
#"'Nicholas Musi"'

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")


#2 Preliminary steps

#a)
print(df["Electric Range"].value_counts().head(10))
##using the head module combined with value_counts it gives us the top 10 Electric Range. 
print(df.shape)
#Showing that I have 250659 rows and 17 columns
print(df.info())
#Shows the number of non empty values for each column and gives the type of number/object it is.
print(df.describe())
#Gives you the  count, mean, standart deviation, min, 25%, 50%, 75% and max for column. 


#b)
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.shape)


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
#Explanation of code: for this part I had originaly coded it column by column creating a massive bunch of code, to simplify I used a loop. To start I split both my numerical and categorical columns into their own variables.
#To then use them in the loop using the col function that I found and researched online. It let create a loop for the numerical and categorical values respectively allowing me to replace them with the median and "unknown".



#Keep all rows to preserve large dataset integrity. Use mean imputation for numeric columns to avoid data loss. Use “Unknown” for categorical columns to maintain clarity while keeping categorical values. 


#d)
#For my specific data set I have no collums that I need to convert.

#3 Univariable non-graphical EDA


#4 Univariable graphical EDA

#The two numerical value collum that dont't apply for this part would be "postal code" for the simple reason that it is random and doesn't follow any perticular pattern and therefore won't lead to any interesting questions.
#Also the DOl Vehicle ID would not apply because it is random as well. 

#plots (add bins size)
df_numerical = ["Electric Range", "Model Year","Base MSRP","Legislative District"]
for i in df_numerical:
     sns.displot(data=df, x=i, hue="Electric Vehicle Type",kind="kde")


#5 Multivariate non-graphical EDA

#a)
ctab=pd.crosstab(df["Model Year"], df["Electric Range"])
print(ctab.head(10))

ctab2= pd.crosstab(df["Base MSRP"], df["Electric Vehicle Type"])
print(ctab2.head(10))

ctab3= pd.crosstab(df["Electric Utility"], df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"])
print(ctab3.head(10))


#b)
ctab_p=pd.crosstab(df["Model Year"], df["Electric Range"], normalize="index")
print(ctab_p.head(10))

ctab2_p= pd.crosstab(df["Base MSRP"], df["Electric Vehicle Type"], normalize="columns")
print(ctab2_p.head(10))

ctab3_p= pd.crosstab(df["Electric Utility"], df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"], normalize=True)
print(ctab3_p.head(10))


#c)
three_way=pd.crosstab([df["County"],df["Electric Vehicle Type"]] ,df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"], normalize="index")
print(three_way.head(10))



























