from django.db import models

# Create your models here.

class Members(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{Members.first_name} {Members.last_name} ({Members.username})"

