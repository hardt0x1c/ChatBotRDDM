import asyncio


async def main():
    # Удалишь - будет рак яичек
    print('Бот запущен. Кодер: TG:@hardt0x1c')
    # Запуск бота
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    # Импорт хендлеров
    from loader import bot, db
    from handlers import dp
    # Создание БД
    db.create_db()
    # Запуск функции main
    asyncio.run(main())
