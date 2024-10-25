# Hotel Assistant Chatbot Web Application with Rasa and Flask


**Description**: 
This repository contains a web-based chatbot application that serves as a **Hotel Assistant**. The chatbot uses 
**Flask** for the web interface and **Rasa** for natural language processing (NLP) and conversation management. 
The bot can interact with users, handling multiple responses to a single input in a conversational interface, 
providing hotel-related assistance.

## Features

- Hotel-related conversational assistant, providing booking information and answers to the FAQs
- Persistent user login and message history with Flask and SQLAlchemy
- Integration with Rasa to handle natural language responses
- User registration system using SQLAlchemy (prevents duplicate registrations).
- Sample pages: Home, About, Blog, Chat, Login, and Registration

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
<div style="display: flex; flex-wrap: wrap; gap: 10px;"> 
<img src="/imgs/1.jpg" alt="Example Conversation 1" width="200"> 
<img src="/imgs/2.jpg" alt="Example Conversation 2" width="200"> 
<img src="/imgs/3.jpg" alt="Example Conversation 3" width="200"> 
<img src="/imgs/4.jpg" alt="Example Conversation 4" width="200"> 
<img src="/imgs/5.jpg" alt="Example Conversation 5" width="200"> </div>



## Customization
- To expand chatbot capabilities, add more intents, entities, slots, responses and actions in folder 'chatbot'
