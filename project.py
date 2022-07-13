#Name: Mahgabin Khanom
#Email: Mahgabin.khanom69@myhunter.cuny.edu
#URL: https://mahgabinkhanom69.wixsite.com/choices
#Title: My Body, My Choice: Abortions in New York City 
#Resources: using the pandas package, textbook, programs, online resources listed in citations: https://www1.nyc.gov/site/doh/health/health-topics/abortion.page, https://www1.nyc.gov/site/doh/health/health-topics/abortion.page, https://a816-healthpsi.nyc.gov/NYCHealthMap/home/ByServices?services=72, https://www.nychealthandhospitals.org/, https://prochoice.org/patients/find-a-provider/
import pandas as pd
from pandasql import sqldf 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

InputfileY= input('Enter file name:')

csvOutputY = input("Enter output file name: ")
workingfile = pd.read_csv(InputfileY) #reading in from csv file

df = pd.DataFrame(workingfile)


result = df['Fake_clinic'].groupby(df['Borough']).value_counts()

result.plot(kind='barh', x='Borough')

plt.xlabel("Number of clinics")

plt.ylabel("Borough with Fake clinics")

plt.title("Regional Locations of Fake Abortion Clinics")

plt.show()



result2 = df['Name']
result= df.loc[(df['Medicaid']=="yes") & (df['Num_of_insurance']), ['Medicaid','Num_of_insurance']]
resulty = pd.concat([result2, result], axis=1)
print(resulty)

q1 = 'select `Borough` as borough, avg(`Surgical_duration`)as surgical_duration, avg(`Medication_duration`) as medication_duration from workingfile group by Borough'

q1_columns = sqldf(q1)

df1 = pd.DataFrame(q1_columns)

df1.plot(x='borough', y=['medication_duration', 'surgical_duration'], kind="bar")

plt.title("Surgical/Medication Duration Availaility From Clinics")

plt.show()



result= df.loc[(df['Fake_clinic']=="yes") & (df['Borough']) & (df['Number']) & (df['Name']), ['Fake_clinic','Borough','Number','Name']]
print(result)
result.to_csv(csvOutputY, index=False)


s = df.squeeze(axis=1)
reading = s.describe()
print(reading)
reading.to_csv(csvOutputY, index=False)


