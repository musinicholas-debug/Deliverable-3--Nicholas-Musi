
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")


#Preliminary steps

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
print(df.duplicated())
print(df.drop_duplicates())

#c)
print(df.isnull().sum())
#Check missing values per column

df["Electric Range"]= df["Electric Range"].fillna(df["Electric Range"].mean())
df["Postal Code"]= df["Postal Code"].fillna(df["Postal Code"].mean())
df["Model Year"]= df["Model Year"].fillna(df["Model Year"].mean())
df["Electric Range"]= df["Electric Range"].fillna(df["Electric Range"].mean())
df["Base MSRP"]= df["Base MSRP"].fillna(df["Base MSRP"].mean())
df["Legislative District"]= df["Legislative District"].fillna(df["Legislative District"].mean())
df["DOL Vehicle ID"]= df["DOL Vehicle ID"].fillna(df["DOL Vehicle ID"].mean())
#Fill missing numerical values with the mean

df["County"]= df["County"].fillna('Unknown')
df["City"]= df["City"].fillna('Unknown')
df["State"]= df["State"].fillna('Unknown')
df["Make"]= df["Make"].fillna('Unknown')
df["Model"]= df["Model"].fillna('Unknown')
df["Electric Vehicle Type"]= df["Electric Vehicle Type"].fillna('Unknown')
df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"]= df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].fillna('Unknown')
df["Vehicle Location"]= df["Vehicle Location"].fillna('Unknown')
df["Electric Utility"]= df["Electric Utility"].fillna('Unknown')
df["2020 Census Tract"]= df["2020 Census Tract"].fillna('Unknown')
# Fill missing categorical values with 'Unknown'

#Explanation: Keep all rows to preserve large dataset integrity. Use mean imputation for numeric columns to avoid data loss. Use “Unknown” for categorical columns to maintain clarity while keeping categorical values. 

#d)
df["Model Year"] = pd.to_numeric(df["Model Year"])
df["Electric Range"] = pd.to_numeric(df["Electric Range"])
#Model Year should be numeric for trend or range calculations and electric range should also be numeric, since missing or non-numeric entries may have been stored as strings.
