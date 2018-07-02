Feature: The user enters
  the news code, and
  the WeChat assistant
  returns information
  about the news

  Scenario: Factorial of 0
    Given I have the code 0
    When I compute its factorial
    Then I see the number 1