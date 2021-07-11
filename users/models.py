from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = "Users"
        verbose_name_plural = verbose_name
        ordering = ["-id"]

    def __str__(self):
        return self.username


class Ouser(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.username


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    author = models.CharField(max_length=25)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.course_name


class EnrolledCourse(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)


class WishlistModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username)
