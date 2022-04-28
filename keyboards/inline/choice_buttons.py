from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import URL_MERCEDES, URL_TOYOTA, URL_KIA, URL_LEXUS, URL_BMW

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2)

buy_pear = InlineKeyboardButton(text="Mercedes", callback_data=buy_callback.new(item_name="buy:Mercedes", quantity=1))

choice.insert(buy_pear)

buy_apples = InlineKeyboardButton(text="Toyota", callback_data="buy:Toyota:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Kia", callback_data="buy:Kia:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="Lexus", callback_data="buy:Lexus:5")

choice.insert(buy_apples)

buy_apples = InlineKeyboardButton(text="BMW", callback_data="buy:BMW:5")

choice.insert(buy_apples)

cancel_button = InlineKeyboardButton(text="Cancel", callback_data="cancel")

choice.insert(cancel_button)

pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="Visit", url=URL_MERCEDES)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_TOYOTA)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_KIA)

    ]

])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_LEXUS)

    ]



])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [

        InlineKeyboardButton(text="visit", url=URL_BMW)

    ]

])