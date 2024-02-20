import matplotlib.pyplot as plt
import seaborn as sns

# scatter plot used to plot values of 2 variable on 2-d grid------------

# load data into pandas dataframe
flower_df = sns.load_dataset('iris')    # loads pre-defined dataset 'flower' in seaborn
print(flower_df)

# check species
print(flower_df.species.unique())

# visualize data:

# customize seaborn figure
sns.set_style('darkgrid')
plt.figure(figsize=(10, 5))
plt.title('Sepal Data')

# create line chart
# plt.plot(flower_df.sepal_length, flower_df.sepal_width)     # irregular graph, not efficient

# create scatter plot
sns.scatterplot(x=flower_df.sepal_length,
                y=flower_df.sepal_width,
                hue=flower_df.species,
                s=100)

# to show graph
plt.show()
