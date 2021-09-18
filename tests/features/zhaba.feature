Feature: Home Page
    Scenario: Cookie notification
        Given Go to main page
        When Cookie notification
        And Close notification
        Then No notification

    Scenario: Authorization blocked
        Given Go to main page
        When Login
        Then Login unsuccess