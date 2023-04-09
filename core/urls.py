#схема для core

from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name="history"),
    path('add_operation/', views.add_operation, name='add_operation')
]