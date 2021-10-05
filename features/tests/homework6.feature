# Created by Houston Lea at 10/4/2021
Feature: Homework 6
  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon Terms of Conditions page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And Close the current window
    And Switch back to original


  Scenario: Make a test case using a loop on BestSellers
    Given Open BestSellers page
    Then Verify that new page open when looping
