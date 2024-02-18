from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'app'

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('', views.index, name='index'),

    path('<path>', views.table, name='table'),
    path('<path>/create', views.create, name='create'),
    path('<path>/delete/<id>', views.delete, name='delete'),
    path('<path>/update/<id>', views.update, name='update'),

]