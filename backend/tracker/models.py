from django.db import models
from django.contrib.auth.models import User # new

# Create your models here.
class TeacherProfile(models.Model):
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)