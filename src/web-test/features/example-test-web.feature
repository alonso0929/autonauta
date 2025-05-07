Feature: Example Web Testing Automation

@WEB
Scenario: Search RUC and validate results
    Given user navigates to Consulta SUNAT page
    When user search for RUC "20100030595"
    Then it should show all the results according to the search "20100030595 - BANCO DE LA NACION"
