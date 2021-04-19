Feature: Test navigation between pages
  we can have a longer description
  that can span a few lines

  Scenario: Homepage can go to blog
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page