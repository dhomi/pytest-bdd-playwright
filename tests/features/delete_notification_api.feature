Feature: Delete Notification API
  Deze call verwijderd een klant
  voor het Business Portal scenario

  @verwijder_klant
  Scenario: Send SOAP request to delete a notification
    Given I have the necessary headers and body for the delete API request
    When I send the delete request to the API
    Then I should receive a valid response with status code 200