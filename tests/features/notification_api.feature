Feature: Notification API
  Deze call maakt voor het Business Portal scenario
  een 'standaard' klant aan.

  Scenario: Maak een standaard klant aan voor het Business Portal
    Given the Notification API endpoint is set
    And the request headers are set
    And the SOAP request body is prepared
    When I send the SOAP request
    Then the response status code should be 200
    And the response should contain a valid SOAP response