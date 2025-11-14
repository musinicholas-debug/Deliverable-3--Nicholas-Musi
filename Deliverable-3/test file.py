import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

top_makes = df["Make"].value_counts().head(5).index
df_top = df[df["Make"].isin(top_makes)].copy()


