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
df[numeric_col] = df[numeric_col].fillna(df[numeric_col].median())
df[categorical_col] = df[categorical_col].fillna("Unknown")

print(df.isnull().sum())
#Explanation of code: for this part I had originaly coded it column by column creating a massive bunch of code, to simplify I used a loop. To start I split both my numerical and categorical columns into their own variables.
#To then use fillna to replace all numeric values missing with the median and all categorical values with unknow.



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

#6 Multivariate graphical EDA

# For some plots, it's easier to work with a subset (e.g. top 5 makes)
top_makes = df["Make"].value_counts().head(5).index
df_top = df[df["Make"].isin(top_makes)].copy()
#explanation of code: 


#6.1.Visualizing statistical relationships (5 plots):

#a) 
sns.relplot(data=df_top , x="Model Year", y="Electric Range", col="Electric Vehicle Type")

#b)
sns.relplot( data=df_top, x="Model Year", y="Electric Range", hue="Electric Vehicle Type", size="Base MSRP", col="Make")

#c)
sns.lmplot( data=df, x="Model Year", y="Electric Range", hue="Electric Vehicle Type", scatter_kws={"alpha": 0.3})

#6.2.Visualizing categorical data (10 plots):
    
#a) 
sns.stripplot(data=df_top, x="Electric Vehicle Type", y="Electric Range", jitter=False)

#b)
sns.catplot(data=df_top, x="Electric Vehicle Type", y="Electric Range", hue="Make", kind="swarm")

#c)

#d)

#e)

#f)

#g)

#6.3. Visualizing bivariate distributions (3 plots):
    
#a)

#b)


























