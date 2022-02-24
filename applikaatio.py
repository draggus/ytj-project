from flask import Flask, request
app = Flask(__name__)

@app.route('/json-example', methods=['GET', 'POST'])
def json_example():
    request_data = request.get_json()

    if request_data:
        if 'businessid' in request_data:
            if 'businessid' in request_data['results']:
                businessid = request_data['results'][0]['businessId']

        if 'company_name' in request_data:
            if 'company_name' in request_data['results']:
                company_name = request_data['results'][0]['name']
        
        if 'street_address' in request_data:
            if 'street_address' in request_data['results'][0]:
                for x in request_data['results'][0]['addresses']:
                    if ['street'] == "":
                        continue
                    elif ['street'] == None:
                        continue
                    else:
                        street_address = request_data['results'][0]['addresses']['street']
                        break
                        
        if 'post_code' in request_data:
            if 'post_code' in request_data['results'][0]:
                for x in request_data['results'][0]['addresses']:
                    if ['postCode'] == "":
                        continue
                    elif ['postCode'] == None:
                        continue
                    else:
                        post_code = request_data['results'][0]['addresses']['postCode']
                        break
        
        if 'city' in request_data:
            if 'city' in request_data['results'][0]:
                for x in request_data['results'][0]['addresses']:
                    if ['city'] == "":
                        continue
                    elif ['city'] == None:
                        continue
                    else:
                        city = request_data['results'][0]['addresses']['city']
        
        if 'phone_number' in request_data:
            if 'phone_number' in request_data['results'][0]:
                if 'phone_number' in request_data['results'][0]['contactDetails']:
                    for x in request_data['results'][0]['contactDetails']:
                        if ['Puhelin'] == "":
                            continue
                        elif ['Puhelin'] == None:
                            continue
                        else:
                            phone_number = request_data['results'][0]['contactDetails']['value']

        if 'webpage' in request_data:
            if 'phone_number' in request_data['results'][0]:
                if 'phone_number' in request_data['results'][0]['contactDetails']:
                    for x in request_data['results'][0]['contactDetails']:
                        if ['type'] == ["Kotisivun www-osoite"]:
                            webpage = request_data['results'][0]['contactDetails']['value']
                            break
                        elif ['type'] == ['www-adress']:
                            webpage = request_data['results'][0]['contactDetails']['value']
                            break
                        elif ['type'] == ['Website address']:
                            webpage = request_data['results'][0]['contactDetails']['value']
                            break                        
    businessid = None
    company_name = None
    street_address = None
    post_code = None
    city = None
    phone_number = None
    webpage = None

    return '''
            The businessid is: {}
            The company_name is: {}
            The street address is: {}
            The post code is: {}
            The city is: {}
            The phone number is: {}
            The webpage is: {}'''.format(businessid, company_name, street_address, post_code, city, phone_number, webpage)

if __name__ == '__main__':
    app.run(debug=True, port=5000)