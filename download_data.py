import requests
import datetime

now = datetime.date.today()
print (now)
yesterday = now - datetime.timedelta(days=1)
print(yesterday)



request = requests.get("https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-" +str(now)+".xlsx")
if request.status_code == 200:


    dls = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-" +str(now)+".xlsx"
    
    
    
    
    resp = requests.get(dls)
    
    output = open('COVID-19-geographic-disbtribution-worldwide.xlsx', 'wb')
    output.write(resp.content)
    output.close()
    print("Todays data released")
else:
    dls = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-" +str(yesterday)+".xlsx"
    
    
    print("Todays data not released yet downloading yesterdays data") 
    
    resp = requests.get(dls)
    
    output = open('COVID-19-geographic-disbtribution-worldwide.xlsx', 'wb')
    output.write(resp.content)
    output.close()
