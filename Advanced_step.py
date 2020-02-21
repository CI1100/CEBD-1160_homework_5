#Load the insurance.csv in a DataFrame using pandas.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

insurance = pd.read_csv('insurance.csv', header=0)

# Explore the dataset using functions like to_string(), columns, index, dtypes, shape, info() and describe().
# Use this DataFrame for the following exercises.
print("Insurance dataframe string:", insurance.to_string())
print("Insurance dataframe columns:", insurance.columns)
print("Insurance dataframe index:", insurance.index)
print("Insurance dataframe dtypes:", insurance.dtypes)
print("Insurance dataframe shapes:", insurance.shape)
print("Insurance dataframe info:", insurance.info())
print("Insurance dataframe describe:", insurance.describe().to_string())

#Print only the column age
insurance_2 = insurance.set_index("age", drop = False)
print('Print column age:', insurance.loc[:,'age'])

#Print only the columns age,children and charges
print('Print 3 columns:', insurance [['age', 'children', 'charges']])
#Print only the first 5 lines and only the columns age,children and charges
print('Print 3 columns and 5 first lines:', insurance.loc [:5,['age', 'children', 'charges']])

#What is the average, minimum and maximum charges ?
print('Min =', insurance['charges'].min().round(2),
      'Average=', insurance['charges'].mean().round(2),
      'Max:', insurance['charges'].max().round(2))

#What is the age and sex of the person that paid 10797.3362. Was he/she a smoker?
selecting_columns = insurance[insurance['charges']==10797.3362]
print("Selecting rows by multiple criteria:", selecting_columns[['age', 'sex', 'smoker']])

 #What is the age of the person who paid the maximum charge?
#selecting_age = insurance_2['charges'].max()
selecting_age = insurance.loc[insurance['charges'].idxmax()]
print('Age of the person who paid the maximum charge:', selecting_age['age'])
#print(insurance.groupby(['age'])['charges'].max())

#How many insured people do we have for each region?
print('Insured people by Region:', insurance.groupby('region')['sex'].count())
#How many insured people are children?
print('How many insured children:', insurance.groupby('sex')['children'].value_counts())     #####C!!!!!!heck how to eliminate ZERO

#What do you expect to be the correlation between charges and age, bmi and children?
      #I assume that correlation between charges and age will be positve and high
      #but positive and low in case of children as insurance fee is usually lower as more people (families) insured

#Using the method corr(), check if your assumptions were correct.
print('Correlation:', insurance.corr())

