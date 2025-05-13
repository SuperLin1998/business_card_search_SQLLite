import sqlite3
import os

# SQLite 資料庫位置
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'cards.db')

def init_db():
    """初始化資料庫（只需跑一次）"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            raw_text TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_to_sqlite(filename, raw_text):
    """儲存辨識文字到 SQLite"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO cards (filename, raw_text)
        VALUES (?, ?)
    ''', (filename, raw_text))
    conn.commit()
    conn.close()

def get_all_cards():
    """列出資料庫中所有名片紀錄"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, filename, raw_text, created_at FROM cards')
    cards = cursor.fetchall()
    conn.close()
    return cards

def get_connection():
    """取得帶有 dict 功能的 SQLite 連線"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # ✨ 重點：讓 cursor 回傳 dict 而不是 tuple
    return conn
