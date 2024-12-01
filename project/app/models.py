from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.CharField(max_length=255, unique=True)  # Changed to CharField
    phone = models.CharField(max_length=15, default='Not Provided')
    age = models.CharField(max_length=3, default='18')  # Changed to CharField
    experience = models.CharField(max_length=50, default='0', help_text="Experience in years")  # Changed to CharField
    bio = models.TextField(default='This user has not provided a bio.', blank=True)

    def __str__(self):
        return self.name