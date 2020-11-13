from telethon import TelegramClient, events
import asyncio
from base.functions import  find_button, find_text_from_table
from features.logger_file import LogGen

logger = LogGen.loggen()

class User():
    """
    class of user which could make action in telegram:
     - click button
     - send message
     - get message(s)
    ------------------------------
    client - object of TelegramClient()
    bot - name of the bot who you talk to
    """
    def __init__(self, client, bot, table=[]):
        self.client = client
        self.bot = bot
        self.loop = asyncio.get_event_loop()
        self.table = table




    async def get_last_message(self):
        message = await self.client.get_messages(self.bot, limit=1)
        return message[0]

    async def last_messages(self, quantity=2):
        messages = await self.client.get_messages(self.bot, limit=quantity)
        return messages

    async def xxx(self, conv):
        conv.wait_event(events.NewMessage(from_users=self.bot))
        conv.wait_event(events.NewMessage(from_users=self.bot))

    async def wait_after_click_button(self):
        async with self.client.conversation(self.bot) as conv:
            edit = conv.wait_event(events.MessageEdited(from_users=self.bot))
            deleted = conv.wait_event(events.NewMessage(from_users=self.bot))
            done, pending = await asyncio.wait([edit, deleted], return_when='FIRST_COMPLETED')
        await asyncio.sleep(2)

    async def wait_after_sending_message(self, amount=2):
        async with self.client.conversation(self.bot) as conv:
            for i in range(amount):
                try:
                    await conv.wait_event(events.NewMessage(from_users=self.bot))
                except:
                    logger.error("could not wait")
        await asyncio.sleep(2)
    async def async_click_button(self, tex):
        messages = await self.last_messages()
        button = find_button(messages, tex)
        message = self.get_last_message()
        event = button.click()
        await asyncio.wait({event, message},return_when='FIRST_COMPLETED' )
        await self.wait_after_click_button()

    async def async_send_message(self, message):
        await self.client.send_message(self.bot, message)
        await self.wait_after_sending_message()

    async def async_get_message(self):
        message = await self.get_last_message()
        self.message = message.text

    async def async_check_message(self, search_text):
        messages = await self.last_messages()
        self.check_text = False
        for message in messages:
            if search_text in message.text:
                self.check_text = True
                return

    async def async_check_message_code(self, code):
        messages = await self.last_messages()
        self.check_text = False
        search_text = find_text_from_table(int(code))
        for message in messages:
            if search_text in message.text:
                self.check_text = True
                return

    def click_button(self, tex):
        with self.client:
            self.client.loop.run_until_complete(self.async_click_button(tex))

    def send_message(self, message_text):
        with self.client:
            self.client.loop.run_until_complete(self.async_send_message(message_text))

    def get_message(self):
        with self.client:
            self.client.loop.run_until_complete(self.async_get_message())
            return self.message

    def check_message(self, search_text):
        with self.client:
            self.client.loop.run_until_complete(self.async_check_message(search_text))
        return self.check_text

    def check_message_code(self, code):
        with self.client:
            self.client.loop.run_until_complete(self.async_check_message_code(code))
        return self.check_text
