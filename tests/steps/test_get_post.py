import requests
from pytest_bdd import scenarios, given, when, then

# Define the feature file to be used
scenarios('../features/get_post.feature')

# Define the endpoint
POST_ENDPOINT = "https://jsonplaceholder.typicode.com/posts/1"

@given('I have the endpoint for the post with ID 1', target_fixture="get_post_endpoint")
def get_post_endpoint():
    return POST_ENDPOINT

@when('I send a GET request to the endpoint', target_fixture="send_get_request")
def send_get_request(get_post_endpoint):
    response = requests.get(get_post_endpoint)
    return response

@then('I should receive a valid response with status code 200', target_fixture="check_status_code")
def check_status_code(send_get_request):
    assert send_get_request.status_code == 200

@then('the response should contain the post details', target_fixture="check_response_content")
def check_response_content(send_get_request):
    response_json = send_get_request.json()
    assert response_json['id'] == 1
    assert 'title' in response_json
    assert 'body' in response_json