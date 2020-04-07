import requests
import datetime
now = datetime.date.today()
print (now)



dls = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-" +str(now)+".xlsx"




resp = requests.get(dls)

output = open('COVID-19-geographic-disbtribution-worldwide.xlsx', 'wb')
output.write(resp.content)
output.close()
