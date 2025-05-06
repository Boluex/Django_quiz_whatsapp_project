🧠 Django Quiz WhatsApp Project
This project integrates Django with thTwilio to deliver an interactive quiz experience via WhatsApp. It allows users to register, receive quiz questions, submit answers, and get feedback—all through WhatsApp messages.

🚀 Features
User registration via WhatsApp

Multiple-choice quiz system

Score calculation and feedback

Admin interface to manage quizzes and users

Django-based backend with a clean API

WhatsApp integration using Twilio API 

🛠️ Tech Stack
Python 3.x

Django 4.x

Django REST Framework

WhatsApp API (Twilio)

SQLite/PostgreSQL (as database)



git clone https://github.com/boluex/Django_quiz_whatsapp_project
.git
cd Django_quiz_whatsapp_project

Create and activate a virtual environment:


python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run migrations:


python manage.py makemigrations
python manage.py migrate
Create a superuser:


python manage.py createsuperuser
Start the development server:


python manage.py runserver
Expose local server (if testing WhatsApp integration):

You can use ngrok to expose your local server:


ngrok http 8000
Then update your WhatsApp webhook URL accordingly.

🔌 WhatsApp Integration
Sign up for a provider like Twilio 

Set up a webhook to receive messages.

Use the API to send and receive messages.

Parse incoming messages and route them to your quiz logic.

🧪 Sample Flow
User sends "START" to the WhatsApp number.

Server responds with a welcome message and first question.

User replies with their answer (e.g., "A", "B", "C").

Server sends next question or final score.

Admin can view all responses in the Django admin panel.

