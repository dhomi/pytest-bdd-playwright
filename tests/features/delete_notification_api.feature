Feature: Delete Notification API
  Deze call verwijderd een klant
  voor het Business Portal scenario

  @verwijder_klant
  Scenario: Send SOAP request to delete a notification
    Given the Notification API endpoint is set
    And the request headers are set
    And the SOAP delete request body is prepared
    When I send the SOAP delete request
    Then the response status code should be 200
    And the response should contain a valid SOAP response