import pandas as pd

pd.read_csv('Salaries.csv')
sal = pd.DataFrame(pd.read_csv('Salaries.csv'))
#print(sal.info())
#print(sal.head(3).to_string())
# print(sal["BasePay"].mean())
# print(sal['OvertimePay'].max())

#print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
#a = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
#print(a)


gb = sal.groupby('Year')['BasePay'].mean()
#print(gb)

a = len(sal['JobTitle'].unique())
#print(a)

c = sal['JobTitle'].value_counts().head(5)
#print(c)

o = sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)
#print(o)



def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else :
        return False


ch = sum(sal['JobTitle'].apply(lambda x: chief_string(x)))
#print(ch)

sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['TotalPayBenefits','title_len']].corr())
