from django.urls import path
from .views import index, academy, manager, mentor, student

app_name = 'main'

urlpatterns = [
    path('v1/', index, name='index'),
    path('academy/<int:pk>/', academy, name='academy'),
    path('manager/<int:pk>/', manager, name='manager'),
    path('mentor/<int:pk>/', mentor, name='mentor'),
    path('student/<int:pk>/', student, name='student')
]
