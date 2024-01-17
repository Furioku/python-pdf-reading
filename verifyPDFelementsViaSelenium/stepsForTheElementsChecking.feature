Feature: We would like to check if pdf file contains appropriate content

Scenario: User should be able to check if pdf file opens in browser and contains appropriate conten
    Given User enters to pdf file via provided link
    Then User verifies that pdf file contains content
    