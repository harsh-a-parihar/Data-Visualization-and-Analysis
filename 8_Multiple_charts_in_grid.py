import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# data1
year = [2010, 2011, 2012, 2013, 2014]
orange_yield = [0.892, 0.917, 0.932, 0.941, 0.947]
apple_yield = [0.927, 0.911, 0.901, 0.898, 0.891,]

# data2
flower_df = sns.load_dataset('iris')

setosa_df = flower_df[flower_df.species == 'setosa']
versicolor_df = flower_df[flower_df.species == 'versicolor']
virginica_df = flower_df[flower_df.species == 'virginica']

# data3
tip_df = sns.load_dataset('tips')

# data4
flight_df = sns.load_dataset('flights').pivot(columns='year', index='month', values='passengers')

# data5
from urllib.request import urlretrieve
urlretrieve('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Red_Kitten_01.jpg/640px-Red_Kitten_01.jpg', 'cat.jpg')
# before image displayed, it has to be read into memory using Python Imaging Library (PIL) module
from PIL import Image
img = Image.open('cat.jpg')   # open image into memory

print('\n')     # gap

# plotting multiple charts in grid-------------
fig, axes = plt.subplots(2, 3, figsize=(10, 10))      # shows plots in grid

# line chart
axes[0, 0].plot(year, orange_yield, 'o--r')     # plotting orange yield
axes[0, 0].plot(year, apple_yield, 'o-b')      # plotting apple yield
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Yield (tons per hectare)')
axes[0, 0].set_title('Yield of Fruits')
axes[0, 0].legend(['Orange', 'Apple'])
plt.tight_layout(pad=3)     # padding between plots

# scatter plot
axes[0, 1].set_title('Sepal Dimension')
sns.scatterplot(x=flower_df.sepal_length,
                y=flower_df.sepal_width,
                hue=flower_df.species,
                s=100,
                ax=axes[0, 1])

# histogram
axes[0, 2].set_title('Distribution of Sepal_width')
axes[0, 2].hist(setosa_df.sepal_width, bins=np.arange(2, 5, 0.25), rwidth=.97, label='Setosa', stacked=True)
axes[0, 2].hist(versicolor_df.sepal_width, bins=np.arange(2, 5, 0.25), rwidth=.97, label='Versicolor', stacked=True)
axes[0, 2].hist(virginica_df.sepal_width, bins=np.arange(2, 5, 0.25), rwidth=.97, label='Virginica', stacked=True)
axes[0, 2].legend(['Setosa', 'Versicolor', 'Virginica'])

# Bar chart
axes[1, 0].set_title('Restaurant Bill')
sns.barplot(x='day', y='total_bill', hue='sex', data=tip_df, ax=axes[1, 0])

# HeatMap
axes[1, 1].set_title('Flight traffic')
sns.heatmap(flight_df, cmap='Blues', ax=axes[1, 1])

# Image
axes[1, 2].set_title('A cat staring')
axes[1, 2].imshow(img)
axes[1, 2].grid(False)
axes[1, 2].set_xticks([])   # hide x axis
axes[1, 2].set_yticks([])   # hide y axis
plt.tight_layout(pad=2)

# to show graph/image
plt.show()
