#Importing header files

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the file from path and store in variable data
data = pd.read_csv(path)
data.hist(['Rating'])
data=data[data['Rating']<=5]

# Check the Null values in data
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())

# Concat the columns those who have maximum missing values 
missing_data = pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)
print(missing_data)

# Dropping the NA values from data and stored it and 'data_1' variable
data_1 = data.dropna()

total_null_1 = data_1.isnull().sum()
percent_null_1 = (total_null_1/data_1.isnull().count())
missing_data_1 = pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)
print(missing_data_1)

sns.catplot(x="Category",y="Rating",data=data, kind="box",height = 10)
sns.xticks=90
plt.title('Rating vs Category [BoxPlot]')

#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

data['Installs']=data['Installs'].str.replace('+','')
data['Installs']=data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].astype(int)
print(data['Installs'])

le = LabelEncoder()
data['Installs']=le.fit_transform(data['Installs'])
plt.figure(figsize = (10,10))
sns.regplot(x="Installs", y="Rating",color = 'teal' , data=data)
plt.title('Rating vs Installs [RegPlot]',size=20)

print(data['Price'])

data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)
plt.figure(figsize = (10,10))
sns.regplot(x="Price", y="Rating" , data=data)
plt.title('Rating vs Price [RegPlot]',size=20)

data['Genres'].unique()
data['Genres'] = data['Genres'].str.split(';').str[0]
gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()
print(gr_mean.describe())
gr_mean = gr_mean.sort_values(by=['Rating'])

data['Last Updated'] =pd.to_datetime(data['Last Updated'])
data['Last Updated Days'] = (data['Last Updated'].max()-data['Last Updated'] ).dt.days 
plt.figure(figsize = (10,10))
sns.regplot(x="Last Updated Days", y="Rating",color = 'lightpink', data=data)
plt.title('Rating vs Last Updated Days[RegPlot]',size = 20)

#Code ends here



