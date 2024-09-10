# Registration handle for tech.dep

## Description

Basic handle, that takes registration info in POST request, writes it to DB and alerts specified user through telegram
bot

## Tech Stack

    Aiogram
    FastAPI
    Pydantic
    SQLAlchemy
    SQLite

## Installing and launching repository:

### 1. Clone the repository:

    git clone <repository-url>
    cd <cloning-path>

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Set environment variables (Example.env)

    CHAT_ID = 'YOUR-CHAT-ID'
    BOT_TOKEN = 'YOUR-BOT-TOKEN'

### 4. Run

    fastapi run main.py

## Endpoint information:

Address: POST /api/register

Parameters:

- name - supports whitespaces and hyphen (for complex names)
- tg - telegram username, should always start with at sign (@)
- specialty - one of the strings from the list: ['Front-end', 'Back-end', 'Design']

Request body example (JSON):

    {
        "name": "Test",
        "tg": "@Test1",
        "specialty": "Front-end"
    }
    