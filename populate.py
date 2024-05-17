import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

import django
django.setup()

from faker import Faker
import random
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from todo_app.models import Task

fake = Faker()

def populate_users(n):
    User.objects.all().delete()
    Task.delete_everything(Task)
    print('Deleted all the data')
    for i in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.user_name()
        email = fake.email()
        password = make_password('pass1234')
        user, created = User.objects.get_or_create(
            first_name=first_name, 
            last_name=last_name, 
            username=username, 
            email=email, 
            password=password
        )
        m = random.randint(0, 100)
        for _ in range(m):
            title = fake.sentence(nb_words=4)
            start_date = datetime.datetime.now()
            end_date = start_date + datetime.timedelta(days=10)
            dead_line = start_date + (end_date - start_date) * random.random()
            Task.objects.get_or_create(title=title, dead_line=dead_line, user=user)
        print(f'User {i}, {m} tasks created')
    print('Populate completed successfully')

    
n = int(input('Enter number of users to populate: '))
populate_users(n)
