from behave import *
from base.user_telegram import User
from features.logger_file import LogGen

@then("client check message -{message}-{code}-")
def step_impl(context, message, code):
    client = User(context.client, 'sd_test12_bot')
    assert client.check_message_code(code)

@given("client send message -{message}-")
def step_impl(context, message):
    client = User(context.client, 'sd_test12_bot')
    client.send_message(message)