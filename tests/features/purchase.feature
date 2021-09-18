Feature: Purchase product
  Scenario Outline: Purchase success
        Given User on main page
        When Click 'SIGN IN / REGISTER' button
        And Enter first name
        And Enter last name
        And Enter unique email address
        And Enter password
        And Enter password confirmation
        And Check 'Terms and conditions'
        And Click 'Register' button
        And Choose product
        And Click add product to cart
        And Click checkout
        And Click cart checkout
        And Fill form
        And Submit form
        And Fill payment
        And Submit payment form
        And Finish purchase
        Then Order placed

        Examples:
        | firstname    | lastname | password   | password_confirmation |
        | 'name'       | 'sur'    | 'passw0rd' | 'passw0rd'            |