Feature: Get Post from JSONPlaceholder API
  This feature tests the retrieval of a post from the JSONPlaceholder API.

  @get_post
  Scenario: Retrieve a post by ID
    Given I have the endpoint for the post with ID 1
    When I send a GET request to the endpoint
    Then I should receive a valid response with status code 200
    And the response should contain the post details