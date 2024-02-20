import matplotlib.pyplot as plt
import seaborn as sns

# plot a simple chart-------------
year = [2010, 2011, 2012, 2013, 2014]
orange_yield = [0.892, 0.917, 0.932, 0.941, 0.947]
apple_yield = [0.927, 0.911, 0.901, 0.898, 0.891,]

# improving default styles using seaborn
sns.set_style('darkgrid')

# to change styles directly from matplotlib
# import matplotlib
# matplotlib.rcParams['font.size'] = 14
# matplotlib.rcParams['figure.figsize'] = (9, 5)
# matplotlib.rcParams['figure.facecolor'] = '#00000000'

plt.plot(year, orange_yield, marker='o', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')    # plots the graph
plt.plot(year, apple_yield, marker='x', c='r', ls='--', lw=3, ms=10, alpha=0.5)
# more args: color/linestyle/linewidth/markersize/alpha

plt.figure(figsize=(10, 5))    # change the figure size
plt.plot(year, orange_yield, 's-')     # shorthand for changing marker, color, and ls

plt.xlabel('Year')     # label for x axis
plt.ylabel('Yield (grow per hectare)')      # label for y axis
plt.title('Data of crop yield')     # shows the title of graph
plt.legend(['Orange', 'Apple'])     # show line by its name


plt.show()  # shows the graph in pop-window
