# teamusers
Create, Edit, and Delete team members rest API
The app is implemented in Python using the Django web framework. The app
uses a MySQL server as the database. All actions (creating, editing, deleting)
is persisted in the database.

Steps to execute the project:

pip install virtualenv

cd my_project_folder

virtualenv my_project

source my_project/bin/activate

pip install djangorestframework

cd my_project 

python manage.py runserver 0.0.0.0:8000

http://localhost:8000/api/users - will list all team members and create one with the below json format the keys are different but made sure all the fields mentioned are used:

{
    "id": 1,
    "first_name": "team1",
    "last_name": "last",
    "email": "manjusha.y009@gmail.com",
    "phone_number": "9022134211",
    "is_superuser": true
}

http://localhost:8000/api/users/1/ - will list user details with id 1 and we can edit / delete this user







