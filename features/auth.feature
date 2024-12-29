Feature: Authenticated API Testing
@auth
  Scenario: Test authenticated GET request
    Given the API base URL is SET
    When I send an authenticated GET request to "/protected/resource"
    Then the response status code should be 404