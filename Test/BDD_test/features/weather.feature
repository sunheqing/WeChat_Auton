Feature: The user enters
  the weather code, and
  the WeChat assistant
  returns information
  about the weather

  Scenario: Factorial of 0
    Given I have the code 0
    When I compute its factorial
    Then I see the number 1