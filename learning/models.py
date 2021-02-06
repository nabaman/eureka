from django.db import models
from user_management.models import *

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=255)
    teacher = models.ForeignKey(Data_Teacher, on_delete=models.CASCADE, null=True,blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class ImageMateri(models.Model):
    img = models.ImageField()

    def __str__(self):
        return f'{self.img}'

class Materi(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,null=True)
    materi = models.TextField(null=True)
    gambar = models.ManyToManyField(ImageMateri)
    def __str__(self):
        return f'{self.title}'

class Question(models.Model):
    materi = models.ForeignKey(Materi, on_delete=models.CASCADE, null=True)
    chc = (
        ('text','text'),
        ('choice','choice')
    )
    question = models.CharField(max_length=200,null=True)
    q_type = models.CharField(max_length=200,choices=chc,null=True)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(Choice,on_delete=models.CASCADE, related_name='answer',blank=True,null=True)
    def __str__(self):
        return self.question
