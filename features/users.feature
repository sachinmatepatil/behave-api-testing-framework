Feature: JSONPlaceholder User API testing
  As a QA Engineer
  I want to test JSONPlaceholder /users endpoint
  So that I can validate the API's behavior and response

  Scenario: Retrieve a list of users
    Given the API base URL is SET
    When I send GET request to "/users"
    Then the response status code should be 200
    And the response should contain a list of users

  Scenario: To create a post
    Given the API base URL is SET
    When I send POST request to "/posts" with the following data:
      | key   | value                |
      | title | first post           |
      | body  | first post by sachin |
      | userId | 1                   |
    Then the response status code should be 201
    And the response should contain "id"

  Scenario: To update existing data
    Given the API base URL is SET
    When I send PUT request to "/posts/1" with the following data:
    | key    | value               |
    | title  | updated first post  |
    | body   | updated post sachin |
    | userId | 1                   |
    Then the response status code should be 200
    And the response should contain the updated "title" as "updated first post"

  Scenario: To delete an existing post
    Given the API base URL is SET
    When I send a DELETE request to "/posts/1"
    Then the response status code should be 200
#    And the resource "/posts/2" should not exist

  Scenario Outline: To test different user IDs
    Given the API base URL is SET
    When I send GET request to "/users/<user_id>"
    Then the response status code should be 200
    Examples:
      | user_id |
      |1        |
      |2        |
      |3        |