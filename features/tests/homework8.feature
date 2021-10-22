
Feature: Homework 8

  Scenario: User can select and search in a department
    Given Open Amazon page
    When Select department by alias computers
    When Input dell monitor into Amazon search
    And Click on Amazon search icon
    Then Verify pc department is selected


  Scenario: User can see New Arrival's deals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrivals
    Then Verify user sees the deals
