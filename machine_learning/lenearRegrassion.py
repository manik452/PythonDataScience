import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets

df = pd.read_csv("housing.csv")

# print(df.head())
print("==============df.info()=================")
print(df.info())
print("==============df.describe()=================")
print(df.describe())
print("==============df.columns()=================")
print(df.columns)
print("==============sn=================")
print(df["longitude"])
# print(sns.displot(df['longitude']))
print(df.columns)
X, y = datasets.load_iris(return_X_y=True)
# x = df[['longitude', 'latitude', 'housing_median_age', 'total_rooms',
#         'total_bedrooms', 'population', 'households', 'median_income',
#         'median_house_value', 'ocean_proximity']]
# y = df['longitude']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=110
)
# print(X_train.shape)
lm = LinearRegression()
lm.fit(X_train, y_train)
print(lm.intercept_)
lm.coef_
# X_train.columns
cdf = pd.DataFrame(lm.coef_, X.columns, columns=["Coeff"])
print(cdf.head)
