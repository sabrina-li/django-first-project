# from django.http import url
from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
]
