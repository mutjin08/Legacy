from django.db import models
from django.contrib.auth.models import User

class CustomGroup(models.Model):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    introduction = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField()
    members = models.ManyToManyField(User, related_name='custom_groups')

    def __str__(self):
        return self.name
