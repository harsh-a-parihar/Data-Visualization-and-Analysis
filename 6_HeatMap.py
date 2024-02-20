import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# heatmap used to visualize 2-d data like matrix or table using colors-----------

# new dataset(flights)
flight_df = sns.load_dataset('flights').pivot(columns='year', index='month', values='passengers')    # pivot makes a data into matrix form
print(flight_df)
plt.plot(flight_df.passengers)    # just a line chart

# draw heatmap
plt.title('No. of passengers. (/1000s)')
sns.heatmap(flight_df, fmt='d', annot=True, cmap='Blues')

# to show graph
plt.show()
