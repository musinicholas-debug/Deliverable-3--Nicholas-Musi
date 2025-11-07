
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")


#Preliminary steps

#a)
print(df["Electric Range"].value_counts().head(10))
print(df.shape)
print(df.info())
print(df.describe())


#b)
print(df.duplicated())
print(df.drop_duplicates())

