# 1.Create a heatmap to visualize correlations in a dataset

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_json("opendata.json")
data.corr()
print(data)

sns.heatmap(data.corr(),annot=True,linewidths=2,linecolor="black",cmap="rainbow")
plt.show()

# 2.Generate a pairplot to study relationships across multiple variables


data=pd.read_json("opendata.json")
data.corr()
print(data)
a=sns.pairplot(data,hue="Duration",palette="rainbow")
plt.show()