Feature: Test that pages have correct content
  
  Scenario: Blog page has a correct title
    Given I am on the blogpage
    Then There is a title shown on the page
    And The title tag had content "This is the blog page"