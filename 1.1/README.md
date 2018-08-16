# Regression issues related to data preprocessing:

## Assumptions in regression

->There exists a linear and additive relationship between dependent (DV) and independent variables (IV). 
By linear, it means that the change in DV by 1 unit change in IV is constant. 
By additive, it refers to the effect of X on Y is independent of other variables.

->There must be no correlation among independent variables. 
Presence of correlation in independent variables lead to Multicollinearity. 
If variables are correlated, it becomes extremely difficult for the model to determine the true effect of IVs on DV.

->The error terms must possess constant variance. Absence of constant variance leads to heteroskedestacity.

->The error terms must be uncorrelated i.e. error at ∈t must not indicate the at error at ∈t+1. 
Presence of correlation in error terms is known as Autocorrelation. 
It drastically affects the regression coefficients and standard error values since they are based on 
the assumption of uncorrelated error terms.

->The dependent variable and the error terms must possess a normal distribution.

## Mathematical concepts

Mathematically, regression uses a linear function to approximate (predict) the dependent variable given as:

                                          Y = βo + β1X + ∈
where, Y - Dependent variable
X - Independent variable
βo - Intercept
β1 - Slope
∈ - Error

βo and β1 are known as coefficients. 

Y - This is the variable we predict
X - This is the variable we use to make a prediction
βo - This is the intercept term. It is the prediction value you get when X = 0
β1 - This is the slope term. It explains the change in Y when X changes by 1 unit. 
∈ - This represents the residual value, i.e. the difference between actual and predicted values.

      β1 = Σ(xi - xmean)(yi-ymean)/ Σ (xi - xmean)² where i= 1 to n (no. of obs.)

                       βo = ymean - β1(xmean)
                       
error estimates:

Residual Sum of Squares (RSS) - ∑[Actual(y) - Predicted(y)]²

Explained Sum of Squares (ESS) - ∑[Predicted(y) - Mean(ymean)]²

Total Sum of Squares (TSS) - ∑[Actual(y) - Mean(ymean)]²

