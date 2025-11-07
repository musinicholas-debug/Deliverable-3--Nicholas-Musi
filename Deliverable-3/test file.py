import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the filtered CSV dataset
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")


print(df.isnull())
