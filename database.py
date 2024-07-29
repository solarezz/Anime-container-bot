import sqlite3

connection = sqlite3.connect('C:\Python\Anime-container-bot\database.db', check_same_thread=False)
cursor = connection.cursor()

def table_input(user_id: int, username: str):
    cursor.execute('INSERT INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    connection.commit()

def info(user_id: int):
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    return result