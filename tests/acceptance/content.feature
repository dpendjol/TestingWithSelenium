Feature: Test that pages have correct content
  
  Scenario: Blog page has a correct title
    Given I am on the blogpage
    Then There is a title shown on the page
    And The title tag had content "This is the blog page"

  Scenario: Home page has a correct title
    Given I am on the homepage
    Then There is a title shown on the page
    And The title tag had content "This is the homepage"

  Scenario: Blog page loads the posts
    Given I am on the blogpage
    And I wait for the posts to load
    # there has to be a minium of one posts
    Then I can see there is a posts section on the page