from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('create', views.create, name='create'),
    path('read', views.read, name='read'),
    path('update', views.updates, name='update'),
    path('delete', views.delete, name='delete'),
    path('querry', views.querry, name='querry'),
]