## AskSphere

A Django-based question-answer system where users can post questions, answer them, and like answers.

Features
1. User authentication (signup, login, logout)
2. Post questions
3. Answer questions
4. Like answers

## Prerequisites
Python, Django, Django REST Framework, HTML, Bootstrap

## Run project locally
- Clone the project from github using httpUrl or sshUrl into you project directory
```bash
  git clone https://github.com/RajiwadeVedanti/AskSphere.git or git@github.com:RajiwadeVedanti/AskSphere.git
```

- Create and Activate Virtual Environment
```bash
   python -m venv venv
   source venv/bin/activate 
```

- Install packages required for project
```bash
  pip install -r requirements. txt
```

- Go to project directory
```bash
  cd ask_sphere
```

- Run the server. port_number is optional, by default it will be 8000
```bash
  python manage.py runserver <port_number>
```

- If new changes are made in models.py, app_name is optional
```bash
  python manage.py makemigrations <app_name>
```

- Run migrate again to create those model tables in your database
```bash
    python manage.py migrate
```

