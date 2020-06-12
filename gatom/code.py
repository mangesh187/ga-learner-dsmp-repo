# --------------

# Import packages
import numpy as np
import pandas as pd

from scipy.stats import mode 

# code starts here

# Read the file using the path  
df = pd.read_csv(path)

bank = pd.DataFrame(df)

categorical_var = df.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = df.select_dtypes(include = 'number')
print(numerical_var)

banks = bank.drop(['Loan_ID'],axis = 1)
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())

avg_loan_amount = pd.pivot_table(banks,index=["Gender","Married","Self_Employed"],values=["LoanAmount"],aggfunc=(np.mean))
print(avg_loan_amount)

# code for loan aprroved for self employed
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_se)

# code for loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No")  & (banks["Loan_Status"]=="Y"), ["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614)
percentage_se=percentage_se[0]

# print percentage of loan approved for self employed
print(percentage_se)

#percentage of loan for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse=percentage_nse[0
                              
#print percentage of loan for non self employed
print (percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x:int(x)/12)
big_loan_term =len(loan_term[loan_term >=25])
print(big_loan_term)

# code starts here
loan_groupby = banks.groupby(['Loan_Status'])
columns=['ApplicantIncome','Credit_History']
loan_groupby = loan_groupby[columns]
mean_values = loan_groupby.agg([np.mean])
print(mean_values)
                              
# code ends here

