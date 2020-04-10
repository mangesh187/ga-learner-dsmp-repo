# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# path        [File location variable]
data = pd.read_csv(path)

data_sample = data.sample(n=sample_size,random_state =0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
margin_of_error = z_critical*(sample_std/math.sqrt(sample_size))
confidence_interval =(sample_mean - margin_of_error,
sample_mean + margin_of_error)
true_mean = data['installment'].mean()
print("True mean :{}".format(true_mean))

import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

fig ,axes = plt.subplots(nrows = 3 , ncols = 1)
for i in range(len(sample_size)):
    m = []
    for j in range(1000):
        data['installment'].sample(n=sample_size[i])
        m.append(data['installment'].mean())
    mean_series = pd.Series(m)
    axes[i].hist(mean_series)
    
#Importing header files
from statsmodels.stats.weightstats import ztest
import statsmodels

data['int.rate'] = data['int.rate'].str.replace('%','')
data['int.rate'] = data['int.rate'].astype(float)/100
x1 = data[data['purpose']=='small_business']['int.rate']
z_statistic,p_value= statsmodels.stats.weightstats.ztest(x1,value=data['int.rate'].mean(),alternative='larger')
if p_value < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are failed to reject  null hypothesis")

#Importing header files

from statsmodels.stats.weightstats import ztest

x1 = data[data['paid.back.loan']=='No']['installment']
x2 = data[data['paid.back.loan']=='Yes']['installment']
z_statistic,p_value = statsmodels.stats.weightstats.ztest(x1,x2)
if p_value < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are failed to reject  null hypothesis")

#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
observed = pd.concat([yes.transpose(),no.transpose()], 1,keys=['Yes','No'])
chi2, p, dof, ex = chi2_contingency(observed, correction=False)

print("Critical value")
print(critical_value)
print("Chi Statistic")
print(chi2)
# --------------
