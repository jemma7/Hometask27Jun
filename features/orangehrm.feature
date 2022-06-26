Feature: OrangeHRM

    Scenario: Login OrangeHRM Admin page and add a user
    Given launch Chrome browser
    When open OrangeHRM homepage
    Then Login OrangeHRM Admin page
    Then Add a user 
    Then Verify a user is added
    And close the browser