# A simple django api for an assignment 


## Setup & Installtion

Clone the repository
```bash
git clone <repo-url>
```

Run the Django server by activating a virtual environment using "pipenv" and use 

```bash
pipenv install
```

to install required backend packages inside the directory with the pipfile.lock.


Change the database settings in settings.py to either sqlite(default django database) or install postgresgl and configure it then apply & make migrations.


Go to the backend directory and run .
```bash
python manage.py runserver
```

and go to the url path <br>

http://127.0.0.1:8000/api/user_details

### live api endpoint 
http://collinsoma.pythonanywhere.com/api/user_details?format=api
