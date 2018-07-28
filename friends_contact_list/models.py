
from django.db import models


class Friend(models.Model):
    """
    Friend Model
    Defines the attributes of a Friend
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(max_length=70, blank=True, unique=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_email(self):
        return self.name + ' email address is ' + self.email + ' .'

    def __repr__(self):
        return self.name + ' is added.'
