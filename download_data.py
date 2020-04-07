import requests
import datetime
now = datetime.date.today()
print (now)
yesterday = now - datetime.timedelta(days=1)

try:

    dls = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-" +str(now)+".xlsx"
    
    
    
    
    resp = requests.get(dls)
    
    output = open('COVID-19-geographic-disbtribution-worldwide.xlsx', 'wb')
    output.write(resp.content)
    output.close()
except:
    dls = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-" +str(yesterday)+".xlsx"
    
    
    
    
    resp = requests.get(dls)
    
    output = open('COVID-19-geographic-disbtribution-worldwide.xlsx', 'wb')
    output.write(resp.content)
    output.close()
