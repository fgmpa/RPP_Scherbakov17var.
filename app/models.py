from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    function = models.CharField(max_length=45)


    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

class Affiliate(models.Model):
    id = models.AutoField(primary_key=True)
    adress = models.CharField(max_length=20, null=False)
    country = models.CharField(max_length=20, null=False)
    


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    affiliate = models.ForeignKey(Affiliate, on_delete=models.SET_NULL, null=True)
    room_num = models.IntegerField()
    city = models.CharField(max_length=20, null=False)
    


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    office = models.ForeignKey(Office, on_delete=models.SET_NULL, null=True)
    storey = models.IntegerField()



class History_move(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(auto_now=True)
    status_workplace= models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)



class Worker_room(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
