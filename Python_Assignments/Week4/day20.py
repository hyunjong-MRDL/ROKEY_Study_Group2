import statsmodels.api as sm
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

Xc = sm.add_constant(X)
results = sm.OLS(y, Xc).fit()

intercept, slope = results.params
intercept = intercept.item()
slope = slope.item()

y_pred = [slope * x + intercept for x in X]

plt.title("Linear Regression")
plt.scatter(X, y)
plt.plot(X, y_pred, color="r")
plt.xlabel("x")
plt.ylabel("y")
plt.show()