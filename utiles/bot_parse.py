from telethon import TelegramClient, events
import os
import asyncio
import pyexcel

""""script to parse bot's answers"""

""" create telegram clients"""
client_dict = eval(os.environ.get('stalone'))
agent_dict = eval(os.environ.get('chan'))
bot = 'sd_test12_bot'

client = TelegramClient('stalone', client_dict['api_id'], client_dict['api_hash'])
agent = TelegramClient('chan', agent_dict['api_id'], agent_dict['api_hash'])
agent.start()

"""create scenarios"""
asd = []
action_list = [
    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Перерахування грн на картку Приватбанк', 'button'], ['Створити тікет на поточну тему', 'button'],
    ['запит', 'text'], ['Відмінити тікет', 'button'], ['Так', 'button'], ['Головне меню', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Перерахування грн на картку Приватбанк', 'button'], ['Створити тікет на поточну тему', 'button'],
    ['Відміна', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Перерахування грн на картку Приватбанк', 'button'], ['Створити тікет на поточну тему', 'button'],
    ['запит', 'text'], ['Відмінити тікет', 'button'], ['Ні', 'button'], ['Головне меню', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Перерахування грн на картку Приватбанк', 'button'], ['Створити тікет на поточну тему', 'button'],
    ['запит', 'text'], ['Взяти тікет', 'agent'], ['Закрити тікет', 'agent'], ['Так', 'agent'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Перерахування грн на картку іншого банку', 'button'], ['Створити тікет на поточну тему', 'button'],
    ['Відміна', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Обмін валюти і перерахування на картку Приватбанк', 'button'], ['Створити тікет на поточну тему', 'button'],
    ['Відміна', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Обмін валюти і перерахування на картку інших банків', 'button'], ['Створити тікет на поточну тему', 'button'],
    ['Відміна', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Щомісячні платежі', 'button'], ['Назад', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Щомісячні платежі', 'button'], ['В головне меню', 'button'],

    ['/start', 'text'], ['Операції по СПД', 'button'], ['Банк', 'button'],
    ['Створити тікет на іншу тему в поточній категорії', 'button'], ['Відміна', 'button'],

    ['/start', 'text'], ['Інформація по виплатам', 'button'], ['В яких числах очікувати зарахування ЗП?', 'button'],
    # ['Замінити файл з інформацією','button'],['Відміна','button'],
    ['В головне меню', 'button'],

    ['/start', 'text'], ['Інформація по виплатам', 'button'], ['Чому сума виплати більша ніж вказана в БОТ?', 'button'],
    ['Назад', 'button'], ['Який у мене залишок ЗП на виплату? (тікет)', 'button'], ['Відмінити тікет', 'button'],
    ['Так', 'button'], ['Головне меню', 'button'],

    ['/start', 'text'], ['Інформація по виплатам', 'button'],
    ['Де я можу побачити суми зарахувань на мій СПД?', 'button'],
    ['В головне меню', 'button'],

    ['/start', 'text'], ['Інформація по виплатам', 'button'], ['Коли мені відкриють СПД?', 'button'],
    ['Назад', 'button'], ['Створити тікет на іншу тему в поточній категорії', 'button'], ['запит', 'text'],
    ['Відмінити тікет', 'button'], ['Так', 'button'], ['Головне меню', 'button'],

    ['/start', 'text'], ['Благодійність', 'button'], ['ST.FAMILY', 'button'], ['запит', 'text'],
    ['Відмінити тікет', 'button'],
    ['Так', 'button'], ['Головне меню', 'button'],

    ['/start', 'text'], ['Благодійність', 'button'], ['ST.HELP', 'button'], ['запит', 'text'],
    ['Відмінити тікет', 'button'],
    ['Так', 'button'], ['Головне меню', 'button'],

    ['/start', 'text'], ['Благодійність', 'button'], ['Інші проекти', 'button'], ['запит', 'text'],
    ['Відмінити тікет', 'button'],
    ['Так', 'button'], ['Головне меню', 'button'],

    ['/start', 'text'], ['Благодійність', 'button'], ['Створити тікет на іншу тему в поточній категорії', 'button'],
    ['Відміна', 'button'],

    ['/start', 'text'], ['Створити тікет на іншу тему', 'button'], ['Відміна', 'button'],

    ['/start', 'text'], ['Help', 'button'],

    ['/start', 'text'], ['Фідбек', 'button'], ['Повідомити про помилку', 'button'], ['помилка', 'text'],

    ['/start', 'text'], ['Фідбек', 'button'], ['Запропонувати поліпшення', 'button'], ['Відміна', 'button'],

    ['/start', 'text'], ['Фідбек', 'button'], ['Відміна', 'button'],

]
current_button = '/start'


def find_button(messages, button_name):
    for message in messages:
        for butt_row in message.buttons:
            for button in butt_row:
                if button_name in button.text:
                    return button


def table_save(event, func, button):
    text = event.text
    amount_button = event.button_count
    code = len(text) + ord(text[0]) + ord(text[-1])
    dic = {
        '1.кнопка чи текст': button,
        '2.код': code,
        '3.функція': func,
        '4.кількість кнопок': amount_button,
        '5.зміст': text
    }
    if dic not in asd:
        asd.append(dic)
    pyexcel.save_as(records=asd, dest_file_name="bot_file.xls")


@client.on(events.NewMessage(from_users='AlexZatushevskiy', pattern=r'(?i)start'))
async def handler_0(event):
    global current_button
    for i in action_list:
        print('-----------------')
        if i[1] == 'text':
            current_button = i[0]
            await client.send_message(bot, i[0])
            await asyncio.sleep(3)
        elif i[1] == 'button':
            current_button = i[0]
            messages = await client.get_messages(bot, limit=2)
            button = find_button(messages, i[0])
            message = client.get_messages(bot, limit=1)
            event = button.click()
            await asyncio.wait({event, message}, return_when='FIRST_COMPLETED')
            await asyncio.sleep(3)
        else:
            current_button = i[0]
            messages = await agent.get_messages(bot, limit=2)
            button = find_button(messages, i[0])
            message = agent.get_messages(bot, limit=1)
            event = button.click()
            await asyncio.wait({event, message}, return_when='FIRST_COMPLETED')
            await asyncio.sleep(3)


@client.on(events.NewMessage(from_users='sd_test12_bot'))
async def handler_1(event):
    print(current_button)
    table_save(event, 'new', current_button)


@client.on(events.MessageEdited(from_users='sd_test12_bot'))
async def handler_2(event):
    print(current_button)
    table_save(event, 'edit', current_button)


"""start program"""
with client:
    client.run_until_disconnected()
