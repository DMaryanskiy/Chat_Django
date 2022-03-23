# Chat Django
Simple chat made using Django and Django Channels.

## Description

This is a synchronous app with some asychronous code. It has two routes:

```
/chat/
/chat/<str:room_name>/
```

First route directs to page with single input field. You write there name of a chat, you want to connect to.

Second route directs to chat room you've entered earlier. Also it creates a websocket for asynchronous work.

If you enter message and send it to server it will be shown in all windows with same page opened simultaneously.

## Installation

1. Copy a repository on your computer.
2. Create a virtual environment with `python -m venv venv`.
3. Activate it using `./venv/Scripts/activate`.
4. Install requirements with `pip install -r requirements.txt`.
5. Change your directory to `Chat_Django` using `cd Chat_Django`.
6. Launch application with `python manage.py runserver` and follow the link `http://127.0.0.1:8000`.

## Technology stack

1. Python 3.9.4
2. Django 4.0.3
3. Django-Channels 3.0.4
