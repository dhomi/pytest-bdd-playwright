Feature: Delete Customer on the Notification API
  This call deletes a customer
  for the Business Portal scenario

  @delete_customer
  Scenario: Send SOAP request to delete a notification
    Given I have the necessary headers and body for the delete API request
    When I send the delete request to the API
    Then I should receive a valid response with status code 200