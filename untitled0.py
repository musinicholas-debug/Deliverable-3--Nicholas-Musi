import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")


# For some plots, it's easier to work with a subset (e.g. top 5 makes)
top_makes = df["Make"].value_counts().head(5).index
df_top = df[df["Make"].isin(top_makes)].copy()

sns.violinplot(data=df_top, x="Electric Vehicle Type", y="Model Year", inner=None)
plt.title("Violin + Scatter: Electric Range by EV Type")
plt.show()