Feature: Home Page
    Scenario: Cookie notification
        Given User on main page
        When Cookie notification
        And Close notification
        Then No notification

    Scenario Outline: Authorization blocked
        Given User on login page
        When Login
        Then Login unsuccess

        Examples:
        | login           | password |
        | '12341@mail.ru' | '1234123' |