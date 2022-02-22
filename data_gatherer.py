import requests
import json
bisid = str(input("Enter a businessID: "))
response = requests.get('https://avoindata.prh.fi/bis/v1/'+ (bisid))
print(response.status_code)
company = response.json()
print ("Business ID: ", company['results'][0]['businessId'])
print ("Company Name: ", company['results'][0]['name'])
for x in company['results'][0]['addresses']:
    if x['street'] == "":
        continue
    elif x['street'] == None:
        continue
    else:
        print("Address: ", x['street'])
        break
for x in company['results'][0]['addresses']:
    if x['postCode'] == "":
        continue
    elif x['postCode'] == None :
        continue
    else:
        print("Post Code: ", x['postCode'])
        break
for x in company['results'][0]['addresses']:
    if x['city'] == "":
        continue
    elif x['city'] == None :
        continue
    else:
        print("City: ", x['city'])
        break
for x in company['results'][0]['contactDetails']:
    if ["Puhelin"]:
        if x['value'] == "":
            continue
        elif x['value'] == None:
            continue
        else:
            print("Phone Number: ",x['value'])
            break
    else:
        continue
#This part I just couldn't get to work for now..
print("Webpage: ", company['results'][0]['contactDetails'][9]['value'])
#This part I just couldn't get to work for now..