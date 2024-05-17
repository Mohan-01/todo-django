## TODO application using DJANGO

---

### To run this project in your system

Step 1: clone the repository in your system
(Optional) Create a new virtual environment and activate it to run this project i.e not to distrub with your python modules and its versions
Step 2: Run the following commands

`\n1. pip install Django\n2. pip install Faker`
Step 3: Configure the database of your choice in settings.py file (I used mysql)
`\n1. python manage.py makemigrations\n2. python manage.py migrate`
Step 4: Populate the fake data
`python populate.py` then enter the number of records to populate
Step 5: Create a superuser to access the admin panel
`python manage.py createsuperuser` then enter details
Step 6: Run the server
`python manage.py runserver`
