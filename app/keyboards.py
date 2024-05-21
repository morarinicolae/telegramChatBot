from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)


from aiogram.utils.keyboard import InlineKeyboardBuilder


from app.database.request import get_categories, get_category_item

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Categorii')],
                                     [KeyboardButton(text='Contacte')],
                                     [KeyboardButton(text='Despre Proiect'),]],
                                      resize_keyboard=True,
                                      input_field_placeholder='Apasa un buton de mai jos')

# catalog = InlineKeyboardMarkup(inline_keyboard=[
#           [InlineKeyboardButton(text='Restaurant', callback_data = 'restaurants')],
#           [InlineKeyboardButton(text='Vinarii', callback_data= 'winery')]])


# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Transmiteti numarul dvs de telefon', 
#                                                            request_contact=True)]],
#                                 resize_keyboard=True)


async def categories():
    all_categories = await get_categories()
    keyboard = InlineKeyboardBuilder()
    for category in all_categories:
        keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
    keyboard.add(InlineKeyboardButton(text="Menu principal", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()

async def items(category_id):
    all_items = await get_category_item(category_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text="Menu principal", callback_data='to_main'))
    return keyboard.adjust(2).as_markup()