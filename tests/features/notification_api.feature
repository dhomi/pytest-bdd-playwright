Feature: Notification API
  Deze call maakt een 'standaard' klant aan
  voor het Business Portal scenario

  @maak_klant_aan

  Scenario: Maak een standaard klant aan voor het Business Portal
    Given I have the necessary headers and body for the API request
    When I send the request to the API
    Then I should receive a valid response with status code 200
