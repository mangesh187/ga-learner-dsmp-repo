# --------------
import pandas as pd
import matplotlib as plt
import seaborn as sns
data=pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
sns.barplot(y=loan_status)


# --------------
#Code starts here




property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
sns.barplot(y=property_and_loan)
xlabels=('Property_Area')
ylabels=('Loan Status')



# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])

education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar')
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)


# --------------
#Code starts here

#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']


#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education']=='Not Graduate']


#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density', label='Graduate')


#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')


#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)
ax_1.scatter(x=data['ApplicantIncome'],y=data['LoanAmount'])
plt.title('Applicant Income')
ax_2.scatter(x=data['CoapplicantIncome'],y=data['LoanAmount'])
plt.title('Coapplicant Income')
TotalIncome=data['ApplicantIncome']+data['CoapplicantIncome']
data['TotalIncome']=TotalIncome
ax_3.scatter(x=data['TotalIncome'],y=data['LoanAmount'])
plt.title('Total Income')


