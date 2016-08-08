Feature: Search result is displayed for searched items on amazon website.

    Scenario: check that after user enters search text, and submit search result are displayed
	When I go to the amazon home page
        And I enter search text "qa testing" in search field and click submit
	Then I should see search result "qa testing"

    Scenario: check that total number of search result displayed is a positive integer.
        When I go to the amazon home page
        And I enter search text "qa testing" in search field and click submit
	Then I should see search result "qa testing"
        And Total number of search result is a positive integer

    Scenario: check that if no search text is entered, no result is displayed
        When I go to the amazon home page
        And I enter search text " " in search field and click submit
        Then No search result should be displayed

