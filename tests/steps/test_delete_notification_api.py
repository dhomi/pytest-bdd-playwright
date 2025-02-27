import requests
from pytest_bdd import scenarios, given, when, then
from lxml import etree

scenarios('../features/delete_notification_api.feature')

API_URL = 'https://api-dev.cdn.cldsvc.net/system/v1/notifications/esp'
HEADERS = {
    'Content-Type': 'application/xml',
    'apikey': '545d1a46-2ed4-4593-b1c3-eecdb90c443d'
}
SOAP_DELETE_BODY = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://schemas.postnl.nl/parcels/customerInteraction/notifications/emailBasicSubscriptionService/v1.0/" xmlns:com="http://schemas.postnl.nl/parcels/customerInteraction/notifications/common/">
<soapenv:Header/>
<soapenv:Body>
<v1:DeleteRequest>
<v1:KlantNr>13371340</v1:KlantNr>
</v1:DeleteRequest>
</soapenv:Body>
</soapenv:Envelope>'''

@given('the Notification API endpoint is set', target_fixture="set_api_endpoint")
def set_api_endpoint():
    return API_URL

@given('the request headers are set', target_fixture="set_request_headers")
def set_request_headers():
    return HEADERS

@given('the SOAP delete request body is prepared', target_fixture="prepare_soap_delete_body")
def prepare_soap_delete_body():
    return SOAP_DELETE_BODY

@when('I send the SOAP delete request', target_fixture="send_soap_delete_request")
def send_soap_delete_request(set_api_endpoint, set_request_headers, prepare_soap_delete_body):
    response = requests.post(set_api_endpoint, headers=set_request_headers, data=prepare_soap_delete_body)
    return response

@then('the response status code should be 200', target_fixture="check_response_status_code")
def check_response_status_code(send_soap_delete_request):
    assert send_soap_delete_request.status_code == 200

@then('the response should contain a valid SOAP response', target_fixture="check_response_content")
def check_response_content(send_soap_delete_request):
    try:
        etree.fromstring(send_soap_delete_request.content)
    except etree.XMLSyntaxError:
        assert False, "Response is not a valid XML"