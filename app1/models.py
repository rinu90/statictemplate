from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20, help_text='Enter phone number in format: +1234567890')
    email = models.EmailField()
    content = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # Display full name in Django admin

