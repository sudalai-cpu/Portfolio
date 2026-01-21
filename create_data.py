import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from portfolio.models import Home

if not Home.objects.exists():
    Home.objects.create(
        name="Sudalaiyandi Dynamic",
        greetings_text="Hello, I am",
        bio="This content is coming from the database! I am a passionate Developer.",
    )
    print("Created dummy Home object.")
else:
    print("Home object already exists.")
