# FIRST VERSION OF CODE - NEEDS A CLEAN! asdfasdf

import urllib.request
DataURL='https://raw.githubusercontent.com/robertoioi/trainer-telegram/main/Programma%20Maratona%20di%20Roma.CSV'

# Download data
response=urllib.request.urlopen(DataURL)
data=response.read().decode("utf-8")

# Turn raw data into series
rows=data.split("\n")
days=rows[0].split(";")[0:6]
list_weeks=[]
for n in range(1,len(rows)-2):
        weeks=rows[n].split(";")[0]
        list_weeks.append(weeks)
#print(list_weeks)

list_activities=[]
for n in range(1,len(rows)-2):
        activity=rows[n].split(";")[1:7]
        list_activities.append(activity)
print(list_activities)


giorni_settimana=7
for wk in range(len(list_weeks)-1):
        for dd in range(giorni_settimana-1):
                print("("+list_weeks[wk]+")",days[dd], list_activities[wk][dd])



