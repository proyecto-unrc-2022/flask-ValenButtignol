Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Jason Bourne |

  Scenario: Add a new user.
    Given some users are in the system
    When I add a new user 'lebronj' as 'Lebron James'
    And it's not already on users
    Then I should get a '201' response
    And the following user details are returned:
      | name         |
      | Lebron James |


  Scenario: Retrieve all customers details.
    Given some users are in the system
    When I retrieve all the customers
    Then I should get a '200' response
    And the following users details are returned
      | name         |
      | Jason Bourne |
      | Mike Tyson   |
      | Will Smith   |