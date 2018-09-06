#Data visualization in pandas
#Univariate plots:
#-techniques you can use to understand each attribute independently

#histograms
import matplotlib.pyplot as plt
import pandas
import numpy
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
data=pandas.read_csv(url, names=names)
data.hist()
plt.show()
#density plots
data.plot(kind='density',subplots=True, layout=(3,3), sharex=False)
plt.show()
#box and whisker plots
data.plot(kind='box',subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()

#Multivarite plots
#-interaction between multiple variables

#correlation matrix plot
correlations=data.corr()
fig=plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(correlations, vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=numpy.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
plt.show()

#scatter plot
from pandas.plotting import scatter_matrix
scatter_matrix(data)
plt.show()