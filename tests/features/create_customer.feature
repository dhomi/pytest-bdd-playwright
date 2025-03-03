Feature: Create Customer on the Notification API
  This call creates a 'standard' customer
  for the Business Portal scenario

  @create_customer
  Scenario: Create a standard customer for the Business Portal
    Given I have the necessary headers and body for the API request
    When I send the request to the API
    Then I should receive a valid response with status code 200
