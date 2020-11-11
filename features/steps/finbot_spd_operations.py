from behave import *
from base.user_telegram import User
# use_step_matcher("re")

@given("client clicks a set of buttons")
def step_impl(context):
    client = User(context.client, '@sd_test12_bot')
    client.send_message('/start')
    for row in context.table:
        client.click_button(row['button_name'])

@step("client click the button -{button}-")
def step_impl(context, button):
    client = User(context.client, '@sd_test12_bot')
    client.click_button(button)

@when("client send message -{message}-")
def step_impl(context, message):
    client = User(context.client, '@sd_test12_bot')
    client.send_message(message)


@then("agent get message -{message}-")
def step_impl(context, message):
    agent = User(context.agent, '@sd_test12_bot')
    assert agent.check_message(message)