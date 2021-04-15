import pandas as pd

pd.read_csv('Salaries.csv')
sal = pd.DataFrame(pd.read_csv('Salaries.csv'))
print(sal.info())
# print(sal["BasePay"].mean())
# print(sal['OvertimePay'].max())

#print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
a = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
print(a)
