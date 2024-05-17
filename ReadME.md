# TODO Application using Django

## Introduction
This is a simple TODO application built using Django, a high-level Python web framework. Follow the instructions below to set up and run the project on your system.

---

### Step 1: Clone the Repository
Clone the repository to your local system.

(Optional) It's recommended to create a new virtual environment and activate it to isolate the project dependencies from your system's Python modules and versions.

---

### Step 2: Install Dependencies
Run the following commands to install the required dependencies:
```
pip install Django
pip install Faker
pip install mysqlclient
```
 
---

### Step 3: Configure Database
Configure the database of your choice in the `settings.py` file. By default, MySQL is used.
```
python manage.py makemigrations
python manage.py migrate
```

---

### Step 4: Populate Fake Data
To populate the database with fake data, run the following command and specify the number of records to populate:
```
python populate.py
```
---

### Step 5: Create Superuser
Create a superuser account to access the admin panel by running the command and providing the required details:
```
python manage.py createsuperuser
```
---

### Step 6: Run the Server
Start the development server by running the following command:
```
python manage.py runserver
```
---

### Step 7: Access the Application
Open your web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the TODO application.

---

## ReadME.md
This is the ReadME.md file for the project.
