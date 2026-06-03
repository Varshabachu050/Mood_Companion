from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_PATH = 'moodcompanion.db'

# ── Serve HTML pages ──────────────────────────────
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/auth')
def auth():
    return send_from_directory('.', 'auth.html')

# ── Database setup ────────────────────────────────
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')
    conn.execute('''CREATE TABLE IF NOT EXISTS moods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        emoji TEXT,
        mood TEXT,
        note TEXT,
        logged_at TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.execute('''CREATE TABLE IF NOT EXISTS chats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        role TEXT,
        message TEXT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

# ── Auth routes ───────────────────────────────────
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()
    if not all([name, email, password]):
        return jsonify({'error': 'All fields required'}), 400
    conn = get_db()
    try:
        conn.execute('INSERT INTO users (name, email, password) VALUES (?,?,?)',
                     (name, email, password))
        conn.commit()
        return jsonify({'message': 'Registered!', 'name': name, 'email': email}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Email already exists'}), 409
    finally:
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    conn = get_db()
    user = conn.execute(
        'SELECT * FROM users WHERE email=? AND password=?',
        (data.get('email'), data.get('password'))
    ).fetchone()
    conn.close()
    if user:
        return jsonify({'message': 'OK', 'name': user['name'], 'email': user['email']}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

# ── Mood routes ───────────────────────────────────
@app.route('/api/mood', methods=['POST'])
def log_mood():
    data = request.get_json()
    conn = get_db()
    conn.execute('INSERT INTO moods (user_email, emoji, mood, note) VALUES (?,?,?,?)',
                 (data.get('email'), data.get('emoji'), data.get('mood'), data.get('note','')))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Mood saved!'}), 201

@app.route('/api/mood/<email>', methods=['GET'])
def get_moods(email):
    conn = get_db()
    rows = conn.execute('SELECT * FROM moods WHERE user_email=? ORDER BY logged_at DESC', (email,)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

# ── Run ───────────────────────────────────────────
if __name__ == '__main__':
    init_db()
    print("\n✅ MoodCompanion running at http://127.0.0.1:5000\n")
    app.run(debug=True, port=5000)