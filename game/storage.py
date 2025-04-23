import sqlite3

DB = 'db.sqlite3'
conn = sqlite3.connect(DB, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS games (
    chat_id INTEGER PRIMARY KEY,
    mode TEXT,
    phase TEXT
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS players (
    chat_id INTEGER,
    user TEXT,
    role TEXT,
    PRIMARY KEY (chat_id, user)
)""")
conn.commit()

def new_game(chat_id, mode):
    cursor.execute("REPLACE INTO games VALUES (?,?,?)", (chat_id, mode, 'waiting'))
    conn.commit()

def add_player(chat_id, user):
    cursor.execute("INSERT OR IGNORE INTO players(chat_id,user) VALUES (?,?)", (chat_id, user))
    conn.commit()

def set_phase(chat_id, phase):
    cursor.execute("UPDATE games SET phase=? WHERE chat_id=?", (phase, chat_id))
    conn.commit()

def set_role(chat_id, user, role):
    cursor.execute("UPDATE players SET role=? WHERE chat_id=? AND user=?", (role, chat_id, user))
    conn.commit()

def get_players(chat_id):
    cursor.execute("SELECT user, role FROM players WHERE chat_id=?", (chat_id,))
    return cursor.fetchall()

def get_game(chat_id):
    cursor.execute("SELECT mode, phase FROM games WHERE chat_id=?", (chat_id,))
    return cursor.fetchone()