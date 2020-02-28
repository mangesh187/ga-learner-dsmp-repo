# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#path of the data file- path
data = pd.read_csv(path)
#Code starts here
data['Gender'].replace('-','Agender',inplace = True) 
gender_count = data['Gender'].value_counts()
gender_count.plot(kind = 'bar')
plt.title('Gender Counts')


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot.pie(label='Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = data['Strength'].std()
sc_combat = data['Combat'].std()
sc_pearson = sc_covariance/(sc_combat*sc_strength)
sc_pearson = sc_pearson.round(2)
print(sc_covariance)
print(sc_pearson)
ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = data['Intelligence'].std()
ic_combat = data['Combat'].std()
ic_pearson = ic_covariance/(ic_combat*ic_intelligence)
ic_pearson = ic_pearson.round(2)
print(ic_pearson)




# --------------
#Code starts here
total_high = data['Total'].quantile(0.99)
print(total_high)
super_best = data[data['Total'] > total_high]
super_best_names = super_best['Name']
super_best_names = list(super_best_names)
print(super_best_names)


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(3)
ax_1.plot(data['Intelligence'])
plt.title('Intelligene')
ax_2.plot(data['Speed'])
plt.title('Speed')
ax_3.plot(data['Power'])
plt.title('Power')



