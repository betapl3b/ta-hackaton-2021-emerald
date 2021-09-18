Feature: Home Page
    Scenario: Cookie notification
        Given User on main page
        When Cookie notification
        And Close notification
        Then No notification

    Scenario Outline: Authorization invalid
        Given User on login page
        When Login
        Then Login unsuccess

        Examples:
        | email           | password |
        | '12341@mail.ru' | '1234123' |

    Scenario Outline: Authorization success
        Given User on main page
        When Click 'SIGN IN / REGISTER' button
        And Enter first name
        And Enter last name
        And Enter unique email address
        And Enter password
        And Enter password confirmation
        And Check 'Terms and conditions'
        And Click 'Register' button
        And Click 'Logout' button
        And Login
        Then Main page is opened
        And Username is shown in header section

        Examples:
        | firstname    | lastname | password   | password_confirmation |
        | 'name'       | 'sur'    | 'passw0rd' | 'passw0rd'            |

    Scenario Outline: No results search item
        Given User on main page
        When Enter searching word
        Then No results message are showed

         Examples:
        | word             |
        | 'hghgh'          |


    Scenario Outline: Success search item
        Given User on main page
        When Enter searching word
        Then Results are showed

         Examples:
        | word             |
        | 'helmet'          |


    Scenario: Empty search item
        Given User on main page
        When Click search button
        Then Nothing happens


