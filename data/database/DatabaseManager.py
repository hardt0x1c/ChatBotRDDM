import sqlite3


class DatabaseManager:
    def __init__(self, db_file):
        # Принимаем путь до БД
        self.db_file = db_file
        # Создание подключения к базе данных
        self.conn = sqlite3.connect(self.db_file)
        # Создание курсора для выполнения SQL-запросов
        self.cursor = self.conn.cursor()

    # Создание БД
    def create_db(self):

        # SQL-запрос для создания таблицы "users"
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY NOT NULL,
            user_id INTEGER UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            first_question TEXT NOT NULL DEFAULT 0,
            second_question TEXT NOT NULL DEFAULT 0,
            third_question TEXT NOT NULL DEFAULT 0
        )
        ''')

        # Сохранение изменений и закрытие соединения
        self.conn.commit()

    # Взять user_id пользователя из БД
    def get_user(self, user_id):
        return self.cursor.execute("SELECT * FROM users WHERE user_id=?;", (user_id,)).fetchone()

    # Добавить пользователя в БД
    def add_user(self, user_id, username, name, surname):
        try:
            self.cursor.execute("INSERT INTO users (user_id, username, name, surname) VALUES (?,?,?,?);",
                                (user_id, username, name, surname))
            self.conn.commit()
            return True
        except:
            return False

    # Взять всех пользователей из БД
    def get_users(self):
        self.cursor.execute('''SELECT user_id FROM users''')
        spam_base = self.cursor.fetchall()
        return spam_base

    # Добавляем ответы на викторину
    def add_questions(self, first_question, second_question, third_question, user_id):
        try:
            self.cursor.execute(
                "UPDATE users SET first_question=?, second_question=?, third_question=? WHERE user_id=?",
                (first_question, second_question, third_question, user_id))
            self.conn.commit()
            return True
        except:
            return False

    def get_users_data(self):
        try:
            self.cursor.execute('SELECT * FROM users')
            users_data = self.cursor.fetchall()
            return users_data
        except Exception as ex:
            print(ex)
            return False
