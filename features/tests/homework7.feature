Feature: Scenarios with Page Object pattern

  Scenario: Logged out user sees Sign in page when clicking Orders
   Given Open Amazon page
   When Click Amazon Orders link
   Then Verify Sign In page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
   Given Open Amazon page
   When Click on cart icon
   Then Verify 'Your Amazon Cart is empty' text present

  Scenario Outline: Pick product on Amazon
    # Rewrite homework4 scenario using Page Object pattern
    Given Open Amazon page
    When Input <search_word> into Amazon search
    And Click on Amazon search icon
    And Click on the first product
    When Store product name
    And Click on Add to cart button
    And Click on cart icon
    Then Verify cart has <number> item(s)
    And  Verify cart has correct product
    Examples:
      |search_word  |number|
      |clock        |    1 |


      #|table        |    1 |
      #|mug          |    1 |