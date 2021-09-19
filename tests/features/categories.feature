Feature: Categories
  Scenario: Select categories
        Given User on main page
        When Click 'shop women'
        Then User on searched for women page
        Then Applied Facets is Female
        When Search shop which starts with LONDON
        When Select first price
        And Select first colour
        And Select first size
        Then Collection list is not displayed
        And Category list is not displayed
        And Brand list is not displayed
        And 1 product found
        And products grid contains 1 item

  Scenario: Categories after refresh
        Given User on main page
        When Click 'shop women'
        Then User on searched for women page
        When Select first price
        And Select first colour
        And Select first size
        When Refresh browser
        Then First price selected
        Then First colour selected
        Then First size selected
