from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.role

class Data_Teacher(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user_rel = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



