Feature: Store Finder
    Scenario: Show all stores
        Given User on store finder page
        When 'Find stores' button clicked
        Then stores table is shown

    Scenario Outline: Empty search input
        Given User on store found page
        When 'Magnifier' button clicked
        Then error is shown

        Examples:
        | error_text                                               |
        | 'Check that you entered a valid postcode or place name.' |

    Scenario Outline: Particular store search
        Given User on store found page
        When search input filled with a value
        And 'Magnifier' button clicked
        Then particular store is shown

        Examples:
        | store_name |
        | 'Bedford'  |
