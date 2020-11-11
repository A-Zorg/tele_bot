from telethon import TelegramClient, events
import os
import asyncio

client_dict = eval(os.environ.get('seagal'))
agent_dict = eval(os.environ.get('chan'))


key_mess_1 = "Для створення тікета виберіть у верхньому меню тему тікета, а потім натисніть [створити тікет ...].\nДля того, щоб залишити фідбек про роботу бота - скористайтеся кнопкою в нижньому меню."
lis=['Операції по СПД','Банк']

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
    def __init__(self, client, bot):
        self.client = client
        self.bot = bot
        self.loop = asyncio.get_event_loop()

    def find_button(self,message, button_name):
        for butt_row in message.buttons:
            for button in butt_row:
                if button_name in button.text:
                    return button

    async def get_last_message(self):
        message = await self.client.get_messages(self.bot, limit=1)
        return message[0]

    async def last_messages(self, quantity=2):
        messages = await self.client.get_messages(self.bot, limit=quantity)
        return messages

    async def wait_after_click_button(self):
        async with self.client.conversation(self.bot) as conv:
            edit = conv.wait_event(events.MessageEdited(from_users=self.bot))
            deleted = conv.wait_event(events.MessageDeleted)
            done, pending = await asyncio.wait([edit, deleted], return_when='FIRST_COMPLETED')

    async def wait_after_sending_message(self, amount=2):
        async with self.client.conversation(self.bot) as conv:
            for i in range(amount):
                try:
                    await conv.wait_event(events.NewMessage(from_users=self.bot))
                except:
                    print('hjjh')

    async def async_click_button(self, tex):
        message = await self.get_last_message()
        button = self.find_button(message, tex)
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




client = TelegramClient('seagal', client_dict['api_id'], client_dict['api_hash'])
agent = TelegramClient('chan', agent_dict['api_id'], agent_dict['api_hash'])
pop = User(agent,'@sd_test12_bot' )
bob = User(client,'@sd_test12_bot')
# but = bob.click_button('Благодійність')
# but = bob.start('Інші проекти')
bob.send_message('/start')
bob.click_button('Операції по СПД')
bob.click_button('Банк')
bob.click_button('Перерахування грн на картку Приватбанк')
bob.click_button('Створити тікет на поточну тему')
bob.send_message('32423dsfsd')

print(pop.check_message('32423dsfsdjgjhg'))


# async def main():
    # await client.send_message('@sd_test12_bot', '/start' )
    # message1 = await client.get_messages('@sd_test12_bot', limit=1)
    # print(message1[0].text)

    # async with client.conversation('@sd_test12_bot') as bot_talk:
    #     edit =  bot_talk.wait_event(events.MessageEdited(from_users='@sd_test12_bot'))
    #     # await bot_talk.wait_event(events.NewMessage(from_users='@sd_test12_bot'))
    #     # await bot_talk.wait_event(events.NewMessage(from_users='@sd_test12_bot'))
    #
    #     delete =  bot_talk.wait_event(events.MessageDeleted())
    #     done, pending = await asyncio.wait([edit, delete], return_when='FIRST_COMPLETED')
    #     print(done)
    #     print(pending)
    #
#     bob = User(client,'@sd_test12_bot')
#     but = await bob.find_button('Благодійність')
#     print(but)
#
# asyncio.get_event_loop().run_until_complete(main())

# with TelegramClient('seagal', client_dict['api_id'], client_dict['api_hash']) as client:
#     client.loop.run_until_complete(main())

# import  pyexcel
#
# di = pyexcel.get_book_dict(file_name='C:/Users/sasa/Desktop/111.xlsx')
#
# print(di['Лист1'][1])

# wb = load_workbook('C:/Users/sasa/Desktop/111.xlsx')
# sh = wb['Лист1']
# print(sh.max_column)

