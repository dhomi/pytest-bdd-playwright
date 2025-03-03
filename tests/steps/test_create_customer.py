import requests
from pytest_bdd import scenarios, given, when, then

# Path to the feature file
scenarios('../features/create_customer.feature')


# Given step: Set up the necessary headers and body for the delete request
@given('I have the necessary headers and body for the API request', target_fixture="setup_request")
def setup_request():
    headers = {
        'Content-Type': 'application/xml',
        'apikey': '545d1a46-2ed4-4593-b1c3-eecdb90c443d',
    }

    body = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
        xmlns:v1="http://schemas.postnl.nl/parcels/customerInteraction/notifications/emailBasicSubscriptionService/v1.0/"
        xmlns:com="http://schemas.postnl.nl/parcels/customerInteraction/notifications/common/">
        <soapenv:Header/>
        <soapenv:Body>
        <v1:DeleteRequest>
        <v1:KlantNr>13371340</v1:KlantNr>
        </v1:DeleteRequest>
        </soapenv:Body>
        </soapenv:Envelope>'''

    return {
        'url': 'https://api-dev.cdn.cldsvc.net/system/v1/notifications/esp',
        'headers': headers,
        'body': body
    }


# When step: Send the delete request to the API
@when('I send the request to the API', target_fixture="send_request")
def send_request(setup_request):
    url = setup_request['url']
    headers = setup_request['headers']
    body = setup_request['body']

    response = requests.post(url, headers=headers, data=body)

    return response


# Then step: Assert the response has status code 200
@then('I should receive a valid response with status code 200', target_fixture="check_response_status_code")
def check_response_status_code(send_request):
    response = send_request
    assert response.status_code == 200
