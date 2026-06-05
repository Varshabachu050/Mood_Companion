# MoodCompanion 

## Overview
MoodCompanion is a student-focused mental wellness web application that helps users track moods, access wellness tools, engage with an AI-style companion chat interface, and use stress-relief activities from a single dashboard.

The project combines:
- SQLite database
- HTML, CSS, and JavaScript frontend
- Responsive dashboard UI
- Mood tracking and history
- Student wellness tools and activities

---

## Features

### 🔐 Authentication
- User registration
- User login
- Guest access option
- Session-based user experience

### 😊 Mood Tracking
- Log moods using emoji selections
- Add mood notes
- Store mood history in SQLite
- View previous mood entries
- Quick mood logging from dashboard

### 💬 Wellness Chat Interface
- Companion chatbot-style UI
- Chat history support
- Quick reply suggestions
- Modern messaging interface

### 🌬️ Breathing Exercises
- Guided breathing animation
- Inhale / Hold / Exhale phases
- Relaxation-focused interaction

### 📈 Dashboard Analytics
- Mood overview
- Streak display
- Recent mood activity
- Daily motivational quotes

### 🎮 Stress Relief Activities
- Tic-Tac-Toe
- Memory Matching Game
- Typing Speed Test
- Color Relaxation Canvas

### 🧩 Mood Quiz
- Interactive wellness questionnaire
- Personalized mood feedback

### 💡 Wellness Tips
- Study tips
- Relaxation techniques
- Student productivity suggestions

### 🎨 UI/UX
- Dark mode and light mode
- Mobile responsive design
- Modern glassmorphism-inspired interface
- Animated components and transitions

## Project Structure

```text
MoodCompanion/
│
├── app.py              # Flask backend
├── index.html          # Main dashboard
├── auth.html           # Login/Register page
├── moodcompanion.db    # SQLite database (generated)
└── README.md
```

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Varshabachu050/Mood_Companion.git
cd moodcompanion
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install flask flask-cors
```

### 5. Run Application

```bash
python app.py
```

Application runs at:

```text
http://127.0.0.1:5000
```

---

## Future Enhancements

- AI-powered mental health assistant
- Mood prediction using Machine Learning
- Sentiment analysis on mood notes
- Weekly wellness reports
- Email reminders
- Journal feature
- OAuth authentication
- Cloud deployment

---

## Security Notes

Current version stores passwords in plain text for development purposes.

For production:
- Use password hashing (bcrypt)
- Add JWT/session authentication
- Enable HTTPS
- Add rate limiting and input validation

---

## Author
Bachu Varsha

