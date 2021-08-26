## What's this repository about?

Example created for the blog post [How to Use Django's Built-in Login System][blog-post] at [simpleisbetterthancomplex.com][blog].


## How do I run this project locally?

### 1. Clone the repository:

    git clone https://github.com/sibtc/simple-django-login.git

### 2. Run migrations:

    python manage.py migrate

### 3. Create a user:

    python manage.py createsuperuser

### 4. Run the server:

    python manage.py runserver

### 5. And open 127.0.0.1:8000/login in your web browser.

[blog]: http://simpleisbetterthancomplex.com
[blog-post]: http://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html


## getting an error while tryin to "python manage.py migrate"? it's probably your django installation

## django installation (i recon you install everything onto home directory "ex. cd desktop")

### 1. visit brew.sh
### 2. follow basic installation guide
### 3. type "brew install python" into terminal
### 4. finally, type "python -m pip install Django" into terminal

## you can now "python manage.py migrate"
