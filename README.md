# Basic Chatbot for Jokes, Fun Facts, and Motivation

**Project Name**: Fun Bot

**Description**: This is a simple chatbot built using Rasa library. The bot provides users with jokes, fun facts, and motivational phrases through a user-friendly web interface.

## Features

- Provides jokes, fun facts, and motivational phrases.
- NLP capabilities powered by Rasa.
- User registration system using SQLAlchemy (prevents duplicate registrations).


## Usage:

```bash

git clone https://github.com/MariamKhoKh/Chatbot.git
```

**Create a virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**Install the dependencies**:

```bash
pip install -r requirements.txt
```

## Running the Chatbot
**Step 1**:

- In one terminal, start the Rasa custom action server:
```bash
rasa run actions
```

- In another terminal, start the Rasa model:
```bash
rasa run
```
- To train the Rasa model (if needed):
```bash
rasa train
```
**Step 2**:
- Run the following command to start the Flask app that powers the user interface:

```bash
python app.py
The application will be available at http://127.0.0.1:5000/ in your browser.
```

- Now, navigate to http://127.0.0.1:5000/ in your browser to access the chatbot

## Example Conversation

```bash
User: Tell me a joke.
Bot: Why don't scientists trust atoms? Because they make up everything!

User: Share a fun fact.
Bot: Did you know? Bananas are berries, but strawberries aren't!

User: I need motivation.
Bot: The only way to do great work is to love what you do. – Steve Jobs
```

## Customization

- To expand chatbot capabilities, add more intents, entities, slots and actions in folder 'chatbot'
