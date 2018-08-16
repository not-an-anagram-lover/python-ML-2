# This program is to demonstrate the data pre-processing and extracting for regression algorithms


import numpy as np
import statsmodels.formula.api as sm
import seaborn as sns
sns.set(style="whitegrid")
import pandas as pd

pd.set_option("display.max_columns",10)
import matplotlib.pyplot as plt

class Titanic:
    def __init__(self):
        print("Inside Titanic class")
        self.df=pd.read_csv('titanic3.csv')
        print(self.df.head())
        print("checking correlation \nPearson:\n")

        # Correlation is being checked between Columns to find suitable X to predict value of Y=survival
        # There shouldn't be any correlation between independent variables


        print(self.df.corr(method='pearson'))
        print("checking correlation \nSpearman:\n")
        print(self.df.corr(method='spearman'))
        print("checking correlation \nKendall:\n")
        print(self.df.corr(method='kendall'))

        # We don't really need all of these methods as their result is almost same
        # Above correaltion is between numeeric data only
        # least viable correlation is between survived and sibsp=0.081036; considering kendall corr

        self.data_ext_plot()

    def data_ext_plot(self):
        self.df1=self.df.ix[:,['survived','sibsp']]
        print(self.df1)
        X=self.df.ix[:,0]
        y=self.df.ix[:,1]
        results = sm.ols(formula='survived ~ sibsp',data=self.df1).fit()
        y_pred=results.predict(self.df1[["sibsp"]])
        residual = self.df1["survived"].values-y_pred
        plt.scatter(self.df1[["sibsp"]],residual)
        plt.xlabel("sibsp-a predictor")
        plt.ylabel("Residual")
        plt.show()


t=Titanic()