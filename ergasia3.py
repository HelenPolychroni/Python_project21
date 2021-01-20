import urllib.request
import datetime
import json
from datetime import date, timedelta


day2day= datetime.datetime.now().day
currentmonth=datetime.datetime.now().month

#print(currentmonth)
#print(day2day)

winnums=[]

for i in range(0,day2day):
    days_b4 = (date.today()-timedelta(days=i)).isoformat()
    #o sindesmos gia ta drawid einai ths morfhs:
    #--https://api.opap.gr/draws/v3.0/{gameId}/draw-date/{fromDate}/{toDate}/draw-id---
    drawIdsUrl="https://api.opap.gr/draws/v3.0/1100/draw-date/{}/{}/draw-id".format(days_b4,days_b4)
    r=urllib.request.urlopen(drawIdsUrl)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)
    #print ("The list of drawids looks like this:\n ",html)
    #o sindesmos einai ths morfhs--https://api.opap.gr/draws/v3.0/{gameId}/{drawId}--
    firstDrawUrl="https://api.opap.gr/draws/v3.0/1100/%s" % data[0]
    r1=urllib.request.urlopen(firstDrawUrl)
    html1=r1.read()
    html1=html1.decode()
    data1=json.loads(html1,strict=False)
    #print ("Oi nikhtirioi arithmoi(ths 1st klhrwshs) thn",days_b4, "einai:\n ",data1["winningNumbers"]["list"])
    winnums.append(data1["winningNumbers"]["list"])

#print(winnums)
months=["January","February","March","April","May","June","July","August","September","October","November","December"]

print("Ta statistika twn arithmwn gia to kino pou kerdizoun thn 1h klhrwsh ths hmeras kata ton mhna",months[currentmonth-1],"einai ta parakatw:\n")

print(" num          times")
for i in range (1,81):
   sum(x.count(i) for x in winnums)

   print (" ",i,"   -->    ",sum(x.count(i) for x in winnums))
