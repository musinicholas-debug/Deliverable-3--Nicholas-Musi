#Programming in science
#December 7th, 2025
#Tiago Bortoletto Vaz
#"'Nicholas Musi"'

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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


# Strategy B and C: 
df["Postal Code"]= df["Postal Code"].fillna(df["Postal Code"].mean())
df["Model Year"]= df["Model Year"].fillna(df["Model Year"].mean())
df["Electric Range"]= df["Electric Range"].fillna(df["Electric Range"].mean())
df["Base MSRP"]= df["Base MSRP"].fillna(df["Base MSRP"].mean())
df["Legislative District"]= df["Legislative District"].fillna(df["Legislative District"].mean())
df["DOL Vehicle ID"]= df["DOL Vehicle ID"].fillna(df["DOL Vehicle ID"].mean())


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



print(df.isnull().sum())
#Check missing values per column
#Explanation of code: I used fillna to replace all numeric values missing with the median and all categorical values missing with unknown.

#d)
#For my specific data set I have no collums that I need to convert.


#3 Univariable non-graphical EDA

# Separate numeric and categorical columns
numeric_col = df.select_dtypes(include=["number"]).columns
categorical_col = df.select_dtypes(exclude=["number"]).columns
#Explanation of code: I split both my numerical and categorical columns into their own variables.

#numerical
for i in numeric_col:
    if i in df:
        print(df[i].mean())
        print(df[i].median())
        print(df[i].mode().values)
        print(df[i].std())
        print(df[i].var())
        print(df[i].skew())
        print(df[i].kurt())
        print(df[i].quantile([0.25, 0.50, 0.75]))

#categorical
for i in categorical_col:
    if i in df:
        print(df[i].value_counts())
        print(df[i].value_counts(normalize=True))



#4 Univariable graphical EDA

#The two numerical value collum that dont't apply for this part would be "postal code" for the simple reason that it is random and doesn't follow any perticular pattern and therefore won't lead to any interesting questions.
#Also the DOl Vehicle ID would not apply because it is random as well. 

#plots
df_numerical = ["Electric Range", "Model Year","Base MSRP","Legislative District"]
for i in df_numerical:
     sns.displot(data=df, x=i, hue="Electric Vehicle Type", kind="hist", bins=30, stat="density", kde=True)


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
#explanation of code: This code selects the five most common car manufacturers in the dataset and then creates a smaller dataset containing only the vehicles from those top brands.
#First, top_makes = df["Make"].value_counts().head(5).index counts how many times each manufacturer appears, takes the top five, and extracts just their names. Then, df_top = df[df["Make"].isin(top_makes)].copy() filters 
#the original dataset to keep only the rows where the “Make” is one of those top five manufacturers, creating a clean copy. This smaller dataset is useful for making clearer, less cluttered plots and comparisons.


#6.1.Visualizing statistical relationships (5 plots):

#a) 
sns.relplot(data=df_top , x="Make", y="Electric Range", col="Electric Vehicle Type")
plt.suptitle("Make vs Electric Range by EV Type", y=1.02)
plt.show()


#b)
sns.relplot( data=df_top, x="Model Year", y="Electric Range", hue="Electric Vehicle Type", size="Base MSRP", col="Make")
plt.suptitle("Electric Range vs Model Year (5 variables)", y=1.02)
plt.show()

#C)
# Filter out outliers above $400,000
df_filtered = df[df["Base MSRP"] <= 100000]

sns.lmplot( data=df_filtered, x="Base MSRP", y="Electric Range", hue="Electric Vehicle Type")
plt.title("Linear Regression: Electric Range vs Base MSRP")
plt.show()
              

#6.2.Visualizing categorical data (10 plots):
    
#a) 
sns.stripplot(data=df_top, x="Electric Vehicle Type", y="Electric Range", jitter=False)
plt.title("Linear Regression: Electric Range vs Model Year")
plt.show()

#b)
#sns.swarmplot(data=df_top, x="Electric Vehicle Type", y="Electric Range", hue="Make", s=0.001)
#plt.title("Beeswarm: Electric Range by EV Type and Make")
#plt.show()
#This specific is not loading with my data set im assuming since its too big the spyder program cant load it I left it in # for you to see it.
#sns.catplot(data=df_top, x="Model Year", y="Electric Range", hue="Make", kind="swarm", s=0.0001)
#C:\Users\Nicholas\AppData\Local\spyder-6\envs\spyder-runtime\Lib\site-packages\seaborn\categorical.py:3399: UserWarning: 99.1% of the points cannot be placed; you may want to decrease the size of the markers or use stripplot.
#warnings.warn(msg, UserWarning)
#after trying both swarmplot and catplot this plot will not load I have tried many different variables and all don't work the error I am getting is above.

#c)
sns.boxenplot(data=df_top, x="Make", y="Electric Range")
plt.title("Boxenplot: Electric Range by Make")
plt.xticks(rotation=45)
plt.show()

#d)
sns.violinplot(data=df_top, x="Electric Vehicle Type", y="Electric Range", hue="Make", split=True)
plt.title("Split Violin: Electric Range by EV Type and Make")
plt.show()


#e)
sns.violinplot(data=df_top, x="Electric Vehicle Type", y="Model Year", inner=None)
plt.title("Violin + Scatter: Electric Range by EV Type")
plt.show()

#f)
sns.pointplot(data=df_top, x="Model Year", y="Electric Range", hue="Electric Vehicle Type", ci=90, linestyles="--")
plt.title("Point Plot: Electric Range by Year and EV Type (90% CI)")
plt.xticks(rotation=45)
plt.show()

#g)
sns.countplot(data=df, x="Electric Vehicle Type")
plt.title("Number of Vehicles by Type")
plt.xticks(rotation=15)
plt.show()

#6.3. Visualizing bivariate distributions (3 plots):
    
#a)
heatmap_data = pd.crosstab(pd.cut(df["Model Year"], bins=10), pd.cut(df["Electric Range"], bins=10))

sns.heatmap( heatmap_data, cmap="crest")
plt.title("Heatmap: Model Year vs Electric Range")
plt.xlabel("Electric Range bins")
plt.ylabel("Model Year bins")
plt.show()
#explanation of code: This code creates a heatmap that shows how vehicles are distributed across different Model Year ranges and Electric Range ranges. 
#First, pd.cut(df["Model Year"], bins=10) divides all model years into 10 equal-sized bins (for example: 2000–2002, 2002–2004, etc.). 
#The same is done for electric range using pd.cut(df["Electric Range"], bins=10), which groups the electric ranges into 10 interval categories. 
#The pd.crosstab() function then counts how many vehicles fall into each combination of these two categories, creating a two-dimensional table. 
#This table is saved as heatmap_data.


#b)
sns.displot(data=df, x="Model Year", y="Electric Range", kind="kde", fill=False, levels=10, thresh=0.05, hue="Electric Vehicle Type"   )
plt.suptitle("Bivariate KDE: Model Year vs Electric Range", y=1.02)
plt.show()


























