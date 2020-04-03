import pandas as pd
from pathlib import Path
df = pd.read_excel(r'COVID-19-geographic-disbtribution-worldwide.xlsx', sheet_name='COVID-19-geographic-disbtributi')

Path(r"Countries File").mkdir(parents=True, exist_ok=True)
Path(r"Country Graphs").mkdir(parents=True, exist_ok=True)

print("Column headings:")
print(df.columns)
cases=df['cases']
deaths=df['deaths']
date=df['dateRep']
loop=0
for i in df['countriesAndTerritories']:

    first=1
    print(loop)
    filename= "Countries File\\"  + str(i) +".txt"
    print(str(date[loop])+" " + str(cases[loop]) + " " + str(deaths[loop]))
    if i==first:
        f = open(filename, "a")
        f.write(str(date[loop]) +" "+str(cases[loop])+ " " + str(deaths[loop]) + "\n")
        f.close()
    elif i != first:            
        f = open(filename, "a")
        f.write(str(date[loop]) +" "+str(cases[loop])+ " " + str(deaths[loop]) + "\n")
        f.close()
    first=i
    loop=loop+1
   
    