# Created by Houston at 10/2/2021
Feature: Test case HW4

  Scenario: Test case will open BestSellers Amazon page
    Given Open BestSellers page
    When Store card metric list
    Then Verify there are 5 links in the list
    Then Verify the number the 1 item is "Best Sellers"
    And Verify the number the 2 item is "New Releases"
    And Verify the number the 3 item is "Movers & Shakers"
    And Verify the number the 4 item is "Most Wished For"
    And Verify the number the 5 item is "Gift Ideas"

  Scenario Outline: Pick product on Amazon
    Given Open Amazon page
    When Input <search_word> into Amazon search
    And Click on Amazon search icon
    And Click on the first product
    When Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has <number> item(s)
    And  Verify cart has correct product
    Examples:
      |search_word  |number|
      |clock        |    1 |
      |table        |    1 |
      |mug          |    1 |