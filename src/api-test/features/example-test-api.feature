Feature: Example API Testing Automation

@API
Scenario: Validate API Status Response GET
    Given the path is "/api/users/2"
    When I make a GET request
    Then the response status should be 200

@API
Scenario: Validate API Data Response GET
    Given the path is "/api/users/2"
    When I make a GET request
    Then the response name should be "Janet"