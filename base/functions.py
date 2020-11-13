import pyexcel

def find_table():
    table = pyexcel.get_book_dict(file_name='/utiles/bot_file.xls')
    return table

def find_text_from_table(code):
    table = pyexcel.get_book_dict(file_name='/utiles/bot_file.xls')
    for row in table['pyexcel_sheet1']:
        if code in row:
            return row[4]

def find_button(messages, button_name):
    for message in messages:
        for butt_row in message.buttons:
            for button in butt_row:
                if button_name in button.text:
                    return button
