from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """model for User."""
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(
        verbose_name='username', max_length=100, blank=True, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=100)
    last_name = models.CharField(verbose_name='second name', max_length=100)
    phone_number = models.CharField(verbose_name='phone number', max_length=10)
    created_at = models.DateField(auto_now_add=True)
    is_student = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Student(models.Model):
    """model for Student."""
    major = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Tutor(models.Model):
    """model for Tutor."""
    education_level = models.CharField(
        verbose_name='education level', max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'
