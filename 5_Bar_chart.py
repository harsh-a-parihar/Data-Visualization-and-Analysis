import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# bar chart similar to line chart----------

year = range(2000, 2006)
orange = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
apples = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

# create bar chart and line chart together
plt.bar(year, orange)
plt.plot(year, apples, 's--r')
plt.title('Yield of Oranges')

# stack bar
plt.bar(year, apples)
plt.bar(year, orange, bottom=apples)
plt.legend(['orange', 'apples'])

# bar chart with average

# new dataset(tips)
tip_df = sns.load_dataset('tips')
print(tip_df)

# find avg bill on days using bar
bill_avg_df = tip_df.groupby('day')[['total_bill']].mean()
print(bill_avg_df)
plt.bar(bill_avg_df.index, bill_avg_df.total_bill)  # bar chart

# drawing same avg bill on days using seaborn
sns.barplot(x='day',
            y='total_bill',
            hue='smoker',
            data=tip_df)

# to show graph
plt.show()
