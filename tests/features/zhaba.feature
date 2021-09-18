Feature: Home Page
    Scenario: Cookie notification
        Given Go to main page
        When Cookie notification
        When Close notification
        Then No notification