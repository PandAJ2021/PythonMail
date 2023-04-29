# PythonMail
# Messenger

Messenger is a Python application that allows users to send and receive messages between each other. Users can log in with their username and password, send messages to other users, and view their inbox, draft, and sent folders. The application uses a database to store user information and their messages.

## Features

- User authentication: Users can log in with their username and password to access the application.
- Send messages: Users can send messages to other users by entering the recipient's username and message content.
- View messages: Users can view their inbox, draft, and sent folders to see the messages they have received or sent.
- Draft messages: Users can save messages they have written but not sent in their draft folder.
- Read status: Each message gets a read tag after being read.
- Database storage: User information and messages are stored in a database.

## Dependencies

Messenger requires the following dependencies:

- Python 3.x
- psycopg2: A PostgreSQL database adapter for Python. You can install it with pip:

    ```
    pip install psycopg2
    ```
