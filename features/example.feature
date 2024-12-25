Feature: Simple Example for Behave

  Scenario: Verify Behave is running
    Given I have installed Behave
    When I run Behave
    Then I should see Behave execute successfully