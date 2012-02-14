Feature: Index Page
  In order to get Twitlist started
  As a user
  I should be able to see an initial page

  Scenario: Checking the index page when user is not signed in
    Given I access the url "/"
    Then I should see the header "TwitList"
    And I should see the image linking to Twitter sign in