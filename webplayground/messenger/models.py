from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField(verbose_name='Mensaje', max_length=500)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        ordering=['created']

class Thread(models.Model):
    user=models.ManyToManyField(User, related_name='threads')
    messages=models.ManyToManyField(Message)