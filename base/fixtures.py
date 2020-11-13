from telethon import  TelegramClient
from behave import fixture
import  os

@fixture()
def user(context):
    agent_dict = eval(os.environ.get('chan'))
    client_dict = eval(os.environ.get('stalone'))

    context.agent = TelegramClient('chan', agent_dict['api_id'], agent_dict['api_hash'])
    context.client = TelegramClient('stalone', client_dict['api_id'] , client_dict['api_hash'])
    yield
    # context.agent.disconnect()
    # context.client.disconnect()