import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    weight INTEGER,
    height INTEGER,
    like_bots TEXT
)
''')
conn.commit()
def add_user(user_id, name, age, weight, height, like_bots):
    cursor.execute('''
            INSERT INTO users (id, name, age, weight, height, like_bots)
            VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(id)
            DO UPDATE SET
                name = excluded.name,
                age = excluded.age,
                weight = excluded.weight,
                height = excluded.height,
                like_bots = excluded.like_bots
        ''', (user_id, name, age, weight, height, like_bots))
    conn.commit()


def show_db():
    # обращается к бд 
    # Запрос: выбираем все стоки из таблицы users
    # записываем результат в переменную
    all_lines = cursor.execute('''
        SELECT * FROM users  
    ''')
    return all_lines.fetchall()