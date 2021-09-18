Feature: Registration
    Scenario Outline: User sign up
        Given User on main page
        When Click 'SIGN IN / REGISTER' button
        Then Page title contains 'Login'
        When Select title
        And Enter first name
        And Enter last name
        And Enter unique email address
        And Enter password
        Then Password complexity bar is displayed
        When Enter password confirmation
        And Check 'Terms and conditions'
        Then 'Register' button is active
        When Click 'Register' button
        Then Main page is opened
        And 'Thank you for registering' banner is displayed
        And Username is shown in header section

        Examples:
        | title     | firstname    | lastname | password   | password_confirmation |
        | 'Mr.'     | 'name'       | 'sur'    | 'passw0rd' | 'passw0rd'            |
