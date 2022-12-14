import json
from behave import *
from application import USERS

@given('some users are in the system')
def step_impl(context):
    USERS.update({
      'jasonb': {'name': 'Jason Bourne'},
      'miket': {'name': 'Mike Tyson'},
      'wills': {'name': 'Will Smith'}
    })

@when(u'I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/{}'.format('jasonb'))
    assert context.page

@then(u'I should get a \'200\' response')
def step_impl(context):
    assert context.page.status_code is 200

@then(u'the following user details are returned')
def step_impl(context):
    # assert context.table[0].cells[0] in context.page.text
    assert "Jason Bourne" in context.page.text


@when('I retrieve all the customers')
def step_impl(context):
    context.page = context.client.get('/users/')
    assert context.page

@then('the following users details are returned')
def step_impl(context):
    assert "Jason Bourne" in context.page.text 
    assert "Mike Tyson" in context.page.text 
    assert "Will Smith" in context.page.text

@when(u"I add an user \'lebronj\' as \'Lebron James\' that does not exists yet")
def step_impl(context):
    context.page = context.client.post('/users/', data=json.dumps({'lebronj': {'name': 'Lebron James'}}))

@then(u"I should get a \'201\' response")
def step_impl(context):
    assert context.page.status_code is 201

@when(u"I update the name of an existing user \'jasonb\' to \'Jason Bateman\'")
def step_impl(context):
    context.page = context.client.put('/users/{}'.format('jasonb'), data=json.dumps({'jasonb': {'name': 'Jason Bateman'}}))

@when("I delete the existing user \'jasonb\'")
def step_impl(context):
    context.page = context.client.delete('/users/{}'.format('jasonb'))
