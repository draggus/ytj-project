import requests
import json
response = requests.get('https://avoindata.prh.fi/bis/v1/2532004-3')
print(response.status_code)
company = response.json()
print ("Business ID: ", company['results'][0]['businessId'])
print ("Company Name: ", company['results'][0]['name'])
print ("Address: ", company['results'][0]['addresses'][1]['street'])
print ("Post Code: ", company['results'][0]['addresses'][1]['postCode'])
print ("City: ", company['results'][0]['addresses'][1]['city'])
print ("Phone Number: ", company['results'][0]['contactDetails'][3]['value'])
print ("Webpage: ", company['results'][0]['contactDetails'][9]['value'])
