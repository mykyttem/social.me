# Instructions for Running the "social.me" Project

This guide will help you run the Django project "social.me" on your computer. Follow these steps to successfully start the project.

## Step 1: Clone the Repository

```bash
git clone https://github.com/mykyttem/social.me.git
```

## Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For UNIX/Linux
venv\Scripts\activate  # For Windows
```

## Step 3: Install Libraries

```bash
pip install -r requirements.txt
```

## Step 4: Database Migration

```bash
python manage.py makemigrations main_app
python manage.py migrate
```

## Step 5: Step 5: Run the Django Server and Tailwind CSS

```bash
1. python manage.py runserver (first terminal)
2. python manage.py tailwind start (second terminal)
```