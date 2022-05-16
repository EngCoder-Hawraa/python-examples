# هذا الموقع مهم لهذا الموضوع
# https://seaborn.pydata.org/generated/seaborn.violinplot.html
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
plt.figure(figsize=(4,8))


# g = sns.catplot(x="sex", y="total_bill",hue="smoker", col="time",
#                 data=data, kind="violin", split=True,height=4, aspect=.7)


# planets = sns.load_dataset("planets")
# ax = sns.violinplot(x="orbital_period", y="method",
#                     data=planets[planets.orbital_period < 1000],
#                     scale="width", palette="Set3")

sns.violinplot(x="day", y="total_bill",data=data)


# sns.violinplot(x="day", y="total_bill", hue="sex",
#     data=data, palette="Set2", split=True,
#     scale="count", inner="stick",scale_hue=False, bw=.2)


# sns.violinplot(x="day", y="total_bill", hue="smoker",
#     data=data, palette="Set2", split=True,
#     scale="count", inner="stick",scale_hue=False, bw=.2)


# sns.violinplot(x="time", y="total_bill",data=data)
plt.show()