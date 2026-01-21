from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=100)
    greetings_text = models.CharField(max_length=100)
    bio = models.TextField()
    profile_photo = models.ImageField(upload_to='profile/')

    def __str__(self):
        return self.name
