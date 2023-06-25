import os
from dotenv import load_dotenv

load_dotenv()

# токен бота
bot_token = os.getenv('bot_token')
# имя бота
bot_name = os.getenv('bot_name')
# ID админа
admin_id = int(os.getenv('admin_id'))
# Ссылка на проект
link = os.getenv('link')
# Юзернейм админа
admin_name = os.getenv('admin_name')
