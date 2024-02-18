from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label="email", max_length=20)
    password = forms.CharField(label="password", max_length=20, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    email = forms.EmailField(label="email", max_length=20)
    name = forms.CharField(label="name", max_length=20)
    surname = forms.CharField(label="surname", max_length=20)
    password = forms.CharField(label="password", max_length=20, widget=forms.PasswordInput)


class UserForm(forms.Form):
    email = forms.EmailField(label="email", max_length=20)
    name = forms.CharField(label="name", max_length=20)
    surname = forms.CharField(label="surname", max_length=20)
    password = forms.CharField(label="password", max_length=20, widget=forms.PasswordInput)
    function = forms.CharField(label="function")



class RoomForm(forms.Form):
    office_id = forms.CharField(label="office_id", max_length=20)
    storey = forms.CharField(label="storey")


class OfficeForm(forms.Form):
    affiliate_id = forms.CharField(label="affiliate")
    room_num = forms.IntegerField(label="room_num")
    city = forms.CharField(label="city", max_length=20)


class AffiliateForm(forms.Form):
    adress = forms.CharField(label="adress")
    country = forms.CharField(label="country")


class History_moveForm(forms.Form):
    status_workplace = forms.IntegerField(label="status")
    room_id = forms.IntegerField(label="room_id")
    worker_id = forms.IntegerField(label="worker_id")


class Worker_roomForm(forms.Form):
    room_id = forms.IntegerField(label="room_id")
    worker_id = forms.IntegerField(label="worker_id")
    