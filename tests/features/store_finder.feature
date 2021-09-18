Feature: Store Finder
    Scenario: Show all stores
        Given User on store finder page
        When 'Find stores' button clicked
        Then stores table is shown

    Scenario: Empty search input
        Given User on store found page
        When search input is empty
        And 'Magnifier' button clicked
        Then 'Check that you entered a valid postcode or place name.' error is shown

    Scenario Outline: Particular store search
        Given User on store found page
        When search input filled with a value
        And 'Magnifier' button clicked
        Then particular store is shown

        Examples:
        | store_name |
        | 'Bedford'  |
