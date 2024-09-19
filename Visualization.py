import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("tips")
print(df)

# Distribution plots
# histplot
sns.histplot(x="total_bill",data=df,kde=False,bins=3)
plt.show()

# jointplot
sns.jointplot(x="total_bill",y="tip",data=df,kind="hex")
plt.show()

# pairplot
sns.pairplot(df,hue="smoker")
plt.show()

# rugplot and kedplot

sns.rugplot(x="total_bill",data=df)
sns.kdeplot(x="total_bill",data=df)
plt.show()

# categorical data plots
# boxplot
sns.barplot(x="day",y="tip",data=df,hue="sex")
plt.show()

# countplot
sns.countplot(x="time",data=df,hue="sex",stat="percent")
plt.show()

# boxplot
sns.boxplot(x="smoker",y="tip",data=df,hue="sex")
plt.show()

# violinplot
sns.violinplot(x="smoker",y="tip",data=df,hue="sex",split=True)
plt.show()

# stripplot
sns.stripplot(x="smoker",y="tip",data=df,hue="sex",dodge=True)
plt.show()

# swarmplot
sns.swarmplot(x="smoker",y="tip",data=df,hue="sex",dodge=True)
plt.show()


# violinplot and swarmplot
sns.violinplot(x="day",y="total_bill",data=df,hue="sex",split=True)
sns.swarmplot(x="day",y="total_bill",data=df,hue="sex",dodge=True)
plt.show()

# catplot
sns.catplot(x="day",y="total_bill",data=df,kind="box")
plt.show()

# boxplot
sns.boxplot(df)
plt.show()

# matrix plots and correlation matrix

df=sns.load_dataset("flights")
print(df)
pvtable=pd.pivot_table(values="passengers",index="year",columns="month",data=df)
print(pvtable)
sns.heatmap(pvtable,cmap="viridis",linecolor="white",linewidths=2)
plt.show()

# corr
file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\Data-Visualization-with-Seaborn\file.csv'
df=pd.read_csv(file_path)
print(df.corr())

sns.heatmap(df.corr(),cmap="viridis",linecolor="white",linewidths=2,annot=True)
plt.show()

# gridplot
df=sns.load_dataset("iris")
print(df)
a=sns.PairGrid(data=df,hue="species")
a.map_diag(plt.hist)
a.map_upper(plt.scatter)
a.map_lower(sns.kdeplot)
plt.show()

# pairplot
sns.pairplot(df,hue="species")
plt.show()


import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

# Facetgrid

df=sns.load_dataset("tips")
print(df)
a=sns.FacetGrid(data=df,row="time",col="smoker",hue="sex")
a.map(sns.scatterplot,"total_bill","tip")
plt.show()

# JointGrid

df = sns.load_dataset("tips")
g = sns.JointGrid(data=df, x="total_bill", y="tip",hue="sex")
g.plot(sns.scatterplot, sns.histplot)
plt.show()


# regression plots

df = sns.load_dataset("tips")
sns.lmplot(data=df, x="total_bill", y="tip")
plt.show()


df = sns.load_dataset("tips")
sns.lmplot(data=df, x="total_bill", y="tip",hue="sex")
plt.show()


df = sns.load_dataset("tips")
sns.lmplot(data=df, x="total_bill", y="tip",hue="sex",row="time",markers=["o","v"],scatter_kws={"s":100},aspect=0.6)
plt.show()