
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

df['Electric Range'].fillna(df['Electric Range'].mean())
#Fill missing numerical values (Electric Range) with the mean

df['Electric Utility'].fillna('Unknown')
# Fill missing categorical values (Electric Utility) with 'Unknown'

#d)

