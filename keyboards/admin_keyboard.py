from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Кнопки админ-панели
admin_panel = [
    [KeyboardButton(text='🎙 Рассылка'),
     KeyboardButton(text='📊 Статистика'),
     KeyboardButton(text='📜 Получить ответы пользователей на викторину')]
]
admin_panel = ReplyKeyboardMarkup(keyboard=admin_panel, resize_keyboard=True)

# Инлайн кнопка главного меню с обнулением состояний
back_menu_inline = [
    [InlineKeyboardButton(text='В главное меню', callback_data='back_menu_inline')]
]
back_menu_inline = InlineKeyboardMarkup(inline_keyboard=back_menu_inline)
