import os
os.environ('DJANGO_SETTINGS_MODULE', 'todo.settings')

import django
django.setup()

from faker import Faker
import random
from django.contrib.auth.models import User

fake = Faker()

def populate_users(n):
    for i in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.username()
        email = fake.email()
        password = fake.password()
        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)[0]
        for j in range(random.randint(0, 100)):
            title = fake.sentence(nb_words=24)
            dead_line = fake.date_time()