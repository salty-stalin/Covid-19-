import requests

dls = "https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-04-03.xlsx"




resp = requests.get(dls)

output = open('COVID-19-geographic-disbtribution-worldwide.xlsx', 'wb')
output.write(resp.content)
output.close()