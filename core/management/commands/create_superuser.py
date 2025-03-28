import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **kwargs):
        username = os.getenv("ADMIN_NAME")
        email = os.getenv("ADMIN_EMAIL")
        password = os.getenv("ADMIN_PASSWORD")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists.'))