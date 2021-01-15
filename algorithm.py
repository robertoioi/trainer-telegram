# NEEDS A CLEAN
import urllib.request                                                                                                                                                                 import urllib.request
DataURL='https://raw.githubusercontent.com/robertoioi/trainer-telegram/main/Programma%20Maratona%20di%20Roma.CSV'

# Download data
response=urllib.request.urlopen(DataURL)
data=response.read().decode("utf-8")

# Turn raw data into series
rows=data.split("\n")
days=rows[0].split(";")[0:7]
list_weeks=[]
for n in range(1,len(rows)-1):
        weeks=rows[n].split(";")[0:8]
        list_weeks.append(weeks)

for wk in range(len(list_weeks)-1):
        for dd in range(len(days)):
                #current_train=str(("("+list_weeks[wk]+")",days[dd], list_activities[wk][dd]))
                #print(current_train)
                print("("+list_weeks[wk][0]+")",days[dd], list_weeks[wk][dd])
