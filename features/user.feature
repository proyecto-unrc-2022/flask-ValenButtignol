Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Jason Bourne |

  Scenario: Retrieve all customers details.
    Given some users are in the system
    When I retrieve all the customers
    Then I should get a '200' response
    And the following users details are returned
      | name         |
      | Jason Bourne |
      | Mike Tyson   |
      | Will Smith   |

  Scenario: Add a new user.
    Given some users are in the system
    When I add a user 'lebronj' as 'Lebron James' that does not exists yet
    Then I should get a '201' response