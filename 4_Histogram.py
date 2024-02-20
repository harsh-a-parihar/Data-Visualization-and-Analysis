import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# histogram represents the data for single type of variable--------------

# load data into pandas dataframe
flower_df = sns.load_dataset('iris')    # loads pre-defined dataset 'flower' in seaborn

# sepal_width
print(flower_df.sepal_width)
# check range of sepal_width
print(flower_df.describe())

# create histogram
plt.title('Distribution of Sepal width')    # customize style
plt.hist(flower_df.sepal_width, bins=5)    # specifying the number of bins
# or
plt.hist(flower_df.sepal_width, bins=np.arange(2, 5, 0.25), rwidth=0.95)     # arrange between two interval using numpy

# multiple histogram (taking species)
setosa_df = flower_df[flower_df.species == 'setosa']
versicolor_df = flower_df[flower_df.species == 'versicolor']
virginica_df = flower_df[flower_df.species == 'virginica']
print(setosa_df)

plt.hist(setosa_df.sepal_width, rwidth=.95, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(versicolor_df.sepal_width, rwidth=.95, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.legend(['setosa', 'versicolor'])

# stack histograms
plt.title('Distribution of sepal_width among diff. species')
plt.hist(setosa_df.sepal_width, bins=np.arange(2, 5, 0.25), rwidth=.97, label='Setosa', stacked=True)
plt.hist(versicolor_df.sepal_width, bins=np.arange(2, 5, 0.25), rwidth=.97, label='Versicolor', stacked=True)
plt.hist(virginica_df.sepal_width, bins=np.arange(2, 5, 0.25), rwidth=.97, label='Virginica', stacked=True)

plt.legend(['setosa', 'versicolor', 'virginica'])

# to show graph
plt.show()
